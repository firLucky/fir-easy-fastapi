import os

from starlette.middleware.cors import CORSMiddleware

from src.api.v1.user_controller import user_router
from src.common import global_exception_handler
from src.common.singleton import Singleton
from src.entity import user, department
from src.config.initialize.event_handlers import register_events
from src.config.filter import dependencies
from src.api.v1.sys_controller import sys_router
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI


def fir_app():
    # 拦截器
    dependencies_all = dependencies.all_dependencies()

    # 判断是否是开发环境，只有在开发环境中，才使用在线文档功能
    database_url = os.environ.get('ENV')
    openapi_url = None
    docs_url = None
    redoc_url = None
    if database_url == 'dev':
        openapi_url = "/openapi.json"
        docs_url = "/swagger-ui.html"
        redoc_url = "/redoc"
    # 构建服务
    app = FastAPI(title="杉极简", version="1.0.1",
                  dependencies=dependencies_all,
                  openapi_url=openapi_url,
                  docs_url=docs_url,
                  redoc_url=redoc_url,
                  )
    # 允许跨域配置
    app.add_middleware(
        CORSMiddleware,
        # 允许的域名
        allow_origins=["*"],
        allow_credentials=True,
        # 允许的 HTTP 方法，["GET", "POST", "PUT", "DELETE", "OPTIONS"]
        allow_methods=["*"],
        # 允许的请求头
        allow_headers=["*"],
    )
    # 控制层
    app.include_router(sys_router)
    app.include_router(user_router)
    # 注册异常处理器
    global_exception_handler.exception_register(app)
    # 服务启动与关闭触发方法
    register_events(app)
    singleton = Singleton()
    quoted_user = singleton.quoted_user
    quoted_password = singleton.quoted_password
    database_url = singleton.database_url
    # 配置 TortoiseORM 连接数据库
    db_auth = f"mysql://{quoted_user}:{quoted_password}@"
    db_url = database_url.replace("mysql://", db_auth, 1)
    register_tortoise(
        app,
        db_url=db_url,
        # 数据对象
        modules={"entity": [user, department]},
        # 禁用自动生成数据库表
        generate_schemas=False,
        add_exception_handlers=True,
    )

    return app

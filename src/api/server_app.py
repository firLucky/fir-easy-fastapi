import os
from src.api.v1.user_controller import user_router
from src.common import global_exception_handler
from src.entity import user, department
from src.config.initialize.event_handlers import register_events
from src.config.filter import dependencies
from src.api.v1.sys_controller import sys_router
from tortoise.contrib.fastapi import register_tortoise
from urllib.parse import quote_plus
from fastapi import FastAPI


def fir_app():
    # 拦截器
    dependencies_all = dependencies.all_dependencies()

    # 构建服务
    app = FastAPI(title="杉极简", version="0.0.1",
                  dependencies=dependencies_all,
                  docs_url="/swagger-ui.html",
                  )
    # 控制层
    app.include_router(sys_router)
    app.include_router(user_router)
    # 注册异常处理器
    global_exception_handler.exception_register(app)
    # 服务启动与关闭触发方法
    register_events(app)

    # 配置 TortoiseORM 连接数据库
    database_url = os.environ.get('DATABASE_URL')
    database_user = os.environ.get('DATABASE_USER')
    database_password = os.environ.get('DATABASE_PASSWORD')
    # 转义密码中的特殊字符
    quoted_user = quote_plus(database_user)
    quoted_password = quote_plus(database_password)
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

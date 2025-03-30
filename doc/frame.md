## 框架说明

### 启动类文件

文件位置

```
src/application.py
```

```python
import argparse
import os

import uvicorn
from dotenv import load_dotenv
from src.api.server_app import fir_app
from src.config.initialize.initialize_utils import initialize_trigger
from src.config.initialize.launch_title import start_logo_log


def main():
    """
    项目启动方法
    """
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="获取命令行参数")
    # 添加参数
    parser.add_argument('--active', type=str)
    # 解析命令行参数
    args = parser.parse_args()

    # 执行项目启动前的初始化
    initialize_trigger()
    env_active = args.active
    if env_active is None:
        env_active = "dev"
    env_file = f'src/resources/{env_active}.env'

    if os.path.exists(env_file):
        load_dotenv(env_file)
        server_port = os.environ.get('SERVER.PORT')
        server_port = int(server_port)
        server_host = os.environ.get('SERVER.HOST')
        start_logo_log()
        uvicorn.run(fir_app, host=server_host, port=server_port, log_config="src/resources/uvicorn_config.json",
                    use_colors=True,
                    loop="asyncio",
                    )
    else:
        raise Exception(".启动失败--env配置文件不存在")


if __name__ == "__main__":
    # 启动主程序方法
    main()

```

uvicorn_config.json配置系统日志框架输出。

### 配置文件

文件位置

```
src/resources/dev.env
```

加载配置文件

```
默认加载.env.dev
```

体现在启动类文件中该部分

```python
    # 执行项目启动前的初始化
    initialize_trigger()
    env_active = args.active
    if env_active is None:
        env_active = "dev"
    env_file = f'src/resources/.env.{env_active}'
```

里面有类似一下内容

```
# *******************数据库配置********************
DATABASE_URL=mysql://127.0.0.1:13306/fir_fast
DATABASE_USER=root
DATABASE_PASSWORD=123456
# *******************数据库配置********************
```

#### 简单调用

在系统中进行调用

```
import os

DATABASE_URL = os.environ.get('DATABASE_URL')
print(DATABASE_URL)
```

可以通过不同的启动参数选择配置文件

```
python application.py --active test
```

#### 单例调用

推荐使用单例模式进行初始化调

```
src/common/Singleton
```

需要设置变量并且给与相应的get，set方法

```python
	# 令牌前缀
	jwt_token_head = None

    @classmethod
    def set_jwt_token_head(cls, value):
        cls.jwt_token_head = value

    @classmethod
    def get_jwt_token_head(cls):
        return cls.jwt_token_head
```

在此进行项目启动时的变脸初始化

```python
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            jwt_token_head = os.environ.get('JWT_TOKEN_HEAD')
            cls._instance.jwt_expiration = jwt_expiration
```

在系统中的调用，先实例化该类，在死用get方法进行参数的调用

```python
    singleton = Singleton()
    jwt_token_head = singleton.get_jwt_token_head()
```

#### 配置文件说明

##### 接口白名单

修改一下配置

```
SERVER.WHITE.URL=['/auth/login','/auth/logout']
```



### 拦截器

```python
    # 构建服务器
    app = FastAPI(title="杉极简", version="0.0.1",
                  dependencies=dependencies_all
                  )
```

#### token拦截器

#### swagger页面使用Authorization请求头

使得swagger页面使用Authorization请求头，需要进行如下设置，之后就可以在页面输入token。

```python
from fastapi.security import APIKeyHeader
from fastapi import Depends, Request, Security

api_token_key = APIKeyHeader(name='Authorization', auto_error=False)

async def verify_token(request: Request, Authorization=Security(api_token_key)):
```

![image-20241223171602613](frame.assets/image-20241223171602613.png)

![image-20241223171613294](frame.assets/image-20241223171613294.png)

#### 拦截器完整代码

```python
import os

from fastapi import Depends, Request, Security
from fastapi.security import APIKeyHeader
from src.common.global_exception_handler import DescriptionException
from src.config.result.api_code import ApiCode
from src.config.sys.cache_utils import cache

api_token_key = APIKeyHeader(name='Authorization', auto_error=False)


async def verify_token(request: Request, Authorization=Security(api_token_key)):
    """
    token拦截器
    :param Authorization: 请求令牌
    :param request: 请求头
    :return: 通过/拦截返回401
    """

    # 生产环境下，应开启token拦截器
    jwt_filter = os.getenv('JWT_FILTER', 'false').lower() == 'true'
    if not jwt_filter:
        return None

    if request.url.path == "/auth/login":
        return None

    if not Authorization:
        raise DescriptionException(ApiCode.ACCESS_DENIED)
    user = cache.get(Authorization)

    if not user:
        raise DescriptionException(ApiCode.ACCESS_DENIED)

    return Authorization


def all_dependencies():
    """
    请求拦截器
    1.处理token
    :return:
    """
    return [Depends(verify_token)]

```

### 全局异常处理器

```
    # 注册异常处理器
    global_exception_handler.exception_register(app)
```

实现方式

```python
import logging

from fastapi import FastAPI

from src.config.result.api_result import ApiResult
from src.config.result.api_code import ApiCode

log = logging.getLogger("uvicorn")


class DescriptionException(Exception):
    """
    自定义异常-登录超时
    """

    def __init__(self, api_code: ApiCode):
        message = api_code.description
        code = api_code.code
        self.code = code
        self.message = message
        super().__init__(code, message)


def exception_register(app: FastAPI):
    """
    异常处理注册
    """
    app.exception_handler(DescriptionException)(description_exception)
    app.exception_handler(Exception)(exception_handler)


async def description_exception(request, exc):
    """
    自定义异常处理器-通用
    :param request: 请求
    :param exc: 异常描述
    :return: 统一返回值
    """
    log.error(f"通用自定义异常: {exc}")
    message = str(exc.message) or "请求失败！"
    return ApiResult.fail(code=exc.code, message=message)


async def exception_handler(request, exc):
    """
    默认Exception异常
    :param request: 请求
    :param exc: 异常
    :return: 请求失败描述
    """
    log.error(f"全局异常捕捉: {exc}")
    return ApiResult.fail(code=500, message="请求失败！")

```

### MySQL+TortoiseORM配置

```python
    # 配置 TortoiseORM
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
        modules={"entity": [models, department]},
        # 禁用自动生成数据库表
        generate_schemas=False,
        add_exception_handlers=True,
    )
```

### 统一返回值

#### 返回值实体类

```python
from fastapi import status
from fastapi.responses import JSONResponse, Response
from typing import Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from tortoise.models import Model


class ApiResult:
    """统一异常返回类"""

    @classmethod
    def success(cls, data: Union[list, dict, str, bool, Model, BaseModel] = None) -> Response:
        """
        通用-请求成功
        :param data:
        :return:
        """
        json_compatible_item_data = jsonable_encoder(data)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'code': 200,
                'message': "请求成功",
                'data': json_compatible_item_data,
            }
        )

    @classmethod
    def fail(cls, code: int = 400,
             message: str = "请求失败",
             data: Union[list, dict, str, Model, BaseModel] = None,
             ) -> Response:
        """
        通用-失败请求返回体
        :param code: 状态码
        :param message: 描述
        :param data: 请求数据
        :return:
        """
        json_compatible_item_data = jsonable_encoder(data)
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'code': code,
                'message': message,
                'data': json_compatible_item_data,
            }
        )

```

#### 状态描述枚举类

```python
from enum import Enum


class ApiCodeCustomEnum(Enum):
    def __init__(self, code: int, description: str):
        self._value_ = code
        self.description = description

    def __str__(self):
        return f"{self.__class__.__name__}.{self.name}: (Code: {self.value}, Description: {self.description})"

    @property
    def code(self):
        return self._value_


class ApiCode(ApiCodeCustomEnum):
    """
    接口返回码
    """
    ACCESS_DENIED = (401, "登录过期!")
    ERROR_USER_PASS = (400, "用户名或密码错误!")

```

#### 应用示例

在特定的情况下抛出异常，前端将会接收到相应的参数

```
DescriptionException(ApiCode.ERROR_USER_PASS)
```

```python
    async def login(self, username: str, password: str, user_service: UserService) -> UserDto:
        """
        登录

        :param user_service:
        :param username: 用户名
        :param password: 用户密码
        :return: 用户登录信息
        """
        user = await user_service.get_user_by_username_password(username=username, password=password)
        if user is None:
            raise DescriptionException(ApiCode.ERROR_USER_PASS)
```


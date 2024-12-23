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

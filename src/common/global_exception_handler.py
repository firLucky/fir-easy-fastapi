import logging

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

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
    # 处理有关于接口参数缺失异常
    app.exception_handler(RequestValidationError)(request_validation_error_exception)
    app.exception_handler(Exception)(exception_handler)

async def request_validation_error_exception(request, exc):
    """
    服务器无法处理请求的实体数据(JSON)
    JSON数据格式错误
    缺少必需的字段
    字段类型错误
    :return: 统一返回值
    """
    api_code = ApiCode.ERROR_PARAMETER_MISS
    log.error(f"通用自定义异常: {api_code.description}")
    message = str(api_code.description) or "请求失败！"
    return ApiResult.fail(code=api_code.code, message=message)

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

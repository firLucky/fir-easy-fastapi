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

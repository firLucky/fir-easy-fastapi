import os

from src.common.global_exception_handler import DescriptionException
from src.config.result.api_code import ApiCode
from src.dto.user_dto import UserDto
from src.config.sys.cache_utils import cache
from src.service.sys_service import SysService
from src.service.user_service import UserService
from src.utils.security_utils import create_access_token


class SysServiceImpl(SysService):
    """
    用户实现层
    """

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
        access_token = create_access_token(uid=user.id, uname=user.username)
        user_dto = UserDto(username=user.username, token=access_token)

        jwt_expiration = os.environ.get('JWT_EXPIRATION')
        jwt_expiration = int(jwt_expiration)
        cache.set(access_token, user_dto, expire=jwt_expiration)
        return user_dto

    async def logout(self, authorization: str) -> bool:
        """
        登出

        :param authorization: 用户认证令牌
        :return: 成功/失败
        """
        cache.delete(authorization)
        return True

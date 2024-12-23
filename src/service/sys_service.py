from abc import ABC, abstractmethod

from src.dto.user_dto import UserDto
from src.service.user_service import UserService


class SysService(ABC):
    """
    用户接口
    """

    @abstractmethod
    async def login(self, username: str, password: str, user_service: UserService) -> UserDto:
        """
        登录

        :param username: 用户名
        :param password: 用户密码
        :param user_service: 用户接口
        :return: 用户登录信息
        """
        pass

    @abstractmethod
    async def logout(self, authorization: str) -> bool:
        """
        登出

        :param authorization: 用户认证令牌
        :return: 成功/失败
        """
        pass


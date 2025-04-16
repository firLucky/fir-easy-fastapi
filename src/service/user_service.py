from abc import ABC, abstractmethod
from typing import List, Optional
from fastapi import Depends
from src.dependencies.sys_dependencies import get_user_mapper
from src.dto.user import CreateUserDTO, UpdateUserDTO, deleteUserDTO
from src.dto.user.user_dto import UserDTO
from src.dto.user_department_dto import UserDepartmentDTO
from src.entity.user import User
from src.mapper.user_mapper import UserMapper


class UserService(ABC):
    """
    用户接口
    """

    @abstractmethod
    async def create_user(self, create_user_dto: CreateUserDTO) -> UserDTO:
        """
        创建一个新用户。

        :param create_user_dto: 用户信息
        :return: 用户对象
        """
        pass

    @abstractmethod
    async def get_user(self, user_id: int) -> Optional[UserDTO]:
        """
        根据用户ID获取用户信息。

        :param user_id: 用户的唯一标识符
        :return: 用户对象
        """
        pass

    @abstractmethod
    async def get_all_users(self) -> List[UserDTO]:
        """
        获取所有用户的信息。

        :return: 用户对象的列表
        """
        pass

    @abstractmethod
    async def update_user(self, update_user_dto: UpdateUserDTO) -> bool:
        """
        更新指定用户的信息。

        :param update_user_dto: 用户信息
        :return: 更新后的用户对象
        """
        pass

    @abstractmethod
    async def delete_user(self, delete_user_dto: deleteUserDTO) -> bool:
        """
        删除指定用户。

        :param delete_user_dto: 删除用户信息
        :return: 删除操作是否成功
        """
        pass

    @abstractmethod
    async def get_user_department(self, user_id: int, user_mapper: UserMapper = Depends(get_user_mapper)) \
            -> UserDepartmentDTO:
        """
        获取所属部门。

        :param user_mapper:
        :param user_id: 用户的唯一标识符
        :return: 用户部门信息
        """
        pass

    @abstractmethod
    async def get_user_by_username_password(self, username: str, password: str,
                                            user_mapper: UserMapper = Depends(get_user_mapper)) \
            -> User:
        """
        通过用户密码，获取用户信息

        :param username: 用户名称
        :param password: 用户密码
        :param user_mapper:
        :return: 用户信息
        """
        pass

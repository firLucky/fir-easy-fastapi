from typing import List, Optional

from fastapi import Depends

from src.dto.user import CreateUserDTO, UpdateUserDTO
from src.dto.user.user_dto import UserDTO
from src.dto.user_department_dto import UserDepartmentDTO
from src.entity.user import User
from src.mapper.user_mapper import UserMapper
from src.service.user_service import UserService
from src.dependencies.sys_dependencies import get_user_mapper


class UserServiceImpl(UserService):
    """
    用户实现层
    """

    async def create_user(self, create_user_dto: CreateUserDTO
                          ) -> UserDTO:
        """
        创建一个新用户。

        :param create_user_dto: 用户信息
        :return: 用户对象
        """
        user = await User.create(username=create_user_dto.username, password=create_user_dto.password)
        user_dto = UserDTO(
            id=user.id,
            username=user.username,
            password=user.password,
        )
        return user_dto

    async def get_user(self, user_id: int) -> Optional[UserDTO]:
        """
        根据用户ID获取用户信息。

        :param user_id: 用户的唯一标识符
        :return: 用户对象
        """
        user_dto = None
        user = await User.filter(id=user_id).first()
        if not user:
            user_dto = UserDTO(
                id=user.id,
                username=user.username,
                password=user.password,
            )
        return user_dto

    async def get_all_users(self) -> List[UserDTO]:
        """
        获取所有用户的信息。

        :return: 用户对象的列表
        """
        user_list = []
        users = await User.all()
        for item in users:
            user = UserDTO(
                id=item.id,
                username=item.username,
                password=item.password,
            )
            user_list.append(user)
        return user_list

    async def update_user(self, update_user_dto: UpdateUserDTO) -> bool:
        """
        更新指定用户的信息。

        :param update_user_dto: 用户信息
        :return: 更新后的用户对象
        """
        user_id = update_user_dto.user_id
        username = update_user_dto.username
        password = update_user_dto.password
        user = await User.filter(id=user_id).first()
        if not user:
            if username:
                user.username = username

            if username:
                user.password = password
            await user.save()
        return True

    async def delete_user(self, user_id: int) -> bool:
        """
        删除指定用户。

        :param user_id: 要删除的用户ID
        :return: 删除操作是否成功
        """
        user = await User.filter(id=user_id).first()
        if not user:
            await user.delete()
        return True

    async def get_user_department(self, user_id: int,
                                  user_mapper: UserMapper = Depends(get_user_mapper)) -> UserDepartmentDTO:
        """
        获取所属部门。

        :param user_mapper:
        :param user_id: 用户的唯一标识符
        :return: 用户部门信息
        """
        return await user_mapper.get_user_department(user_id)

from typing import List, Optional

from fastapi import Depends

from src.dto.user_department_dto import UserDepartmentDTO
from src.entity.user import User
from src.mapper.user_mapper import UserMapper
from src.service.user_service import UserService
from src.dependencies.sys_dependencies import get_user_mapper


class UserServiceImpl(UserService):
    """
    用户实现层
    """

    async def create_user(self, username: str, email: str, is_active: bool = True) -> User:
        """
        创建一个新用户。

        :param username: 用户名
        :param email: 邮件地址
        :param is_active: 激活状态
        :return: 用户对象
        """
        user = await User.create(username=username, email=email, is_active=is_active)
        return user

    async def get_user(self, user_id: int) -> Optional[User]:
        """
        根据用户ID获取用户信息。

        :param user_id: 用户的唯一标识符
        :return: 用户对象
        """
        user = await User.filter(id=user_id).first()
        if not user:
            return None
        return user

    async def get_all_users(self) -> List[User]:
        """
        获取所有用户的信息。

        :return: 用户对象的列表
        """
        users = await User.all()
        return users

    async def update_user(self, user_id: int, username: Optional[str] = None, email: Optional[str] = None,
                          is_active: Optional[bool] = None) -> Optional[User]:
        """
        更新指定用户的信息。

        :param user_id: 要更新的用户ID
        :param username: 新用户名（可选）
        :param email: 新邮件地址（可选）
        :param is_active: 新激活状态（可选）
        :return: 更新后的用户对象
        """
        user = await User.filter(id=user_id).first()
        if not user:
            return None

        if username:
            user.username = username
        if email:
            user.email = email
        if is_active is not None:
            user.is_active = is_active

        await user.save()
        return user

    async def delete_user(self, user_id: int) -> bool:
        """
        删除指定用户。

        :param user_id: 要删除的用户ID
        :return: 删除操作是否成功
        """
        user = await User.filter(id=user_id).first()
        if not user:
            return False
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

    async def get_user_by_username_password(self, username: str, password: str,
                                            user_mapper: UserMapper = Depends(get_user_mapper)) -> User:
        """
        通过用户密码，获取用户信息

        :param username: 用户名称
        :param password: 用户密码
        :param user_mapper:
        :return: 用户信息
        """
        user = await User.filter(username=username, password=password).first()
        return user

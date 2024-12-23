from abc import ABC, abstractmethod

from src.dto.user_department_dto import UserDepartmentDTO


class UserMapper(ABC):
    """
    用户接口
    """

    @abstractmethod
    async def get_user_department(self, user_id: int) -> UserDepartmentDTO:
        """
        获取用户部门信息

        :param user_id: 用户id
        :return: 用户部门信息
        """
        pass

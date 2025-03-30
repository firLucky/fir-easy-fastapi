from typing import List

from pydantic import BaseModel, Field

from src.dto.user.user_dto import UserDTO


class CreateUserDTO(BaseModel):
    """
    创建用户
    """
    username: str = Field(description="用户名")

class CreateUserResponseDTO(BaseModel):
    """
    创建用户接口返回示例
    """
    code: int = Field(description="状态码")
    message: str = Field(description="描述信息")
    data: CreateUserDTO = Field(description="用户信息")

class ListResponseDTO(BaseModel):
    """
    创建用户接口返回示例
    """
    code: int = Field(description="状态码")
    message: str = Field(description="描述信息")
    data: List[UserDTO] = Field(description="用户信息集合")

class UserResponseDTO(BaseModel):
    """
    创建用户接口返回示例
    """
    code: int = Field(description="状态码")
    message: str = Field(description="描述信息")
    data: UserDTO = Field(description="用户信息")

class UpdateUserDTO(BaseModel):
    """
    更新用户
    """
    user_id: int = Field(description="用户编号")
    username: str = Field(description="用户名")
    password: str = Field(description="用户密码")

class deleteUserDTO(BaseModel):
    """
    删除用户
    """
    user_id: int = Field(description="用户编号")
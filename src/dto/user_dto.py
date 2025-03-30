from pydantic import BaseModel, Field
from typing import Optional


class UserDto(BaseModel):
    """
    用户登录信息
    """
    username: Optional[str] = Field(None, description="用户名称")
    token: Optional[str] = Field(None, description="用户名称")


class UserDtoResponse(BaseModel):
    """
    用户登录信息(返回示例)
    """
    code: int = Field(description="状态码")
    message: str = Field(description="描述信息")
    data: UserDto


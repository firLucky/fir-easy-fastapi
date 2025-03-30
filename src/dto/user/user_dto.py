from pydantic import BaseModel, Field


class UserDTO(BaseModel):
    """
    用户信息
    """
    id: int = Field(description="主键编号")
    username: str = Field(description="用户登录名")
    password: str = Field(description="用户密码")

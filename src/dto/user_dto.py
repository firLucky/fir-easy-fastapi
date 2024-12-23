from pydantic import BaseModel


class UserDto(BaseModel):
    """
    用户登录信息
    """
    username: str
    token: str

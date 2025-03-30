from pydantic import BaseModel, Field


class StateResponse(BaseModel):
    """
    请求状态(返回示例)
    """
    code: int = Field(description="状态码")
    message: str = Field(description="描述信息")
    data: bool = Field(description="成功(True)/失败(False)")

class UserRequest(BaseModel):
    """
    用户登录
    """
    username: str = Field(description="用户名")
    password: str = Field(description="密码")

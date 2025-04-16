from pydantic import BaseModel, Field


class UserDepartmentDTO(BaseModel):
    """
    用户部门信息
    """
    user_id: int = Field(None, description="用户编号")
    username: str = Field(None, description="用户名称")
    dept_name: str = Field(None, description="部门名称")
    dept_code: int = Field(None, description="部门编号")

class UserDepartmentDTOResponse(BaseModel):
    """
    请求状态信息
    """
    code: int = Field(description="状态码")
    message: str = Field(description="描述信息")
    data: UserDepartmentDTO = Field(description="成功(True)/失败(False)")
from pydantic import BaseModel, Field


class UserDepartmentDTO(BaseModel):
    """
    用户部门信息
    """
    username: str = Field(description="用户名称")
    department_name: str = Field(description="部门名称")
    department_code: str = Field(description="部门编号")

class UserDepartmentDTOResponse(BaseModel):
    """
    请求状态信息
    """
    code: int = Field(description="状态码")
    message: str = Field(description="描述信息")
    data: UserDepartmentDTO = Field(description="成功(True)/失败(False)")
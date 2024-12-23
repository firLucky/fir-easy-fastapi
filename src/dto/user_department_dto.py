from pydantic import BaseModel
from typing import Optional


class UserDepartmentDTO(BaseModel):
    """
    用户部门信息
    """
    username: str
    department_name: Optional[str] = None
    department_code: Optional[str] = None

from pydantic import BaseModel, Field
from typing import Optional


class ChatDto(BaseModel):
    """
    用户登录信息
    """
    content: Optional[str] = Field( description="内容")


from pydantic import BaseModel, Field


class AiChatBodyDTO(BaseModel):
    """
    用户对话
    """
    msg: str = Field(description="用户问题")
    stream: bool = Field(True, description="用户问题")

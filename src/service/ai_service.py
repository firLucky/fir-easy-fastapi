from abc import ABC, abstractmethod

from fastapi.responses import StreamingResponse

from src.dto.ai.ai_chat_dto import AiChatBodyDTO


class AiService(ABC):
    """
    AI业务 接口层
    """

    @abstractmethod
    async def ai_chat(self, ai_chat_body_dto: AiChatBodyDTO) -> StreamingResponse:
        """
        流式对话

        :param ai_chat_body_dto: 用户问题信息
        :return: 用户对象
        """
        pass

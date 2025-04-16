import asyncio
import json
import logging

from src.dto.ai.ai_chat_dto import AiChatBodyDTO
from src.dto.ai.chat_dto import ChatDto
from src.service.ai_service import AiService
from fastapi.responses import StreamingResponse

log = logging.getLogger("uvicorn")


class AiServiceImpl(AiService):
    """
    系统管理 实现层
    """

    async def ai_chat(self, ai_chat_body_dto: AiChatBodyDTO) -> StreamingResponse:
        """
        流式对话

        :param ai_chat_body_dto: 用户问题信息
        :return: 用户对象
        """
        msg = ai_chat_body_dto.msg
        stream = ai_chat_body_dto.stream
        return StreamingResponse(self.llm(msg, stream), media_type="text/plain")

    @staticmethod
    async def llm(msg: str, stream=False):
        log.info(f"AI机器人接受问题[{msg}],正在处理... ")
        result = ""
        responses = [
            "你好，",
            "我是",
            "Chat",
            "我可以",
            "帮助你",
            "解答各",
            "种问题，",
            "包括",
            "编程、",
            "写作、",
            "学习等。",
            "如果你",
            "有任何问题，",
            "请随时告诉我！",
            "我会尽力",
            "提供最",
            "准确的",
            "答案。",
            "现在",
            "就开",
            "始交",
            "流吧！"
        ]
        for chunk in responses:
            chat_dto = ChatDto(
                content=chunk,
            )
            yield json.dumps(chat_dto.dict(), ensure_ascii=False) + "\n"
            # 模拟堵塞，允许异步
            await asyncio.sleep(0.1)
            result = result + chunk
        log.info(f"AI机器人处理问题完成[{msg}],当前回复为:[{result}]")

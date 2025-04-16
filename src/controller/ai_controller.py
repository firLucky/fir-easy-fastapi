from fastapi import APIRouter, Depends, Body

from src.dto.ai.ai_chat_dto import AiChatBodyDTO
from src.dto.common import StateDTOResponse
from src.service.ai_service import AiService
from src.service.impl.ai_service_impl import AiServiceImpl

ai_router = APIRouter(prefix="/ai", tags=["AI业务"])


def get_ai_service() -> AiService:
    """
    AI业务 接口层
    """
    return AiServiceImpl()


@ai_router.post(
    "/chat",
    summary="流式对话",
    description="接受用户问题，进行流式回答",
    response_description="对话返回数据",
    response_model=StateDTOResponse,
)
async def ai_chat(
        ai_chat_body_dto: AiChatBodyDTO = Body(description="更新用户"),
        ai_service: AiService = Depends(get_ai_service)):
    data = await ai_service.ai_chat(ai_chat_body_dto)
    return data
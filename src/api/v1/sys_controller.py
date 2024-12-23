import logging
from fastapi import APIRouter, Request, Query, Depends
from src.config.result.api_result import ApiResult
from src.service.impl.sys_service_impl import SysServiceImpl
from src.service.impl.user_service_impl import UserServiceImpl
from src.service.sys_service import SysService
from src.service.user_service import UserService

sys_router = APIRouter(prefix="/auth", tags=["系统管理"])

log = logging.getLogger("uvicorn")


# 通过依赖注入返回服务实例
def get_sys_service() -> SysService:
    return SysServiceImpl()


def get_user_service() -> UserService:
    return UserServiceImpl()


@sys_router.post(
    "/login",
    summary="用户登录",
    description="用户登录",
    response_description="用户信息",
)
async def login(
        username: str = Query(None, description="用户名"),
        password: str = Query(None, description="用户密码"),
        sys_service: SysService = Depends(get_sys_service),
        user_service: UserService = Depends(get_user_service)):
    """
    用户登录
    :param password: 用户的唯一用户名
    :param username: 用户的登录密码
    :param sys_service: 系统接口
    :param user_service: 用户接口
    :return: 用户登录信息
    """
    user_dto = await sys_service.login(username, password, user_service)
    return ApiResult.success(data=user_dto)


@sys_router.post(
    "/logout",
    summary="用户登出",
    description="用户登出",
    response_description="成功/失败",
)
async def logout(request: Request,
                 sys_service: SysService = Depends(get_sys_service)):
    """
    用户登出
    :param request:请求头
    :param sys_service: 系统接口
    :return: 成功/失败
    """
    authorization: str = request.headers.get("Authorization")
    result = await sys_service.logout(authorization)
    return ApiResult.success(data=result)

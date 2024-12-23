from fastapi import APIRouter, Query, Depends

from src.config.result.api_result import ApiResult
from src.dependencies.sys_dependencies import get_user_mapper
from src.mapper.user_mapper import UserMapper
from src.service.impl.user_service_impl import UserServiceImpl
from src.service.user_service import UserService

user_router = APIRouter(prefix="/user", tags=["用户管理"])


# 通过依赖注入返回服务实例
def get_user_service() -> UserService:
    return UserServiceImpl()


@user_router.post(
    "/insert",
    summary="创建用户",
    description="通过提供用户名、邮箱和是否激活状态，创建一个新的用户。",
    response_description="返回创建的用户信息。",
)
async def create_user(username: str = Query(None, description="用户的唯一用户名"),
                      email: str = Query(..., description="用户的邮箱地址"),
                      is_active: bool = Query(..., description="用户是否激活，默认为True"),
                      user_service: UserService = Depends(get_user_service)):
    user = await user_service.create_user(username=username, email=email, is_active=is_active)
    return ApiResult.success(data=user)


@user_router.get(
    "/list",
    summary="获取所有用户",
    description="返回系统中所有用户的详细信息。",
    response_description="返回用户列表。",
)
async def get_users(user_service: UserService = Depends(get_user_service)):
    users = await user_service.get_all_users()
    return ApiResult.success(data=users)


@user_router.get(
    "/get",
    summary="获取单个用户",
    description="通过用户 ID 获取用户的详细信息。如果用户不存在，返回 404 错误。",
    response_description="返回用户的详细信息。",
)
async def get_user(user_id: int = Query(..., description="用户id"),
                   user_service: UserService = Depends(get_user_service)):
    user = await user_service.get_user(user_id)
    return ApiResult.success(data=user)


@user_router.post(
    "/update",
    summary="更新用户信息",
    description="通过用户 ID 更新用户的部分或全部信息。",
    response_description="返回更新结果。",
)
async def update_user(user_id: int = Query(None, description="用户的唯一 ID"),
                      username: str = Query(None, description="用户名"),
                      email: str = Query(None, description="邮箱地址"),
                      is_active: bool = Query(None, description="激活状态"),
                      user_service: UserService = Depends(get_user_service)):
    user = await user_service.update_user(user_id, username, email, is_active)
    return ApiResult.success(data=user)


@user_router.post(
    "/delete",
    summary="删除用户",
    description="通过用户 ID 删除指定用户。如果用户不存在，返回 404 错误。",
    response_description="返回删除结果。",
)
async def delete_user(user_id: int = Query(None, description="用户的唯一 ID"),
                      user_service: UserService = Depends(get_user_service)):
    await user_service.delete_user(user_id)
    return ApiResult.success()


@user_router.get(
    "/get/department",
    summary="获取所属部门",
    response_description="返回用户所属部门。",
)
async def get_user_department(user_id: int = Query(..., description="用户id"),
                              user_service: UserService = Depends(get_user_service),
                              user_mapper: UserMapper = Depends(get_user_mapper)):
    user_department_dto = await user_service.get_user_department(user_id, user_mapper)
    return ApiResult.success(data=user_department_dto)

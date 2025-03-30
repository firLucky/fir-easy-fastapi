from fastapi import APIRouter, Query, Depends, Body

from src.config.result.api_result import ApiResult
from src.dependencies.sys_dependencies import get_user_mapper
from src.dto.common import StateDTOResponse
from src.dto.user import CreateUserDTO, UpdateUserDTO, deleteUserDTO, CreateUserResponseDTO, ListResponseDTO, \
    UserResponseDTO
from src.dto.user_department_dto import UserDepartmentDTOResponse
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
    response_model=CreateUserResponseDTO,
)
async def create_user(
        create_user_dto: CreateUserDTO = Body(description="创建用户"),
        user_service: UserService = Depends(get_user_service)):
    user = await user_service.create_user(create_user_dto=create_user_dto)
    return ApiResult.success(data=user)


@user_router.get(
    "/list",
    summary="获取所有用户",
    description="返回系统中所有用户的详细信息。",
    response_description="所有用户",
    response_model=ListResponseDTO,
)
async def get_users(user_service: UserService = Depends(get_user_service)):
    users = await user_service.get_all_users()
    return ApiResult.success(data=users)


@user_router.get(
    "/get",
    summary="获取单个用户",
    description="通过用户 ID 获取用户的详细信息。如果用户不存在，返回 404 错误。",
    response_description="返回用户的详细信息。",
    response_model=UserResponseDTO,
)
async def get_user(user_id: int = Query(..., description="用户id"),
                   user_service: UserService = Depends(get_user_service)):
    user = await user_service.get_user(user_id)
    return ApiResult.success(data=user)


@user_router.post(
    "/update",
    summary="更新用户信息",
    description="通过用户 ID 更新用户的部分或全部信息。",
    response_description="操作状态",
    response_model=StateDTOResponse,
)
async def update_user(
        update_user_dto: UpdateUserDTO = Body(description="更新用户"),
        user_service: UserService = Depends(get_user_service)):
    user = await user_service.update_user(update_user_dto)
    return ApiResult.success(data=user)


@user_router.post(
    "/delete",
    summary="删除用户",
    description="通过用户 ID 删除指定用户。如果用户不存在，返回 404 错误。",
    response_description="操作状态",
    response_model=StateDTOResponse,
)
async def delete_user(
        delete_user_dto: deleteUserDTO = Body(description="删除用户"),
        user_service: UserService = Depends(get_user_service)):
    await user_service.delete_user(delete_user_dto)
    return ApiResult.success()


@user_router.get(
    "/get/department",
    summary="获取所属部门",
    response_description="用户所属部门",
    response_model=UserDepartmentDTOResponse,
)
async def get_user_department(user_id: int = Query(..., description="用户id"),
                              user_service: UserService = Depends(get_user_service),
                              user_mapper: UserMapper = Depends(get_user_mapper)):
    user_department_dto = await user_service.get_user_department(user_id, user_mapper)
    return ApiResult.success(data=user_department_dto)

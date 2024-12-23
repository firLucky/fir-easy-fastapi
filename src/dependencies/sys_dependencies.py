from src.mapper.impl.user_mapper_impl import UseMapperImpl
from src.mapper.user_mapper import UserMapper


# 依赖注入函数，返回 UserMapper 的实现
def get_user_mapper() -> UserMapper:
    return UseMapperImpl()  # 返回 UserMapper 的实现

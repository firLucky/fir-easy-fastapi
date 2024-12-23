from tortoise import Tortoise
from src.dto.user_department_dto import UserDepartmentDTO
from src.mapper.user_mapper import UserMapper


class UseMapperImpl(UserMapper):
    """
    用户实现层
    """

    async def get_user_department(self, user_id: int) -> UserDepartmentDTO:
        """
        用户对象
        """
        # SQL 查询语句
        query = """
        SELECT
            u.id AS user_id,
            u.username,
            d.code AS department_code,
            d.name AS department_name
        FROM
            user u
        LEFT JOIN
            department d
        ON
            u.department_code = d.code
        WHERE
            u.id = %s
        """

        # 执行 SQL 查询并获取结果
        connection = Tortoise.get_connection("default")
        results = await connection.execute_query_dict(query, [user_id])
        user_department_data = None
        if results:
            # 将查询结果映射到 Pydantic 数据模型
            user_department_data = UserDepartmentDTO(**results[0])  # 只取第一个结果（假设每个用户名唯一）
        return user_department_data

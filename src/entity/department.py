from tortoise import fields
from tortoise.models import Model


class Department(Model):
    id = fields.IntField(pk=True)  # 主键
    name = fields.CharField(max_length=100, unique=True)  # 部门名称
    code = fields.CharField(max_length=50, unique=True)  # 部门编号
    description = fields.TextField(null=True)  # 部门描述
    created_at = fields.DatetimeField(auto_now_add=True)  # 创建时间
    updated_at = fields.DatetimeField(auto_now=True)  # 更新时间

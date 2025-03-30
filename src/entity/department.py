from tortoise import fields
from tortoise.models import Model


class Department(Model):
    """
    部门表
    """
    id = fields.IntField(pk=True, description='逐渐编号')
    name = fields.CharField(max_length=100, unique=True, null=True, description='部门名称')
    code = fields.CharField(max_length=50, unique=True, null=True, description='部门编号')
    description = fields.TextField(null=True, description='部门描述')
    created_at = fields.DatetimeField(auto_now_add=True, null=True, description='创建时间')
    updated_at = fields.DatetimeField(auto_now=True, null=True, description='更新时间')

    class Meta:
        table = "department"
        table_description = "部门表"

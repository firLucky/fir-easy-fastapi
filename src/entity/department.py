from tortoise import fields
from tortoise.models import Model


class Department(Model):
    """
    部门表
    """
    id = fields.IntField(pk=True, description='主键编号')
    name = fields.CharField(max_length=100, unique=True, null=True, description='部门名称')
    code = fields.IntField(description='部门编号')

    class Meta:
        table = "department"
        table_description = "部门表"

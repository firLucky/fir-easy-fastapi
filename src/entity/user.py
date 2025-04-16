from tortoise import fields
from tortoise.models import Model


class User(Model):
    """
    用户表
    """
    id = fields.IntField(pk=True, description='主键编号')
    username = fields.CharField(max_length=50, null=True, description='用户登录名')
    password = fields.CharField(max_length=50, null=True, description='用户密码')
    dept_code = fields.IntField(description='部门编号')

    class Meta:
        table = "user"
        table_description = "用户表"

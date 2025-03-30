from enum import Enum


class ApiCodeCustomEnum(Enum):
    def __init__(self, code: int, description: str):
        self._value_ = code
        self.description = description

    def __str__(self):
        return f"{self.__class__.__name__}.{self.name}: (Code: {self.value}, Description: {self.description})"

    @property
    def code(self):
        return self._value_


class ApiCode(ApiCodeCustomEnum):
    """
    接口返回码
    INVALID：无效参数
    """
    ACCESS_DENIED = (401, "登录过期!")
    ERROR_USER_PASS = (400, "用户名或密码错误!")
    ERROR_PARAMETER_MISS = (400, "参数缺失!")

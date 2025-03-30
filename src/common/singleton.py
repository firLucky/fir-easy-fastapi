import os
from urllib.parse import quote_plus


class Singleton:
    """
    单例模式全局变量
    """
    _instance = None

    # 数据库登录地址
    database_url = None
    # 数据库登录用户名
    database_user = None
    # 数据库登录密码
    database_password = None
    # 令牌秘钥
    jwt_secret = None
    # 令牌加密算法
    jwt_algorithm = None
    # 令牌过期时间
    jwt_expiration = None
    # 令牌前缀
    jwt_token_head = None
    # 是否开启拦截器
    jwt_filter = None
    # 接口白名单
    server_white_url_list = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            # 初次加载时，初始化全局变量
            database_url = os.environ.get('DATABASE_URL')
            database_user = os.environ.get('DATABASE_USER')
            database_password = os.environ.get('DATABASE_PASSWORD')
            # 转义密码中的特殊字符
            quoted_user = quote_plus(database_user)
            quoted_password = quote_plus(database_password)
            cls._instance.quoted_user = quoted_user
            cls._instance.quoted_password = quoted_password
            cls._instance.database_url = database_url

            jwt_secret = os.environ.get('JWT_SECRET')
            jwt_algorithm = os.environ.get('JWT_ALGORITHM')
            cls._instance.jwt_secret = jwt_secret
            cls._instance.jwt_algorithm = jwt_algorithm
            jwt_expiration = os.environ.get('JWT_EXPIRATION')
            jwt_expiration = int(jwt_expiration)
            jwt_token_head = os.environ.get('JWT_TOKEN_HEAD')
            cls._instance.jwt_expiration = jwt_expiration
            cls._instance.jwt_token_head = jwt_token_head
            jwt_filter = os.getenv('JWT_FILTER', 'false').lower() == 'true'
            cls._instance.jwt_filter = jwt_filter

            server_white_url = os.getenv('SERVER.WHITE.URL', '')
            # 将字符串转换为列表
            server_white_url_list = eval(server_white_url)
            cls._instance.server_white_url_list = server_white_url_list

        return cls._instance

    @classmethod
    def set_database_url(cls, value):
        cls._instance.database_url = value

    @classmethod
    def get_database_url(cls):
        return cls._instance.database_url

    @classmethod
    def set_database_user(cls, value):
        cls._instance.database_user = value

    @classmethod
    def get_database_user(cls):
        return cls._instance.database_user

    @classmethod
    def set_database_password(cls, value):
        cls._instance.database_password = value

    @classmethod
    def get_database_password(cls):
        return cls._instance.database_password

    @classmethod
    def set_jwt_secret(cls, value):
        cls._instance.jwt_secret = value

    @classmethod
    def get_jwt_secret(cls):
        return cls._instance.jwt_secret

    @classmethod
    def set_jwt_algorithm(cls, value):
        cls._instance.jwt_algorithm = value

    @classmethod
    def get_jwt_algorithm(cls):
        return cls._instance.jwt_algorithm

    @classmethod
    def set_jwt_expiration(cls, value):
        cls._instance.jwt_expiration = value

    @classmethod
    def get_jwt_expiration(cls):
        return cls._instance.jwt_expiration

    @classmethod
    def set_jwt_token_head(cls, value):
        cls._instance.jwt_token_head = value

    @classmethod
    def get_jwt_token_head(cls):
        return cls._instance.jwt_token_head

    @classmethod
    def set_jwt_filter(cls, value):
        cls._instance.jwt_filter = value

    @classmethod
    def get_jwt_filter(cls):
        return cls._instance.jwt_filter

    @classmethod
    def set_server_white_url_list(cls, value):
        cls._instance.server_white_url_list = value

    @classmethod
    def get_server_white_url_list(cls):
        return cls._instance.server_white_url_list

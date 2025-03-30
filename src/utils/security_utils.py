from datetime import datetime, timedelta
from typing import Any, Union
from jose import jwt

from src.common.singleton import Singleton


def create_access_token(
        uid: Union[str, Any], uname: Union[str, Any], expires_delta: timedelta = None
) -> str:
    """
    生成token
    :param uid: 用户id
    :param uname: 用户名
    :param expires_delta: 过期时间
    :return: 令牌
    """

    singleton = Singleton()
    jwt_secret = singleton.get_jwt_secret()
    jwt_algorithm = singleton.get_jwt_algorithm()
    jwt_expiration = singleton.get_jwt_expiration()
    jwt_token_head = singleton.get_jwt_token_head()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            seconds=jwt_expiration
        )
    to_encode = {"exp": expire, "uid": str(uid), "uname": str(uname)}

    encoded_jwt = jwt.encode(to_encode, jwt_secret, algorithm=jwt_algorithm)
    encoded_jwt = jwt_token_head + encoded_jwt
    return encoded_jwt


def parse_jwt_token(token: str) -> Union[str, Any]:
    """
    解析token
    :param token:
    :return:
    """
    singleton = Singleton()
    jwt_secret = singleton.get_jwt_secret()
    jwt_algorithm = singleton.get_jwt_algorithm()
    payload = jwt.decode(token, jwt_secret, algorithms=[jwt_algorithm])
    return payload

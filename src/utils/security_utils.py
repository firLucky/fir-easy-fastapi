import os
from datetime import datetime, timedelta
from typing import Any, Union
from jose import jwt


def create_access_token(
        uid: Union[str, Any], uname: Union[str, Any], expires_delta: timedelta = None
) -> str:
    jwt_secret = os.environ.get('JWT_SECRET')
    jwt_algorithm = os.environ.get('JWT_ALGORITHM')
    jwt_expiration = os.environ.get('JWT_EXPIRATION')
    jwt_expiration = int(jwt_expiration)
    jwt_token_head = os.environ.get('JWT_TOKEN_HEAD')

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
    jwt_secret = os.environ.get('JWT_SECRET')
    jwt_algorithm = os.environ.get('JWT_ALGORITHM')
    payload = jwt.decode(token, jwt_secret, algorithms=[jwt_algorithm])
    return payload

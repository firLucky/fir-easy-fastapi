from fastapi import status
from fastapi.responses import JSONResponse, Response
from typing import Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from tortoise.models import Model


class ApiResult:
    """统一异常返回类"""

    @classmethod
    def success(cls, data: Union[list, dict, str, bool, Model, BaseModel] = None) -> Response:
        """
        通用-请求成功
        :param data:
        :return:
        """
        json_compatible_item_data = jsonable_encoder(data)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'code': 200,
                'message': "请求成功",
                'data': json_compatible_item_data,
            }
        )

    @classmethod
    def fail(cls, code: int = 400,
             message: str = "请求失败",
             data: Union[list, dict, str, Model, BaseModel] = None,
             ) -> Response:
        """
        通用-失败请求返回体
        :param code: 状态码
        :param message: 描述
        :param data: 请求数据
        :return:
        """
        json_compatible_item_data = jsonable_encoder(data)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'code': code,
                'message': message,
                'data': json_compatible_item_data,
            }
        )

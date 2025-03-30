from pydantic import BaseModel, Field


class PageInfo(BaseModel):
    """
    分页对象
    PageInfo:
        data (List[T]): 数据内容
        total (int): 总数
        pages (int): 当前页码
        size (int): 每页记录数
    """
    total: int = Field(description="总数")
    pages: int = Field(description="当前页码")
    size: int = Field(description="每页记录数")
    data: list = Field(description="数据内容")

class StateDTOResponse(BaseModel):
    """
    请求状态信息
    """
    code: int = Field(description="状态码")
    message: str = Field(description="描述信息")
    data: bool = Field(description="成功(True)/失败(False)")
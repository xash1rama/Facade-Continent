from pydantic import BaseModel
from typing import List


class GetString(BaseModel):
    name: str
    measure: str
    price: int


class GetTable(BaseModel):
    table: List[GetString]


class NewData(BaseModel):
    name: str
    data: str


class Datas(NewData):
    id: int


class DeleteData(BaseModel):
    id: int


class UpdateFacade(BaseModel):
    name: str
    measure: str
    price: int
    id: int


class User(BaseModel):
    user_id: str


# Pydantic модели для ответа
class PortfolioResponse(BaseModel):
    id: int
    title: str
    description: str
    main: str


class PhotoResponse(BaseModel):
    filename: str


class PortfolioUpdate(BaseModel):
    title: str
    description: str




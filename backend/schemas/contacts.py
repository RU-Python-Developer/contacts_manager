from pydantic import BaseModel


class ContactCreate(BaseModel):
    """Схема данных создания записи"""

    name: str
    description: str


class OutContact(BaseModel):
    """Схема возвращаемых данных"""

    id: int


class ContactUpdate(BaseModel):
    """Схема данных обновления записи"""

    id: int
    name: str
    description: str

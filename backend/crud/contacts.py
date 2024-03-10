from sqlalchemy import select
from datetime import date, datetime

from models.database import database
from models.contacts import contacts_table as table
from schemas import contacts

async def create_contact(data: contacts.ContactCreate, date: datetime):
    """Добавление записи в БД"""
    query = table.insert().values(name=data.name, description=data.description, created_at=date).returning(table.c.id)
    return await database.execute(query)

async def update_contact(data: contacts.ContactUpdate, date: datetime):
    """Обновление записи в БД"""
    query = table.update().where(table.c.id==data.id).values(name=data.name, description=data.description, updated_at=date).returning(table.c.id)
    return await database.execute(query)

async def get_contacts():
    """Получение записей из БД"""
    query = table.select()
    return await database.fetch_all(query)

async def delete_contact(id: int):
    """Удаление записи из БД"""
    query = table.delete().where(table.c.id==id).returning(table.c.id)
    return await database.execute(query)

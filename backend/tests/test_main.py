import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from main import app
from models import database


client = TestClient(app)

def set_data(query):
    database.extension_query(query=query)

def test_read_main():
    """Тестирование отображения главной страницы"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

@pytest.mark.asyncio
async def test_create_contact(temp_db_async):
    """Тестирование добавления записи"""
    async with AsyncClient(app=app, base_url="http://test") as async_client:
        response = await async_client.post("/contact/create", json={"name": "Igor", "description": "Good boy"})
        assert response.status_code == 200
        assert response.json() == {'id': 1}

@pytest.mark.asyncio
async def test_get_contacts(temp_db_async):
    """Тестирование получения всех записей"""
    set_data('INSERT INTO "Contact" (name, description, created_at) VALUES (\'Ivan\', \'My friend\', \'2024-03-10 11:09:32.219736\');')
    async with AsyncClient(app=app, base_url="http://test") as async_client:
        response = await async_client.get("/contacts")
        assert response.status_code == 200
        assert response.json() == [{'id': 1, 'name': 'Ivan', 'description': 'My friend', 'created_at': '2024-03-10T11:09:32.219736', 'updated_at': None}]

@pytest.mark.asyncio
async def test_update_contact(temp_db_async):
    """Тестирование обновления записи"""
    set_data('INSERT INTO "Contact" (name, description, created_at) VALUES (\'Ivan\', \'My friend\', \'2024-03-10 11:09:32.219736\');')
    async with AsyncClient(app=app, base_url="http://test") as async_client:
        response = await async_client.put("/contact/update", json={"id": 1, "name": "Igor", "description": "Very good boy"})
        assert response.status_code == 200
        assert response.json() == {'id': 1}
        
        response = await async_client.get("/contacts")
        assert response.status_code == 200
        assert response.json()[0]['updated_at'] and isinstance(response.json()[0]['updated_at'], str)

@pytest.mark.asyncio
async def test_delete_contact(temp_db_async):
    """Тестирование удаления записи"""
    for name in ['Ivan', 'Igor']:
        set_data(f'INSERT INTO "Contact" (name, description, created_at) VALUES (\'{name}\', \'My friend\', \'2024-03-10 11:09:32.219736\');')
    async with AsyncClient(app=app, base_url="http://test") as async_client:
        response = await async_client.get("/contacts")
        assert response.status_code == 200
        assert len(response.json()) == 2 and response.json()[0]['id'] == 1
        
        response = await async_client.delete("/contact/delete/1")
        assert response.status_code == 200
        assert response.json() == {'id': 1}

        response = await async_client.get("/contacts")
        assert response.status_code == 200
        assert len(response.json()) == 1 and response.json()[0]['id'] == 2
        
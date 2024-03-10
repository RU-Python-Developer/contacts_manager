from datetime import datetime
from fastapi import APIRouter, HTTPException

from crud import contacts as crud
from schemas import contacts

router = APIRouter()

@router.post("/contact/create", response_model=contacts.OutContact)
async def create_contact(contact: contacts.ContactCreate):
    """Эндпоинт создания контакта"""
    create_id = await crud.create_contact(data=contact, date=datetime.now())
    if create_id:
        return {'id': create_id}
    else:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error",
        )
    

@router.put("/contact/update", response_model=contacts.OutContact)
async def update_contact(contact: contacts.ContactUpdate):
    """Эндпоинт обновления контакта"""
    update_id = await crud.update_contact(data=contact, date=datetime.now())
    if update_id:
        return {'id': update_id}
    else:
        raise HTTPException(
            status_code=404,
            detail="Contact does not exist",
        )

@router.get("/contacts")
async def get_contacts():
    """Эндпоинт получения контактов"""
    contacts = await crud.get_contacts()
    if contacts:
        return contacts
    else:
        raise HTTPException(
            status_code=404,
            detail="Contacts does not exist",
        )

@router.delete("/contact/delete/{contactId}", response_model=contacts.OutContact)
async def delete_contact(contactId: str):
    """Эндпоинт удаления контакта"""
    delete_id = await crud.delete_contact(id=int(contactId))
    if delete_id:
        return {'id': delete_id}
    else:
        raise HTTPException(
            status_code=404,
            detail="Contact does not exist",
        )

@router.get("/")
async def read_main():
    return {"msg": "Hello World"}
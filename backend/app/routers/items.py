from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.crud.item import create_item, get_items, delete_item
from app.crud.item import update_item
from app.schemas.item import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["Items"])


@router.post("/", response_model=ItemResponse)
def add_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)


@router.get("/", response_model=list[ItemResponse])
def all_items(db: Session = Depends(get_db)):
    return get_items(db)

@router.put("/{item_id}", response_model=ItemResponse)
def edit_item(item_id: UUID, item: ItemCreate, db: Session = Depends(get_db)):
    updated = update_item(db, item_id, item)

    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")

    return updated

@router.delete("/{item_id}")
def remove_item(item_id: UUID, db: Session = Depends(get_db)):
    item = delete_item(db, item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"message": "Item deleted"}

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.crud.item import create_item, get_items
from app.schemas.item import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["Items"])


@router.post("/", response_model=ItemResponse)
def add_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)


@router.get("/", response_model=list[ItemResponse])
def all_items(db: Session = Depends(get_db)):
    return get_items(db)

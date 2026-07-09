from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.item import ItemCreate


def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session):
    return db.query(Item).all()


def get_item(db: Session, item_id):
    return db.query(Item).filter(Item.id == item_id).first()


def delete_item(db: Session, item_id):
    item = get_item(db, item_id)

    if item:
        db.delete(item)
        db.commit()

    return item

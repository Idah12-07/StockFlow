from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.item import ItemCreate


def create_item(db, item):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db):
    return db.query(Item).all()


def get_item(db, item_id):
    return db.query(Item).filter(Item.id == item_id).first()


def update_item(db, item_id, updated):
    item = get_item(db, item_id)

    if not item:
        return None

    for key, value in updated.model_dump().items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)

    return item


def delete_item(db, item_id):
    item = get_item(db, item_id)

    if item:
        db.delete(item)
        db.commit()

    return item

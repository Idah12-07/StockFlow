from pydantic import BaseModel


class ItemCreate(BaseModel):
    item_code: str
    item_name: str
    category: str
    unit: str
    minimum_stock: int
    current_balance: int


class ItemResponse(ItemCreate):
    class Config:
        from_attributes = True

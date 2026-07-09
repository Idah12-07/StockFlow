import uuid

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    item_name = Column(String, nullable=False)

    category = Column(String, nullable=False)

    unit = Column(String, nullable=False)

    minimum_stock = Column(Integer, default=0)

    current_balance = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

from fastapi import FastAPI

from app.database.database import Base, engine
from app.routers.items import router as items_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="StockFlow API")

app.include_router(items_router)


@app.get("/")
def root():
    return {"message": "Welcome to StockFlow API 🚀"}

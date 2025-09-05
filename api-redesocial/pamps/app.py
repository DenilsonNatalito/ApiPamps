from fastapi import FastAPI
from .routes import main_router

app = FastAPI(
    title ="PAMPS API",
    description="PAMPS API for managing and processing data And...",
    version="1.0.0",
)

@app.get("/")
async def index():
    return {"Hello": "Welcome to the PAMPS API!"}

app.include_router(main_router)
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Smart Money Tracker")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API is running"}

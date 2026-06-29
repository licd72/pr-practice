from fastapi import FastAPI
from user_api import router as user_router

app = FastAPI(title="Hello API")

app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health():
    return {"status": "ok"}

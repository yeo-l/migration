from fastapi import FastAPI

from src.routers.authentication import router
from src.routers.user import user

app = FastAPI()

app.include_router(router)
app.include_router(user)

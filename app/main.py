from fastapi import FastAPI
from routes.routes import api_router
from contextlib import asynccontextmanager
from db.init_db import init_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_database()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8001)

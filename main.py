from fastapi import FastAPI, APIRouter
import uvicorn

service = FastAPI()
routers = APIRouter()


@routers.get("/health")
async def health_router() -> dict:
    return {"status": "ok", "version": "1.0.0"}


@routers.get("/hello")
async def hello_router() -> dict:
    return {"message": "Hello World"}


@routers.get("/help")
async def help_router() -> dict:
    return {"message": "I help you"}


service.include_router(routers)

uvicorn.run(service)

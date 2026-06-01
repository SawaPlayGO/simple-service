from fastapi import FastAPI, APIRouter
import uvicorn

service = FastAPI()
routers = APIRouter()

@routers.get("/health")
async def get_health_router() -> dict:
    return {"status": "ok", "version": "1.0.0"}

@routers.get("/hello")
async def get_hello_router() -> dict:
    return {"message": "Hello World"}


service.include_router(routers)

uvicorn.run(service)
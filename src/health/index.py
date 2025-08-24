from fastapi import APIRouter
from lib.redis.index import ping as redis_ping

router = APIRouter()

@router.get("/live")
async def live():
    return {"live": True}

@router.get("/ready")
async def ready():
    return {"ready": True}

@router.get("/deep")
async def deep():
    return {"redis": await redis_ping()}

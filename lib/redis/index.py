import os
import redis.asyncio as redis

def _build_redis_url() -> str:
    dsn = os.getenv("REDIS_URL", "").strip()
    if dsn:
        return dsn
    host = os.getenv("REDIS_HOST", "redis")
    port = os.getenv("REDIS_PORT", "6379")
    db   = os.getenv("REDIS_DB", "0")
    return f"redis://{host}:{port}/{db}"

REDIS_URL = _build_redis_url()
_client: redis.Redis | None = None

async def get_client() -> redis.Redis:
    global _client
    if _client is None:
        _client = redis.from_url(REDIS_URL, decode_responses=True)
    return _client

async def ping() -> bool:
    r = await get_client()
    try:
        return await r.ping()
    except Exception:
        return False

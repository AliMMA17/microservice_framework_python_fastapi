from fastapi import FastAPI
from src.health.index import router as health_router
from src.test.index import router as test_router

app = FastAPI(title="Your Service", version="1.0.0")

# Main API routes
app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(test_router,   prefix="/test",   tags=["test"])

@app.get("/", tags=["root"])
async def root():
    return {"name": "your-service", "ok": True}

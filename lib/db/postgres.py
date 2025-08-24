import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncIterator

def _build_async_dsn() -> str:
    dsn = os.getenv("DATABASE_URL", "").strip()
    if dsn:
        return dsn
    user = os.getenv("POSTGRES_USER", "postgres")
    pwd  = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "db")
    port = "5432"
    db   = os.getenv("POSTGRES_DB", "postgres")
    return f"postgresql+asyncpg://{user}:{pwd}@{host}:{port}/{db}"

DATABASE_URL = _build_async_dsn()

class Base(DeclarativeBase):
    pass

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as session:
        yield session

# No-op: rely on Alembic only
async def init_db() -> None:
    return None

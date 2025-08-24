from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from lib.db.postgres import get_session
from .basemodels import TestCreate, TestRead
from .module import create_test, list_tests

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"pong": True}

@router.get("/items", response_model=list[TestRead])
async def get_items(session: AsyncSession = Depends(get_session)):
    return await list_tests(session)

@router.post("/items", response_model=TestRead, status_code=status.HTTP_201_CREATED)
async def post_item(payload: TestCreate, session: AsyncSession = Depends(get_session)):
    return await create_test(session, payload)

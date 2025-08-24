from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import TestItem
from .basemodels import TestCreate

async def create_test(session: AsyncSession, data: TestCreate) -> TestItem:
    item = TestItem(full_name=data.full_name, note=data.note)
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item

async def list_tests(session: AsyncSession) -> list[TestItem]:
    res = await session.execute(select(TestItem).order_by(TestItem.id))
    return list(res.scalars().all())

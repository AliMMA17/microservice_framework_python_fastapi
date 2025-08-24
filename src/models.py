from datetime import datetime
from sqlalchemy import String, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from lib.db.postgres import Base

class TestItem(Base):
    __tablename__ = "test_items"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)  # renamed
    note: Mapped[str | None] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)

class TestAccount(Base):
    __tablename__ = "test_accounts"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    account_name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    note: Mapped[str | None] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
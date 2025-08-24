from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class TestCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    note: Optional[str] = None

class TestRead(BaseModel):
    id: int
    name: str
    note: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}

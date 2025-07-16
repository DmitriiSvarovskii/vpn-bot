from pydantic import BaseModel, ConfigDict
from typing import Optional


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    telegram_id: int
    source: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None


class UserCreate(UserBase):
    pass

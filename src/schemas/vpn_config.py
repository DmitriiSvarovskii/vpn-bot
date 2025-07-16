import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional


class VPNConfigBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    uuid: str
    flow: str
    email: Optional[str | None]
    expires_at: Optional[datetime.date | None]


class VPNConfigCreate(VPNConfigBase):
    pass

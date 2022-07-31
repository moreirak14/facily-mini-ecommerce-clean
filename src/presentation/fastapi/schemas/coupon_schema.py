from pydantic import BaseModel
from datetime import datetime


class CreateCouponSchema(BaseModel):
    code: str
    expire_at: datetime
    limit: int
    type: str
    value: float

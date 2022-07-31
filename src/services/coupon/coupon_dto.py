from dataclasses import dataclass
from datetime import datetime


@dataclass
class CouponDTO:
    code: str
    expire_at: datetime
    limit: int
    type: str
    value: float

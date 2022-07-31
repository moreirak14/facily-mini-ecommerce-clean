from datetime import datetime, date
from src.domain.exceptions import ValidateDatetimeCoupon


class Coupon:
    def __init__(
        self, code: str, expire_at: datetime, limit: int, type: str, value: float
    ) -> None:
        self.code = code
        self.expire_at = expire_at
        self.limit = limit
        self.type = type
        self.value = value

    def validate_date(self):
        if datetime.utcnow() > self.expire_at:
            raise ValidateDatetimeCoupon("Data de expiração invalida")

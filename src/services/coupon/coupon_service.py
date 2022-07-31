from src.services.coupon.coupon_dto import CouponDTO
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.domain.coupon.model import Coupon
from src.services.exceptions import InvalidCode


def create_coupon(coupon_dto: CouponDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        coupon = uow.coupon_repository.get(code=coupon_dto.code)
        if coupon:
            raise InvalidCode("Codigo de cupom invalido!")

        coupon = Coupon(
            code=coupon_dto.code,
            expire_at=coupon_dto.expire_at,
            limit=coupon_dto.limit,
            type=coupon_dto.type,
            value=coupon_dto.value,
        )
        coupon.validate_date()
        uow.coupon_repository.add(coupon)
        uow.commit()

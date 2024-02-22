from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.types import PositiveInt

from app.constants import INVESTED_AM_DEF


class DonationSchema(BaseModel):
    comment: Optional[str]
    full_amount: Optional[PositiveInt]


class DonationCreate(DonationSchema):
    full_amount: PositiveInt


class DonationDB(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationSuperUserDB(DonationDB):
    user_id: int
    invested_amount: Optional[int] = INVESTED_AM_DEF
    close_date: Optional[datetime]
    fully_invested: Optional[bool] = False

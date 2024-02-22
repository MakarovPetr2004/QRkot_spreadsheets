from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, Extra, validator
from pydantic.types import PositiveInt

from app.constants import MAX_NAME_CHARITY, MIN_NAME_CHARITY, INVESTED_AM_DEF


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, min_length=MIN_NAME_CHARITY,
                                max_length=MAX_NAME_CHARITY)
    description: Optional[str]
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid

    @validator('name', 'description')
    def strip_whitespace(cls, value):
        if isinstance(value, str) and not value.strip():
            raise ValueError("Поле не может быть пустым!")
        return value


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., min_length=MIN_NAME_CHARITY,
                      max_length=MAX_NAME_CHARITY)
    description: str
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectCreate):
    id: int
    create_date: datetime
    invested_amount: int = INVESTED_AM_DEF
    close_date: Optional[datetime]
    fully_invested: bool = False

    @validator('name', 'description', pre=False)
    def strip_whitespace(cls, value):
        return value

    class Config:
        orm_mode = True

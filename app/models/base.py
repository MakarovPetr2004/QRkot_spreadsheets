from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Boolean

from app.core.db import Base


class CharityDonationBase(Base):
    __abstract__ = True

    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)
    full_amount = Column(Integer, nullable=False)
    fully_invested = Column(Boolean, default=False)
    invested_amount = Column(Integer, default=0)

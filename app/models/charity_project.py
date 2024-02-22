from sqlalchemy import Column, String

from app.constants import MAX_NAME_CHARITY
from app.models.base import CharityDonationBase


class CharityProject(CharityDonationBase):
    name = Column(String(MAX_NAME_CHARITY), nullable=False, unique=True)
    description = Column(String, nullable=False)

from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.base import CharityDonationBase


class Donation(CharityDonationBase):
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comment = Column(String)

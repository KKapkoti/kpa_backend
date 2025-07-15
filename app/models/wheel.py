# app/models/wheel.py

from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    wheel_number = Column(String, nullable=False)
    diameter = Column(Float, nullable=False)
    flange_thickness = Column(Float, nullable=False)
    tread_wear = Column(Float, nullable=False)

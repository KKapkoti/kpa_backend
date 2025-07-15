# app/schemas/wheel.py
from pydantic import BaseModel, ConfigDict

class WheelSpecBase(BaseModel):
    wheel_number: str
    diameter: float
    flange_thickness: float
    tread_wear: float

class WheelSpecCreate(WheelSpecBase):
    pass

class WheelSpecResponse(WheelSpecBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

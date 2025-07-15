# app/routes/wheel_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.wheel import WheelSpecification
from app.schemas.wheel import WheelSpecCreate, WheelSpecResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/forms/wheel-specifications", response_model=WheelSpecResponse)
def create_wheel_spec(data: WheelSpecCreate, db: Session = Depends(get_db)):
    new_spec = WheelSpecification(**data.dict())
    db.add(new_spec)
    db.commit()
    db.refresh(new_spec)
    return new_spec

from typing import List

@router.get("/api/forms/wheel-specifications", response_model=List[WheelSpecResponse])
def get_all_wheel(db: Session = Depends(get_db)):
    return db.query(WheelSpecification).all()

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("")
async def list_users(db: Session = Depends(get_db)):
    # Placeholder for user listing
    return {"message": "User listing scaffold"}

@router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    # Placeholder for user retrieval
    return {"user_id": user_id, "message": "User retrieval scaffold"}

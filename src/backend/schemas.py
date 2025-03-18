from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    birth_date: str  # Формат YYYY-MM-DD


class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True

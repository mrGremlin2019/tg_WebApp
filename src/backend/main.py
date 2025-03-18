from fastapi import FastAPI, HTTPException, Depends
from datetime import datetime
from sqlalchemy.orm import Session
from src.database.db_client import DatabaseClient
from src.database.models import User
from src.backend.schemas import UserCreate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
db_client = DatabaseClient()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:9000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = DatabaseClient()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/{telegram_id}")
def save_user(telegram_id: int, user: UserCreate, db: Session = Depends(get_db)):
    birth_date = user.birth_date
    try:
        datetime.strptime(birth_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Неверный формат даты.")

    db_user = User(
        telegram_id=telegram_id,
        username=user.username,
        birth_date=birth_date
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"status": "ok", "message": "Данные сохранены!", "user_id": db_user.id}

@app.get("/user/{telegram_id}")
def get_user(telegram_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден!")

    birth_date = datetime.strptime(user.birth_date, "%Y-%m-%d").replace(year=datetime.now().year)
    now = datetime.now()
    if birth_date < now:
        birth_date = birth_date.replace(year=now.year + 1)
    time_left = birth_date - now

    return {
        "username": user.username,
        "birth_date": user.birth_date,
        "time_left": str(time_left)
    }

@app.get("/share/{user_id}")
def share_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден!")

    birth_date = datetime.strptime(user.birth_date, "%Y-%m-%d").replace(year=datetime.now().year)
    now = datetime.now()
    if birth_date < now:
        birth_date = birth_date.replace(year=now.year + 1)
    time_left = birth_date - now

    return {
        "username": user.username,
        "birth_date": user.birth_date,
        "time_left": str(time_left)
    }
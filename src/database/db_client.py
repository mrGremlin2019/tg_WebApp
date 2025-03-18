import logging
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base, User
from src.backend.schemas import UserCreate


class DatabaseClient:
    def __init__(self):
        load_dotenv()
        self._logger = logging.getLogger(__name__)

        self.db_url = os.getenv("DB_URL").strip()
        if not self.db_url:
            raise ValueError("Переменная окружения DB_URL не найдена в .env файле")
        print("DB_URL:", self.db_url)
        self.engine = create_engine(self.db_url, echo=True)
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

        # Создаём таблицы в БД
        Base.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        """Метод для работы с сессией"""
        with self.SessionLocal() as session:
            try:
                yield session
                session.commit()
            except Exception:
                session.rollback()
                raise
            finally:
                session.close()

    def create_user(self, user_data: UserCreate):
        """Создаёт нового пользователя в БД"""
        with self.get_session() as db:
            db_user = User(
                telegram_id=user_data.telegram_id,
                username=user_data.username,
                birth_date=user_data.birth_date
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user

    def get_user_by_telegram_id(self, telegram_id: int):
        """Получает пользователя по Telegram ID"""
        with self.get_session() as db:
            return db.query(User).filter(User.telegram_id == telegram_id).first()

    def delete_user(self, telegram_id: int):
        """Удаляет пользователя по Telegram ID"""
        with self.get_session() as db:
            user = db.query(User).filter(User.telegram_id == telegram_id).first()
            if user:
                db.delete(user)
                db.commit()
                return True
            return False

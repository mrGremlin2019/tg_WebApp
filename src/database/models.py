from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer

class Base(DeclarativeBase):  # Базовая модель SQLAlchemy
    pass

class User(Base):  # Модель пользователя
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, index=True)
    birth_date: Mapped[str] = mapped_column(String)  # Храним дату рождения в формате "YYYY-MM-DD"
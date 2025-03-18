from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()  # Создаём роутер

@router.message(F.text.lower() == "/start")  # Новый способ фильтрации
async def start(message: types.Message):
    user_id = message.from_user.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Перейти в WebApp", url=f"https://abcd1234.ngrok.io?user_id={user_id}")]
    ])
    await message.answer("Привет! Нажми кнопку ниже, чтобы ввести дату рождения.", reply_markup=keyboard)


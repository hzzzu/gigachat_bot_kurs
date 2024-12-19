from aiogram import Bot, Dispatcher, types
from keyboards.main_menu import main_menu


async def start_command(message: types.Message):
    await message.answer(
        "Привет! Я бот для работы с GigaChat API. Выберите действие в меню ниже.",
        reply_markup=main_menu
    )

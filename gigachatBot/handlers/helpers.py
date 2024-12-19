# helpers.py
from aiogram import types


async def help_command(message: types.Message):
    await message.answer(
        "Я могу выполнить следующие действия:\n"
        "1. Классификация текста.\n"
        "2. Обобщение текста.\n"
        "3. Анализ текста.\n"
        "4. Логическое рассуждение по тексту.\n\n"
        "Выберите действие в меню и отправьте текст для обработки."
    )

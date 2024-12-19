# Главное меню
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_factory.callback_factory import RoleCallbackFactory


# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Роль")],
        [KeyboardButton(text="Классификация")],
        [KeyboardButton(text="Обобщение")],
        [KeyboardButton(text="Анализ")],
        [KeyboardButton(text="Логическое рассуждение")],
        [KeyboardButton(text="Оплатить")],
        [KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True
)

role_kb_builder = InlineKeyboardBuilder()
role_kb_builder.row(
    InlineKeyboardButton(
        text="Ребёнок",
        callback_data=RoleCallbackFactory(role_code=1).pack()
    ),
    InlineKeyboardButton(
        text="Инженер",
        callback_data=RoleCallbackFactory(role_code=2).pack()
    ),
    InlineKeyboardButton(
        text="Профессор",
        callback_data=RoleCallbackFactory(role_code=3).pack()
    ),
    width=3
)
role_kb = role_kb_builder.as_markup()

from aiogram.filters.callback_data import CallbackData

# Фабрика коллбэков для кнопок
class TaskCallback(CallbackData, prefix="task"):
    action: str  # Поле для хранения действия

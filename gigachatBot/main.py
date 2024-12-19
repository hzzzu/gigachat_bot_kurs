import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.storage.memory import MemoryStorage
from utils.gigachat_api import GigaChatAPI
from handlers.payment import router as payment_router
from handlers.helpers import help_command
from handlers.menu import handle_main_menu, process_classification, process_summarization, process_analysis, process_reasoning
from handlers.start import start_command
from handlers.payment import send_invoice
from states.states import MainStates
from utils.constants import ADMIN_ID
from config import GIGACHAT_API_KEY, stats

# Логирование
logging.basicConfig(level=logging.INFO)

# Конфигурация бота
API_TOKEN = "7310283972:AAGGFdNcWefOwUiEkj9YYEw8eeKERuQdRqU"

# Инициализация бота, хранилища состояний и API GigaChat
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
gigachat = GigaChatAPI(api_key=GIGACHAT_API_KEY)

# Обработчик админ-панели
async def admin_panel_command(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("У вас нет доступа к этой команде.")
        return

    stats_message = "Статистика запросов:\n" + "\n".join(
        f"{key.capitalize()}: {value}" for key, value in stats.items()
    )
    await message.answer(f"Добро пожаловать в админ-панель!\n\n{stats_message}")

# Регистрация команд
dp.message.register(start_command, Command(commands=["start"]))
dp.message.register(help_command, Command(commands=["help"]))
dp.message.register(admin_panel_command, Command(commands=["admin"]))

# Регистрация обработчиков состояний
dp.message.register(handle_main_menu, StateFilter(None))
dp.message.register(process_classification, StateFilter(MainStates.waiting_for_classification))
dp.message.register(process_summarization, StateFilter(MainStates.waiting_for_summarization))
dp.message.register(process_analysis, StateFilter(MainStates.waiting_for_analysis))
dp.message.register(process_reasoning, StateFilter(MainStates.waiting_for_reasoning))
dp.include_router(payment_router)
# Основная функция запуска бота
async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())

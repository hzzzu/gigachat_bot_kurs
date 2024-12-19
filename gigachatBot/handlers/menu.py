from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from handlers.payment import send_invoice
from keyboards.main_menu import role_kb
from states.states import MainStates
from config import gigachat, stats
from lexicon.lexicon import LEXICON


# Обработчики текстовых команд
async def handle_main_menu(message: types.Message, state: FSMContext, bot: Bot):
    if message.text == "Роль":
        await message.answer(text=LEXICON['role'], reply_markup=role_kb)
        await state.set_state(MainStates.waiting_for_role)
    elif message.text == "Классификация":
        await message.answer("Введите текст для классификации:")
        await state.set_state(MainStates.waiting_for_classification)
    elif message.text == "Обобщение":
        await message.answer("Введите текст для обобщения:")
        await state.set_state(MainStates.waiting_for_summarization)
    elif message.text == "Анализ":
        await message.answer("Введите текст для анализа:")
        await state.set_state(MainStates.waiting_for_analysis)
    elif message.text == "Логическое рассуждение":
        await message.answer("Введите текст для логического рассуждения:")
        await state.set_state(MainStates.waiting_for_reasoning)
    elif message.text == "Оплатить":
        await send_invoice(message, state, bot)
    else:
        await message.answer("Я не понимаю эту команду. Пожалуйста, выберите опцию из меню.")



async def process_classification(message: types.Message, state: FSMContext):
    try:
        result = gigachat.classify_text(message.text)
        stats['classification'] += 1
        await message.answer(f"Результат классификации:\n{result}")
    except Exception as e:
        await message.answer(f"Ошибка при классификации: {e}")
    await state.clear()


async def process_summarization(message: types.Message, state: FSMContext):
    try:
        result = gigachat.summarize_text(message.text)
        stats['summarization'] += 1
        await message.answer(f"Результат обобщения:\n{result}")
    except Exception as e:
        await message.answer(f"Ошибка при обобщении: {e}")
    await state.clear()


async def process_analysis(message: types.Message, state: FSMContext):
    try:
        result = gigachat.analyze_text(message.text)
        stats['analysis'] += 1
        await message.answer(f"Результат анализа:\n{result}")
    except Exception as e:
        await message.answer(f"Ошибка при анализе: {e}")
    await state.clear()


async def process_reasoning(message: types.Message, state: FSMContext):
    try:
        result = gigachat.logical_reasoning(message.text)
        stats['reasoning'] += 1
        await message.answer(f"Результат логического рассуждения:\n{result}")
    except Exception as e:
        await message.answer(f"Ошибка при логическом рассуждении: {e}")
    await state.clear()

async def process_role(message: types.Message, state: FSMContext):
    try:
        result = gigachat.classify_text(message.text)
        stats['role'] += 1
        await message.answer(f"Вы выбрали роль:\n{result}")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")
    await state.clear()
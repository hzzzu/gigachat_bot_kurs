# Состояния
from aiogram.fsm.state import StatesGroup, State


class MainStates(StatesGroup):
    waiting_for_role = State()
    waiting_for_classification = State()
    waiting_for_summarization = State()
    waiting_for_analysis = State()
    waiting_for_reasoning = State()
    waiting_for_payment_amount = State()

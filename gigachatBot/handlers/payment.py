from aiogram import Router, F, Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, ContentType
from states.states import MainStates

router = Router()

@router.message(F.text == "Оплатить")
async def send_invoice(message: types.Message, state: FSMContext, bot: Bot):
    await state.set_state(MainStates.waiting_for_payment_amount)
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Оплата премиум-версии",
        description="Оплата премиум-версии",
        payload="Payment through a bot",
        provider_token="1744374395:TEST:f2f9eba0406cb4e94727",  # Вставь токен оплаты из BotFather
        currency="rub",
        prices=[
            LabeledPrice(
                label="Покупка премиум-версии",
                amount=500_00
            ),
            LabeledPrice(
                label="НДС",
                amount=100_00
            ),
            LabeledPrice(
                label="Скидка",
                amount=-10_00
            )
        ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000, 2000, 3000],
        start_parameter="pay",
        need_name=True,
        need_phone_number=False,
        need_email=False,
        need_shipping_address=False,
        request_timeout=15
    )

@router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: Message):
    total_amount = message.successful_payment.total_amount / 100
    await message.answer(
        text=f"Спасибо за оплату {total_amount} {message.successful_payment.currency}! Вы купили премиум-версию"
    )

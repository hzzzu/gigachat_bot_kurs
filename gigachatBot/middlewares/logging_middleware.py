from aiogram import BaseMiddleware
from aiogram.types import Message

class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data: dict):
        # Логирование сообщений
        user = event.from_user
        print(f"[LOG] User: {user.id}, Username: {user.username}, Message: {event.text}")
        # Передача управления следующему обработчику
        return await handler(event, data)

from aiogram.filters.callback_data import CallbackData

class RoleCallbackFactory(CallbackData, prefix="role"):
    role_code: int
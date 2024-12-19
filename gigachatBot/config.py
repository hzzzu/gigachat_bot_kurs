from collections import defaultdict
from utils.gigachat_api import GigaChatAPI

# Конфигурация API GigaChat
GIGACHAT_API_KEY = "MjZiZTU0NGYtMWI2Zi00MDMxLTg1ZjMtODExMmVmNmM3NzcyOjA2NWVkOGFjLWZjNTgtNDVlNi1iYjFkLWM0ODA4NTUyZmY5Mw=="
gigachat = GigaChatAPI(api_key=GIGACHAT_API_KEY)

# Статистика использования
stats = defaultdict(int)

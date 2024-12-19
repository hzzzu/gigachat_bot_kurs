from gigachat import GigaChat

class GigaChatAPI:
    gigachat: GigaChat

    def __init__(self, api_key):
        self.gigachat = GigaChat(
            credentials=api_key,
            model="GigaChat",
            verify_ssl_certs=False,
            scope="GIGACHAT_API_PERS",
            streaming=False,
        )

    def classify_text(self, text):
        context = 'Классифицируй этот текст'
        response = self.gigachat.chat(f"{context} {text}")
        return response.choices[0].message.content

    def summarize_text(self, text):
        context = 'Обобщи этот текст'
        response = self.gigachat.chat(f"{context} {text}")
        return response.choices[0].message.content

    def analyze_text(self, text):
        context = 'Анализируй этот текст'
        response = self.gigachat.chat(f"{context} {text}")
        return response.choices[0].message.content

    def logical_reasoning(self, text):
        context = 'Логически рассуди этот текст'
        response = self.gigachat.chat(f"{context} {text}")
        return response.choices[0].message.content
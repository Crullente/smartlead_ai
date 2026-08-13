import requests

from config import Config

class AIServiceError(Exception):
    """
    Yapay zeka servisiyle ilgili hatalar için özel hata sınıfı.
    """
    pass

class AIService:
    """
    Yapay zeka servisleriyle iletişimden sorumlu servis sınıfı.
    """
    GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
    MODEL = "llama-3.1-8b-instant"

    def _get_system_prompt(self):
        """
        Config üzerinden yapay zekânın sistem talimatını getirir.
        """

        return Config.BUSINESS_CONTEXT

    def _groq_request(self, messages):
        """
        Groq API'sine istek gönderir ve cevabı döndürür.
        """

        api_key = Config.GROQ_API_KEY

        if not api_key:
            return (
                "Demo modu: Groq API anahtarı bulunamadı. "
                "Şu anda gerçek yapay zekâ yanıtı üretilemiyor."
            )

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.MODEL,
            "messages": messages
        }

        try:
            response = requests.post(
                self.GROQ_URL,
                headers=headers,
                json=data,
                timeout=30
            )

            response.raise_for_status()

            result = response.json()

            return result["choices"][0]["message"]["content"]

        except (requests.RequestException, KeyError, IndexError) as e:
            raise AIServiceError(
                f"Groq API isteği başarısız oldu: {e}"
            ) from e

    def yanit_uret(self, mesaj, gecmis):
        """
        Kullanıcı mesajını ve konuşma geçmişini Groq'a gönderir.
        """

        system_prompt = self._get_system_prompt()

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        messages.extend(gecmis)

        messages.append(
            {
                "role": "user",
                "content": mesaj
            }
        )

        return self._groq_request(messages)

ai_service = AIService()
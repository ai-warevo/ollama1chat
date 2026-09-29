"""Модуль, реализующий интерактивного агента для работы с Ollama API."""

import sys

from ollama import Client, ResponseError


class OllamaChat:
    """Класс для управления сессией консольного чата с Ollama."""

    def __init__(self, model_name: str):
        """Инициализирует клиента Ollama и сохраняет имя модели."""
        self.model_name = model_name
        self.client = Client()

    def _ask(self, prompt: str) -> str:
        """Отправляет запрос к Ollama и возвращает текстовый ответ."""
        answer = self.client.generate(
            model=self.model_name, prompt=prompt, options={"stream": False}
        )
        return answer.response or ""

    def _get_user_input(self) -> str:
        user_input = input("Вы: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Выход.")
            sys.exit(0)

        return user_input

    def get_current_model(self) -> str:
        """Возвращает имя текущей используемой модели."""
        return self.model_name

    def start_loop(self):
        """Запускает бесконечный цикл диалога в консоли."""
        print(f"🤖 Ollama CLI ({self.model_name}). Для выхода введите 'exit'.\n")

        while True:
            try:
                user_input = self._get_user_input()
                if not user_input:
                    continue

                print("Ollama думает...", end="", flush=True)
                answer = self._ask(user_input)
                print(f"\rOllama: {answer}\n")

            except ResponseError as e:
                print(f"\n❌ Ошибка модели: {e}\n")
            except KeyboardInterrupt:
                print("\nВыход.")
                sys.exit(0)
            except Exception as e:
                print(f"\n❌ Непредвиденная ошибка: {e}\n")

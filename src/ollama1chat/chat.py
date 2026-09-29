import sys
from ollama import Client, ResponseError


class OllamaChat:

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.client = Client()

    def _ask(self, prompt: str) -> str:
        response = self.client.generate(
            model=self.model_name, prompt=prompt, options={"stream": False}
        )
        return response.response

    def _get_user_input(self) -> str:
        user_input = input("Вы: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Выход.")
            sys.exit(0)

        return user_input

    def start_loop(self):
        print(
            f"🤖 Ollama CLI ({self.model_name}). Для выхода введите 'exit'.\n"
        )

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

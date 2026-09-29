"""Главная точка входа для запуска CLI приложения ollama1chat."""

from .chat import OllamaChat
from .cli import parse_args


def main() -> None:
    """Оркестрирует инициализацию аргументов и запуск основного цикла чата."""
    model_name = parse_args()
    bot = OllamaChat(model_name=model_name)
    bot.start_loop()


if __name__ == "__main__":
    main()

"""Модуль для работы с аргументами командной строки."""

import sys


def parse_args() -> str:
    """Парсит аргументы командной строки и возвращает имя модели."""
    default_model = "llama3"

    if "--model" in sys.argv:
        try:
            idx = sys.argv.index("--model")
            return sys.argv[idx + 1]
        except IndexError:
            print("❌ Ошибка: после флага --model нужно указать название модели.")
            sys.exit(1)

    return default_model

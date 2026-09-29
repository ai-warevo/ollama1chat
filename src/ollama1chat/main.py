from .cli import parse_args
from .chat import OllamaChat


def main():
    model_name = parse_args()
    bot = OllamaChat(model_name=model_name)
    bot.start_loop()


if __name__ == "__main__":
    main()

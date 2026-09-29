# ollama1chat

A simple CLI chat interface for [Ollama](https://ollama.com/). Chat with your favorite local LLMs directly from your terminal.

## Features

- 💬 **Interactive Chat:** Seamlessly talk to your local models.
- 🚀 **Lightweight & Fast:** Minimal dependencies, focused on speed and simplicity.
- 🛠️ **Customizable Models:** Specify which model you want to use with ease.

## Prerequisites

- [Ollama](https://ollama.com/) installed and running on your machine.
- [Python 3.14+](https://www.python.org/) (as configured in `pyproject.toml`).
- [uv](https://github.com/astral-sh/uv) for Python package and environment management.

## Installation

First, clone this repository:

```bash
git clone <your-repository-url>
cd ollama1chat
```

Install the project using `uv`:

```bash
uv sync
```

To install the CLI tool globally (optional):

```bash
uv tool install .
```

## Usage

Start a chat session with the default model (`llama3`):

```bash
uv run ollama1chat
```

Or specify a different model:

```bash
uv run ollama1chat --model <model_name>
# Example:
uv run ollama1chat --model llama3
```

To exit the chat, type `exit` or `quit`, or press `Ctrl+C`.

## Development

This project uses modern Python tooling for high code quality.

### Linting, Formatting and Checking

Used to ensure consistent style and catch errors early. The easiest way is to run all checks at once:

```bash
uv run check
```

Or run them individually:

```bash
# Run linting
uv run ruff check .

# Run formatting
uv run black .

# Type checking
uv run mypy src/
```


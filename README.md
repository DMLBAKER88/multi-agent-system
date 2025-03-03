# Multi-Agent System

This is a simple Python-based multi-agent system framework. Agents communicate through a message queue, share tools, and can use local LLMs via Ollama or OpenAI APIs.

## How to Run

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Run the system:
    ```
    python main.py
    ```

## Configuration

Edit `config.py` to choose between local Ollama models and OpenAI.

## Project Structure

- **agents/**: Individual agent logic.
- **tools/**: Shared tools agents can use.
- **memory/**: SQLite for task state.
- **utils/**: Logging and LLM helpers.

This is my first change, just testing my GitHub connection!

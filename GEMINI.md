# Gemini Agent Guidelines

This document provides guidelines for interacting with the Gemini-powered agent in this repository. The agent is designed to assist with various development tasks, from running tests to generating code.

## Project Structure & Module Organization

This is a Python-first, multi-project repo. Each folder under the root (e.g., `local-rag-assistant/`, `llm-deployment-fastapi/`, `agent-playground-lite/`) is a self-contained module with:

- `requirements.txt` (module deps)
- `demo.py` (runnable example)
- `README.md` (module docs)
- `src/` for code
- `tests/` for unit tests
- `eval/` for experiments
- `results/` for artifacts.

You can ask the agent to list the contents of any directory to understand the structure better (e.g., "list files in `local-rag-assistant`").

## Build, Test, and Development Commands

The agent can execute build, test, and development commands for you.

- **Create env:** `python -m venv .venv && source .venv/bin/activate` (Windows: `.venv\Scripts\activate`)
- **Install deps:** `pip install -r requirements.txt`
- **Run demo:** `python demo.py`
- **Run tests:** `pytest -q`

**Example:** "install dependencies for `llm-deployment-fastapi`" or "run the tests for all modules".

## Coding Style & Naming Conventions

The agent will adhere to the following coding style and naming conventions:

- Python 3.10+; 4-space indentation; UTF-8 files.
- Use type hints and docstrings for public functions.
- Naming: `snake_case` for functions/vars, `PascalCase` for classes, `SCREAMING_SNAKE_CASE` for constants.
- Module layout: place implementations under `src/<package>/` and keep `demo.py` minimal.
- Prefer small, pure functions; avoid side effects in module import scope.

## Testing Guidelines

The agent will follow these guidelines when writing or running tests:

- **Framework:** `pytest`
- **Structure:** `tests/test_*.py`; mirror package structure under `tests/`.
- **Conventions:** Arrange–Act–Assert; use fixtures for I/O or network boundaries.

You can ask the agent to "write a test for the function `my_function` in `src/my_module/my_file.py`".

## Generating Commit Messages and Summaries

While the agent does not create commits or pull requests, it can help you generate them. For example, after making changes, you can ask the agent to "generate a commit message for the recent changes".

## Security & Configuration

The agent is designed with security in mind:

- **Never expose secrets:** The agent will never ask for, store, or expose secrets, API keys, or other sensitive information.
- **Use `.env` files:** For configuration that requires secrets, the agent will use `.env` files and can help you create an `.env.example` file.

## Interacting with the Gemini Agent

Here are some tips for effectively interacting with the agent:

- **Be specific:** The more specific your request, the better the agent can assist you. For example, instead of "fix the code", try "fix the bug in `src/my_module/my_file.py` that causes a `ValueError`".
- **Provide context:** Use the `@` symbol to reference files (e.g., `@src/my_module/my_file.py`). This helps the agent to quickly locate the relevant files.
- **Ask for explanations:** If you don't understand a piece of code, you can ask the agent to "explain the function `my_function` in `@src/my_module/my_file.py`".
- **Generate code:** You can ask the agent to generate code for you. For example, "create a new function in `src/my_module/my_file.py` that takes a list of integers and returns the sum".

# Gemini AI Coding Agent

This project is an intelligent AI coding agent powered by the Google Gemini API. It's designed to understand and execute coding-related tasks by interacting with your file system. The agent can list files, read their contents, execute Python scripts, and write new files or modify existing ones, all within a defined working directory for security.

## Features

*   **File and Directory Listing**: Get information about files and directories in the working directory.
*   **File Content Reading**: Read the content of any file within the working directory.
*   **Python Script Execution**: Run Python scripts with optional command-line arguments.
*   **File Writing and Overwriting**: Create new files or modify existing ones with specified content.
*   **Secure Operation**: All file system operations are constrained to the agent's working directory.

## How It Works

The agent leverages the Google Gemini model to interpret user prompts and generate a "plan" in the form of tool calls. These tool calls are then executed by the agent's internal `function_call` mechanism, which dispatches to a set of predefined Python functions (e.g., `get_file_info`, `read_file`, `run_python_file`, `write_file`). The results of these operations are fed back to the Gemini model, allowing it to iteratively refine its understanding and achieve the requested task.

## Setup

To get this agent running, follow these steps:

### Prerequisites

*   Python 3.8+ installed on your system.
*   A Google Gemini API Key. You can obtain one from the [Google AI Studio](https://aistudio.google.com/app/apikey).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    In the root of your project directory, create a file named `.env` and add your Gemini API key:
    ```
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```
    Replace `"YOUR_GEMINI_API_KEY"` with your actual API key.

## Usage

Run the agent from your terminal with a prompt. The agent will attempt to fulfill your request using its available tools.

```bash
python main.py "your coding request here"
```

### Examples

*   **List files in the current directory:**
    ```bash
    python main.py "List all files in the current directory."
    ```
*   **Read the content of a file:**
    ```bash
    python main.py "Read the content of main.py"
    ```
*   **Write a new file:**
    ```bash
    python main.py "Create a new file called 'hello.py' with the content 'print(\"Hello, AI!\")'"
    ```
*   **Run a Python script:**
    ```bash
    python main.py "Run the script 'hello.py'"
    ```

### Verbose Mode

You can run the agent in verbose mode to see the internal function calls it makes:

```bash
python main.py "your coding request here" --verbose
```

## Project Structure

*   `main.py`: The main entry point for the agent.
*   `function_call.py`: Handles the execution and routing of tool calls from the Gemini model.
*   `config.py`: Contains global configuration settings, such as `WORKING_DIRECTORY`.
*   `functions/`: A directory containing the implementations of the tools the agent can use (e.g., `get_file_info.py`, `write_file.py`).
*   `requirements.txt`: Lists all Python dependencies.
*   `.env`: Stores environment variables, including your Gemini API key.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# LangChain Models Repository

This repository contains various experiments and implementations using [LangChain](https://python.langchain.com/), focusing on building AI agents, chatbots, and chains.

## Structure

*   **chains/**: Examples of different LangChain chains.
*   **models/**: LLM integration and configuration examples.
*   **parsers/**: Output parser implementations (JSON, XML, etc.).
*   **prompts/**: Prompt template examples and strategies.
*   **runnables/**: Runnable sequences, parallel execution, and branching logic.
*   **notebooks/**: Jupyter notebooks for learning notes and tutorials.
*   **projects/**: Complete mini-projects (Review Analyzer, Basic Chatbot).
*   **playground/**: Scratchpad scripts for testing concepts.

## Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/LangChain_models.git
    cd LangChain_models
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables**:
    Create a `.env` file in the root directory and add your API keys:
    ```env
    HUGGINGFACEHUB_API_TOKEN=your_token_here
    OPENAI_API_KEY=your_key_here
    ```

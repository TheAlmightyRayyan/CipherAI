# Cipher AI Chatbot

Cipher AI is an intelligent chatbot built using [Streamlit](https://streamlit.io/) and integrated with the Dify API. The chatbot offers seamless conversations and provides meaningful responses based on user input.

## Features

- **Real-time Chat**: Engage in conversations with the chatbot and get instant responses.
- **Dify API Integration**: Powered by the Dify API for intelligent conversational capabilities.
- **Session Management**: The conversation ID is maintained across sessions to keep track of chat history.
- **Responsive UI**: Styled chat interface for a user-friendly experience.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cipher-ai-chatbot.git
    cd cipher-ai-chatbot
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project directory and add your Dify API key:
    ```bash
    DIFY_API_KEY="your_dify_api_key"
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to interact with the Cipher AI chatbot.

## API Integration

This chatbot uses the [Dify API](https://dify.ai/docs) for generating responses. Make sure to obtain an API key by signing up for Dify, and replace the placeholder with your actual API key in the `.env` file.

### API Endpoint Used

- `POST https://api.dify.ai/v1/chat-messages`: Sends the user's query to the Dify server and retrieves the response.


## Customization

- Modify the chatbot's name, UI styling, and additional configurations inside `app.py`.
- Adjust the API requests and response handling logic as needed.

## Dependencies

- Streamlit
- requests
- python-dotenv

To install all the dependencies, run:
```bash
pip install -r requirements.txt

## Credit
- Made by rayyan


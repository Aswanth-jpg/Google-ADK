# Google AI Agent Project

This project is an AI agent built using Google's ADK Python library. The agent can provide the current time for various cities around the world using timezone-aware logic.

## Features
- Returns the current time for supported cities
- Uses Google's Gemini model for LLM tasks
- Timezone conversion powered by `pytz`

## Setup
1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   ```
2. Create and activate a Python virtual environment:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   (Or manually install: `pip install google-adk pytz`)
4. Add your API keys to `.env` or `my_agent/.env` (see below).

## Environment Variables
Add your Google API key and configuration to `.env` or `my_agent/.env`:
```
GOOGLE_API_KEY=your_google_api_key
GOOGLE_GENAI_USE_VERTEXAI=0
```

## Usage
To run the agent:
```sh
adk run my_agent
```
To start the web server:
```sh
adk web --port 8000
```

## Security
- `.env` and `my_agent/.env` are ignored by Git for safety.
- Do not share your API keys publicly.

## License
This project is based on Google's ADK Python library. See the original repository for license details.

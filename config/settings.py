import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LMSTUDIO_BASE_URL = os.getenv("LMSTUDIO_BASE_URL")
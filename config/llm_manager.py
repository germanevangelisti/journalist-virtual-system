from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY, LMSTUDIO_BASE_URL

class LLMManager:
    _instance = None

    def __new__(cls, model="gpt-4", temperature=0.7):
        if cls._instance is None:
            cls._instance = super(LLMManager, cls).__new__(cls)

            if LMSTUDIO_BASE_URL:
                # Use LMStudio or other local LLM if base_url is set
                cls._instance.llm = ChatOpenAI(base_url=LMSTUDIO_BASE_URL, api_key="anything-is-possible", model=model, temperature=temperature)
            elif OPENAI_API_KEY:
                # Fallback to OpenAI if API Key is present
                cls._instance.llm = ChatOpenAI(model=model, temperature=temperature, openai_api_key=OPENAI_API_KEY)
            else:
                # If neither is available, we might want to raise an error or return a mock/dummy
                # For now, we will initialize with a dummy key to let the library raise the error when invoked,
                # or print a warning.
                print("Warning: No OpenAI API KEY or LMStudio URL found. LLM calls will fail.")
                cls._instance.llm = ChatOpenAI(api_key="invalid-key")

        return cls._instance

    def get_llm(self):
        return self.llm

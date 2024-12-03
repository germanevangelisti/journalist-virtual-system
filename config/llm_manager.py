from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY, LMSTUDIO_BASE_URL

class LLMManager:
    _instance = None

    def __new__(cls, model="gpt-4", temperature=0.7):
        if cls._instance is None:
            cls._instance = super(LLMManager, cls).__new__(cls)
            # cls._instance.llm = ChatOpenAI(model=model, temperature=temperature, openai_api_key=OPENAI_API_KEY)
            cls._instance.llm = ChatOpenAI(base_url=LMSTUDIO_BASE_URL, api_key="anything-is-possible")
        return cls._instance

    def get_llm(self):
        return self.llm

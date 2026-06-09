from langchain_moonshot import ChatMoonshot
from langchain_openai import ChatOpenAI

from config import settings

def get_kimi_llm():
    return ChatMoonshot(
        model="kimi-k2.5",
        thinking=False,
        temperature=0.6,
        max_retries=2,
        api_key=settings.kimi_api_key,
        # prompt_cache_key="docs-example-cache",
        # safety_identifier="docs-example-user",
        # max_completion_tokens=1024,
    )

def get_openai_llm():
    return ChatOpenAI(
        model="gpt-4o",
        temperature=0.6,
        max_retries=2,
        api_key=settings.openai_api_key,
    )


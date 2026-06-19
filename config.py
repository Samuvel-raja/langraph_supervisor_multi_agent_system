from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    kimi_api_key: str
    openai_api_key: str
    langchain_tracing_v2: str
    langchain_project: str
    langchain_api_key: str
    google_client_id: str
    google_client_secret: str
    mongo_uri:str
    mongo_db_name:str

settings = Settings()

from pydantic import BaseSettings
from pymongo import MongoClient


def get_db():
    cluster = settings.db_url

    client = MongoClient(cluster)
    db = client.foondaMate
    return db


class Settings(BaseSettings):
    db_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()

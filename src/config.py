from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DB(BaseModel):
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    NAME: str


class APP(BaseModel):
    SECRET_KEY: str
    PERMANENT_SESSION_LIFETIME: int


class Config(BaseSettings):
    DB: DB
    APP: APP

    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        extra="ignore",
    )

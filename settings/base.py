from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ENV_PATH = os.path.join(PROJECT_ROOT_PATH, "settings", f"{ENVIRONMENT}.env")
LOGS_BASE_PATH = os.path.join(PROJECT_ROOT_PATH, 'logs')


class Settings(BaseSettings):
    class Config:
        env_file = ENV_PATH  # 必须使用环境变量的绝对路径
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"
    
    # MYSQL
    MYSQL_SQL_SERVER: Optional[str] = None
    MYSQL_SQL_PORT: Optional[str] = None
    MYSQL_SQL_USER: Optional[str] = None
    MYSQL_SQL_PASSWORD: Optional[str] = None
    MYSQL_SQL_DB_NAME: Optional[str] = None
    PROJECT_NAME: Optional[str] = None
    PROJECT_ROOT_PATH: Optional[str] = PROJECT_ROOT_PATH
    LOGS_BASE_PATH: Optional[str] = LOGS_BASE_PATH


@lru_cache()
def get_settings():
    return Settings()


config = get_settings()

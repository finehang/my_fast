from base import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{config.MYSQL_SQL_USER}:{config.MYSQL_SQL_PASSWORD}@"
    f"{config.MYSQL_SQL_SERVER}:{config.MYSQL_SQL_PORT}/{config.MYSQL_SQL_DB_NAME}?charset=utf8mb4")
ASYNC_SQLALCHEMY_DATABASE_URL = (
    f"mysql+aiomysql://{config.MYSQL_SQL_USER}:{config.MYSQL_SQL_PASSWORD}@"
    f"{config.MYSQL_SQL_SERVER}:{config.MYSQL_SQL_PORT}/{config.MYSQL_SQL_DB_NAME}?charset=utf8mb4")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=200,
    max_overflow=200,
    pool_recycle=300,
    pool_pre_ping=True,
    pool_use_lifo=True,
    pool_reset_on_return=None,
    pool_timeout=30,
    pool_echo=False,
    pool_echo_pool=False,
    pool_echo_pool_options=None,
    pool_logging_name=None,
)

Base = declarative_base()
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

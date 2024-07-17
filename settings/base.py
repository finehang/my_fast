from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "")
ENVIRONMENT = "dev"


# ENVIRONMENT = "pro"


class Settings(BaseSettings):
    class Config:
        env_file = f"{ENVIRONMENT}.env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"
    
    """System configurations."""
    
    # 系统安全秘钥
    SECRET_KEY: Optional[str] = None
    
    # API版本号
    API_VERSION_STR = "/api/v3"
    
    # token过期时间8小时
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 60 * 8
    
    # 算法
    ALGORITHM = "HS256"
    
    # 产品名称
    PRODUCTION_NAME = "gatherone_crm"
    
    # 允许访问的源
    ALLOW_ORIGINS = [
        '*'
    ]
    
    # REDIS存储
    REDIS_STORAGE = {
        'invitation_code': 1,  # 邀请码
        'email_code': 2,  # 邮箱验证码
        'login_info': 3,  # 登录信息
        'sms_code': 4,  # 手机验证码
        'scene': 5,  # 存储场景值
        'api_key': 8,  # api_key
        'pingpongtoken': 9,  # pingpong_refresh_token
    }
    
    # MQ
    MQ_HOST: Optional[str] = None
    MQ_PORT: Optional[str] = None
    MQ_USERNAME: Optional[str] = None
    MQ_PASSWORD: Optional[str] = None
    MQ_VIRTUAL_HOST: Optional[str] = None
    
    # REDIS
    REDIS_HOST: Optional[str] = None
    REDIS_PORT: Optional[int] = None
    REDIS_USERNAME: Optional[str] = None
    REDIS_PASSWORD: Optional[str] = None
    
    # MYSQL
    MYSQL_SQL_SERVER: Optional[str] = None
    MYSQL_SQL_PORT: Optional[str] = None
    MYSQL_SQL_USER: Optional[str] = None
    MYSQL_SQL_PASSWORD: Optional[str] = None
    MYSQL_SQL_DB_NAME: Optional[str] = None
    
    # 认证服务
    AUTH_RPC_SERVER: Optional[str] = None
    
    # 媒体api接口
    API_BASE_URL: Optional[str] = None
    API_KEY: Optional[str] = None
    API_KEY_PREFIX: Optional[str] = None
    
    # 空中云汇
    AirWallexUrl: Optional[str] = None
    AirWallexClientId: Optional[str] = None
    AirWallexApiKey: Optional[str] = None
    
    # PingPong
    PingPongUrl: Optional[str] = None
    PingPongCodeUrl: Optional[str] = None
    PingPongAppId: Optional[str] = None
    PingPongAppSecret: Optional[str] = None
    PingPongOpenId: Optional[str] = None
    PingPongUserId: Optional[str] = None
    PingPongUserSecret: Optional[str] = None
    
    # 阿里云
    ACCESSKEY_ID: Optional[str] = None
    ACCESSKEY_SECRET: Optional[str] = None
    BUCKET_NAME: Optional[str] = None
    END_POINT: Optional[str] = None
    ALIOSS_URL: Optional[str] = None
    OSS_PREFIX: Optional[str] = None
    
    # 天行数据api
    TIANAPI_KEY: Optional[str] = None


@lru_cache()
def get_settings():
    return Settings()


config = get_settings()

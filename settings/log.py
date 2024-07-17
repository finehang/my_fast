import time
import os

from loguru import logger

logs_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')


class MainLog:
    def __init__(self):
        logger.remove()
        create_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        logger.add(
            name=os.path.join(logs_path, create_time + '.log'),
            format="{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}",
            level="INFO",
            rotation="00:00",
            retention="7 days",
            encoding="utf-8",
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )

import os
import time
from loguru import logger

from settings.base import config


class MainLog:
    def __init__(self, file):
        """
        任何调用本类的文件,初始化将自动在项目logs目录下建立对应目录结构的log文件
        :param file: 调用本类的文件的绝对路径
        """
        log_time = time.strftime("%Y-%m-%d", time.localtime())
        base_name = os.path.splitext(os.path.basename(file))[0] + f"_{log_time}.log"
        dir_name = os.path.dirname(os.path.abspath(file))
        relative_dir = os.path.relpath(dir_name, config.PROJECT_ROOT_PATH)
        self.log_path = os.path.join(str(config.LOGS_BASE_PATH), str(relative_dir))
        self.log_name = os.path.join(str(self.log_path), str(base_name))
        self.mk_log_dir()
        
        logger.add(
            sink=self.log_name,
            encoding="utf-8",
            level="INFO",  # 日志文件记录的最低层级
            rotation="500MB",
            retention="5 days",
            compression="zip",
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )
        self.log = logger
    
    def mk_log_dir(self):
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)
    
    def get_logger(self, log_type):
        """
        返回传入类型的的日志记录器
        :param log_type: ["info","error"]等
        :return:
        """
        return getattr(self.log, log_type)

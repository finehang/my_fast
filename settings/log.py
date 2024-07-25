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
        self.__log_path = os.path.join(str(config.LOGS_BASE_PATH), str(relative_dir))
        self.__log_name = os.path.join(str(self.__log_path), str(base_name))
        self.__mk_log_dir()
        
        logger.add(
            sink=self.__log_name,
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
    
    def __mk_log_dir(self):
        if not os.path.exists(self.__log_path):
            os.makedirs(self.__log_path)
    
    # TRACE：用于追踪代码中的详细信息。
    # DEBUG：用于调试和开发过程中的详细信息。
    # INFO：用于提供一般性的信息，表明应用程序正在按预期运行。
    # SUCCESS：用于表示成功完成的操作。
    # WARNING：用于表示潜在的问题或警告，不会导致应用程序的中断或错误。
    # ERROR：用于表示错误，可能会导致应用程序的中断或异常行为。
    # CRITICAL：用于表示严重错误，通常与应用程序无法继续执行相关。
    
    def __getattr__(self, item):
        try:
            return getattr(self.log, item)
        except AttributeError:
            raise AttributeError(f"{item} is not a valid log level")


def get_logger(f=__file__):
    return MainLog(f)

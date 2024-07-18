from settings.log import MainLog

my_log = MainLog(__file__)
log_info = my_log.get_logger("info")
log_error = my_log.get_logger("error")


def mian():
    log_info(("info!!!!", "yeah"))
    log_error(("error!!!!", "no no no no"))


if __name__ == '__main__':
    mian()

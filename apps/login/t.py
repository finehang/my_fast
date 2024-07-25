from settings.log import get_logger

logger = get_logger(__file__)


def mian():
    logger.info(("info!!!!", "yeah"))
    logger.error(("error!!!!", "no no no no"))


if __name__ == '__main__':
    mian()

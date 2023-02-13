import logging

log_format = (
    "%(asctime)s [%(levelname)s] %(name)s %(funcName)15s(%(lineno)d) - %(message)s"
)

file_handler = logging.FileHandler("app_error_log.logs")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter(log_format))


stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter(log_format))


file_handler = logging.FileHandler("app_info_log.logs")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(log_format))


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

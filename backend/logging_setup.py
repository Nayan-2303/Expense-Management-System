import logging


def setup_logger(name, log_files='server.log', level=logging.DEBUG):
    # create custome logger
    logger = logging.getLogger(name)

    # configure the custom logger

    logger.setLevel(level)
    file_handler = logging.FileHandler(log_files)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
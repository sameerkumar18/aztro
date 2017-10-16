import logging


def _setup_debug_logger(name, level=logging.INFO, log_format=None):
    # create logger with name provided
    logger = logging.getLogger(name)
    logger.setLevel(level)
    # create file handler which logs even debug messages
    fh = logging.FileHandler("%s.log" % name)
    fh.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    if not log_format:
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    return logger

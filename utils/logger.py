import logging

def setup_logger(name="VideoProject"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

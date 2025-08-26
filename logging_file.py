import logging


def setup_logging(script_name):
    # Create a logger object
    logger = logging.getLogger(script_name)
    logger.setLevel(logging.DEBUG)

    # Create a file handler for the script
    handler = logging.FileHandler(script_name, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
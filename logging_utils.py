"""
This module provides utils functions to logging data
"""

import logging


def get_logger_handle(name: str, level=logging.INFO) -> logging.Logger:
    """
    Construct a logger handle based on name and logging level and return the handle.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    return logger



def log_txt(data, logger: logging.Logger) -> None:
    """
    Get pretty table format logging of a dataframe
    """
    for line in data: # files are iterable
        logger.info(line)

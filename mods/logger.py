from logging import getLogger, StreamHandler, INFO, Formatter


def set_logger(name: str) -> getLogger:
    """
    Set logger for the given name.
    
    Args:
        name (str): Name of the logger.
    
    Returns:
        getLogger: Logger object.
    """
    logger = getLogger(name)
    handler = StreamHandler()
    logger.setLevel(INFO)
    handler.setLevel(INFO)
    logger.addHandler(handler)
    handler.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    return logger
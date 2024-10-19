import logging


def set_logging(filepath: str) -> None:
    """
    Sets basicConfig at debug level.

    Args:
        filepath (str)

    Returns:
        None
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"{filepath}"),
            logging.StreamHandler()
        ]
    )
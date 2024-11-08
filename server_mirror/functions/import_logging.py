import logging


def main(filepath: str, logger_name: str = None) -> logging.Logger:
    """
    Establishes main logging function.
    
    Parameters:
        filepath (str): ../folder/filename.txt   
        logger_name (str): name_of_logger
        
    Returns:
        logging.Logger (logging.Logger): logging configuration

    Examples:
    Main log argument:
        ("../exports/logging_export.txt", "main_logger")
    To set up the logger:
        my_logger = main(filepath, "my_logger")

    The variable and 3rd function argument should remain the same for ease of referencing.
    """
        # # Tried testing passing boolean to enable StreamHandler, faced issues
        # en_stream (bool): enables StreamHandler (not in use)

    # Create or get the specified logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Clear any existing handlers and prevent duplicates
    if logger.hasHandlers():
        logger.handlers.clear()

    # Configure file handler
    file_handler = logging.FileHandler(filepath)
    file_handler.setLevel(logging.DEBUG)

    # Define formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add file handler to logger
    logger.addHandler(file_handler)

    # # Enable StreamHandler if hints_enabled:
    # if en_stream:
    #     stream_handler = logging.StreamHandler()
    #     stream_handler.setLevel(logging.DEBUG)
    #     stream_handler.setFormatter(formatter)
    #     logger.addHandler(stream_handler)

    return logger


if __name__ == "__main__":
    # try/except added to test docstrings
    try:
        testlogger = main()
    except:
        pass
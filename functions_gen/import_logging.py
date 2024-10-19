import logging

def set_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("functions_alamo/alamo_dtm_logs.txt"),
            logging.StreamHandler()
        ]
    )
import logging
import sys
sys.path.append("..")

from functions import import_logging, alamo_dtm


# Test multiple logging modules
def test_multiple_logging():
    main_logger = import_logging.split("../exports/logging_export.txt", "main_logger")
    main_logger.info(f"{__name__}: TEST TEST TEST from test.py")

    # Call's imported function that will log on their own log .txt
    alamo_dtm.logging_test()


if __name__ == "__main__":
    test_multiple_logging()
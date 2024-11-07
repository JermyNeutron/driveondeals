from functions import import_logging

main_logger = import_logging.main("../exports/logging_export.txt", "main_logger")

path = "../exports/test_log.txt"

def main():
    with open(path, "a") as file:
        mystring = "\nfunction injection with init modified"
        file.write(mystring)

def test():
    main_logger.info("Hey there! I'm being logged from functions/func_test.py")

if __name__ == "__main__":
    main()
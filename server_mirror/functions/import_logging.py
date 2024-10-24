import logging


def main(filepath: str) -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"{filepath}"),
        ]
    )


if __name__ == "__main__":
    pass
import logging


def main(filepath: str) -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"{filepath}"),
            # logging.StreamHandler() # Optional log printing into terminal
        ]
    )


if __name__ == "__main__":
    pass
import os


def get_unique_filename(base_name: str, folder_path: str) -> str:
    """
    Return a unique filename with numerical incremental suffixes if file exists.

    Parameters:
        base_name (str):
        folder_path (str):

    Returns:
        os.path.join (str):
    """
    filename = f"{base_name}.png"
    count = 1
    while os.path.exists(os.path.join(folder_path, filename)):
        filename = f"{base_name}_{count}.png"
        count += 1
    return os.path.join(folder_path, filename)


def verify_folder_path(folder_path: str) -> None:
    """
    Ensure that the specified folder exists. Creates one if it does not.

    Parameters:
        folder_path (str):

    Returns:
        None ():
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


if __name__ == "__main__":
    pass
get_unique_filename()
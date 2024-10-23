import requests


def main(test: bool, hints_enabled: bool) -> None:
    """
    Downloads current .csv file containing the database data from the server hosted on PythonAnywhere.

    Args:
        test (bool)
        hints_enabled (bool)

    Returns:
        None
    """
    url = 'https://jbcrisostomo.pythonanywhere.com/download/data.csv'
    response = requests.get(url)

    local_path = "C:/Users/Jeremy/codelearning/projects/AI Assisted/driveondeals/test/pythonanywherebitch.csv" if test else "C:/Users/Jeremy/codelearning/projects/AI Assisted/driveondeals/temp/data_updated.csv"
    with open(local_path, "wb") as file:
        file.write(response.content)


if __name__ == "__main__":
    test = True
    hints_enabled = True

    main(test, hints_enabled)
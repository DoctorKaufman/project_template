# output.py
import pandas as pd


def output_text_to_console(text):
    """
    Print text to the console.

    Args:
        text (str): Text for printing.
    """
    print(text)


def write_to_file(text, file_path):
    """
    Write text passed to the specified file.

    Args:
        text (str): Text to be written.
        file_path (str): Path to the file.
    """
    with open(file_path, "w") as file:
        file.write(text)


def write_dataframe_to_csv(dataframe, file_path):
    """
    Write dataframe to csv file via pandas.

    Args:
        dataframe (DataFrame): Data to write in csv.
        file_path (str): Path to the file.
    """
    dataframe.to_csv(file_path, index=False)


def write_dict_to_csv(data, file_path):
    """
    Write dictionary to a CSV file.

    Args:
        data (dict): Dictionary containing the data.
        file_path (str): Path to the CSV file.
    """
    df = pd.DataFrame.from_dict(data)
    df.to_csv(file_path, index=False)

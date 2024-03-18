# main.py
import app.io.input as my_input
import app.io.output as my_output
import pandas as pd


def main():
    # Calls to functions to obtain text
    text_from_console = my_input.input_text_from_console()
    text_from_file = my_input.read_text_from_file("data/input.txt")
    text_from_pandas = my_input.read_text_from_file_with_pandas("data/data.csv")

    # Output text to console
    my_output.output_text_to_console(text_from_console)
    my_output.output_text_to_console(text_from_file)
    my_output.output_text_to_console(text_from_pandas)

    # Write text to file
    my_output.write_to_file(text_from_file, "data/output.txt")

    # Create dict
    data = {'Name': ['Andrii', 'Anna', 'Charlie'],
            'Age': [23, 18, 35],
            'City': ['Kyiv', 'Lviv', 'Chicago']}
    df = pd.DataFrame(data)

    # Demonstrate writing from dict
    file_path1 = 'data/dict_output.csv'
    my_output.write_dict_to_csv(data, file_path1)

    # Demonstrate writing from df
    file_path2 = 'data/df_output.csv'
    my_output.write_dataframe_to_csv(df, file_path2)


if __name__ == "__main__":
    main()

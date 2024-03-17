# main.py
import app.io.input as my_input
import app.io.output as my_output


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


if __name__ == "__main__":
    main()

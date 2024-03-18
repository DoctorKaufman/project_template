import unittest
import os
import pandas as pd
from app.io.output import write_to_file, write_dataframe_to_csv


class TestWriteToFile(unittest.TestCase):
    def test_write_text(self):
        test_text = "This text must be written in file with no modifications."
        write_to_file(test_text, "test_output.txt")

        self.assertTrue(os.path.exists("test_output.txt"))

        with open("test_output.txt", "r") as f:
            content = f.read()
            self.assertEqual(content, test_text)

        os.remove("test_output.txt")

    def test_write_empty_text(self):
        write_to_file("", "empty_output.txt")

        self.assertTrue(os.path.exists("empty_output.txt"))

        with open("empty_output.txt", "r") as f:
            written_text = f.read()
            self.assertEqual(written_text, "")

        os.remove("empty_output.txt")

    def test_write_to_not_existing_directory(self):
        with self.assertRaises(OSError):
            write_to_file("test", "/no_such_directory/test_output.txt")


class TestWriteDataFrameToCSV(unittest.TestCase):
    def test_write_csv(self):
        data = {'Name': ['Andrii', 'Anna', 'Charlie'],
                'Age': [23, 18, 35],
                'City': ['Kyiv', 'Lviv', 'Chicago']}
        df = pd.DataFrame(data)

        write_dataframe_to_csv(df, "test_data_output.csv")

        self.assertTrue(os.path.exists("test_data_output.csv"))

        read_df = pd.read_csv("test_data_output.csv")
        self.assertTrue(df.equals(read_df))

        os.remove("test_data_output.csv")

    def test_write_empty_dataframe(self):
        empty_df = pd.DataFrame()

        write_dataframe_to_csv(empty_df, "empty_data_output.csv")

        self.assertTrue(os.path.exists("empty_data_output.csv"))

        # read_df = pd.read_csv("empty_data_output.csv")
        self.assertTrue(os.path.getsize("empty_data_output.csv"), 0)

        os.remove("empty_data_output.csv")


if __name__ == '__main__':
    unittest.main()

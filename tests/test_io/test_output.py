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


if __name__ == '__main__':
    unittest.main()

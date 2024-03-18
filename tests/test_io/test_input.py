import unittest
import app.io.input as my_input
import pandas as pd


class TestInputFunctions(unittest.TestCase):
    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            my_input.read_text_from_file("not_existing.txt")

    def test_read_text_from_file_content(self):
        expected_text = "Test text to check correctness of file reading."
        filename = "../test_data/test_input.txt"
        with open(filename, "w") as file:
            file.write(expected_text)
        actual_text = my_input.read_text_from_file(filename)
        self.assertEqual(actual_text, expected_text)

    def test_read_text_from_file_empty_file(self):
        filename = "../test_data/empty_file.txt"
        open(filename, "w").close()
        text = my_input.read_text_from_file(filename)
        self.assertEqual(text, "")

    def test_read_text_from_file_with_pandas(self):
        filename = "../test_data/test_input.csv"
        with open(filename, "w") as file:
            file.write("Name,Age\nJohn,25\nAnna, 18\nLight, 23")
        text = my_input.read_text_from_file_with_pandas(filename)
        self.assertTrue(text)


if __name__ == "__main__":
    unittest.main()

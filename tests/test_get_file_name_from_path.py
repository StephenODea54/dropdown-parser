import unittest
from dropdown_parser.utils import get_file_name_from_path


class TestGetFileNameFromPath(unittest.TestCase):
    def test_get_file_name_from_path(self):
        # Test with a file path and extension
        file_path = "/path/to/example_file.txt"
        ext = "txt"
        result = get_file_name_from_path(file_path, ext)
        self.assertEqual(result, "example_file")

    def test_get_file_name_from_path_no_ext(self):
        # Test with a file path and no extension
        file_path = "/path/to/example_file"
        ext = ""
        result = get_file_name_from_path(file_path, ext)
        self.assertEqual(result, "example_file")

    def test_get_file_name_from_path_different_ext(self):
        # Test with a file path and a different extension
        file_path = "/path/to/example_file.png"
        ext = "txt"
        result = get_file_name_from_path(file_path, ext)
        self.assertEqual(result, "example_file.png")

    def test_get_file_name_from_path_no_path(self):
        # Test with just the file name and extension
        file_path = "example_file.txt"
        ext = "txt"
        result = get_file_name_from_path(file_path, ext)
        self.assertEqual(result, "example_file")

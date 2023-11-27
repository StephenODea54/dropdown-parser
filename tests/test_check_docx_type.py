import unittest
from unittest.mock import patch
from dropdown_parser.utils import check_docx_type


class TestCheckDocxType(unittest.TestCase):
    @patch("sys.exit")
    def test_check_docx_type_valid_extension(self, mock_sys_exit):
        # Test with a valid .docx extension
        docx_path = "/path/to/document.docx"

        check_docx_type(docx_path)
        mock_sys_exit.assert_not_called()

    def test_check_docx_type_invalid_extension(self):
        # Test with an invalid extension
        docx_path = "/path/to/document.doc"

        with self.assertRaises(SystemExit) as cm:
            check_docx_type(docx_path)

        self.assertEqual(cm.exception.code, "The file must end with a .docx extension.")

    def test_check_docx_type_no_extension(self):
        # Test with a file path without an extension
        docx_path = "/path/to/document"

        with self.assertRaises(SystemExit) as cm:
            check_docx_type(docx_path)

        self.assertEqual(cm.exception.code, "The file must end with a .docx extension.")

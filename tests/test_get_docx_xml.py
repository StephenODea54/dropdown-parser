import unittest
from pathlib import Path
from dropdown_parser.utils import get_docx_xml

SCRIPT_DIR = Path(__file__).parent
TEST_DOC_FILE = SCRIPT_DIR / "test.docx"
TEST_XML_FILE = SCRIPT_DIR / "test_doc.xml"


class TestGetDocxXml(unittest.TestCase):
    def test_get_doc_xml_success(self):
        FAKE_XML = '<w:name w:val="Dropdown1"/>'
        xml_data = get_docx_xml(TEST_DOC_FILE.absolute().as_posix())

        self.assertIn(FAKE_XML, str(xml_data))

    def test_get_docx_xml_zipfile_exception(self):
        with self.assertRaises(Exception) as cm:
            get_docx_xml(TEST_XML_FILE)

        self.assertEqual(str(cm.exception), "File is not a zip file")

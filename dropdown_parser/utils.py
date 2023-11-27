from pathlib import Path
from typing import NoReturn
from zipfile import ZipFile
import sys


def check_docx_type(docx_path: str) -> None:
    if not docx_path.endswith(".docx"):
        sys.exit("The file must end with a .docx extension.")


def get_file_name_from_path(file_path: str, ext: str) -> str:
    file_name = Path(file_path).name
    return file_name.replace(f".{ext}", "")


def get_docx_xml(file_path: str) -> bytes:
    with ZipFile(file_path) as document:
        xml_data = document.read("word/document.xml")
        document.close()

    return xml_data

from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import Callable, List, Literal
import pandas as pd
from .utils import check_docx_type, get_file_name_from_path, get_docx_xml


@dataclass
class DropdownListElement:
    display_text: str
    display_value: str


DropdownList = List[DropdownListElement]
Exporter = Callable[[str, pd.DataFrame], None]
OutputTypes = Literal["csv", "json", "txt", "xlsx"]


def csv_exporter(file_name: str, df: pd.DataFrame) -> None:
    df.to_csv(f"{file_name}.csv", index=False)


def json_exporter(file_name: str, df: pd.DataFrame) -> None:
    df.to_json(f"{file_name}.json", orient="records")


def txt_exporter(file_name: str, df: pd.DataFrame) -> None:
    df.to_csv(f"{file_name}.txt", index=False)


def xlsx_exporter(file_name: str, df: pd.DataFrame) -> None:
    df.to_excel(f"{file_name}.xlsx", index=False)


def get_exporter(out_type: OutputTypes) -> Exporter:
    EXPORTERS = {
        "csv": csv_exporter,
        "json": json_exporter,
        "txt": txt_exporter,
        "xlsx": xlsx_exporter,
    }

    return EXPORTERS[out_type]


class Parser:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.dropdown_list: DropdownList = []

        # Throw error if not .docx file
        check_docx_type(file_path)

    def extract_dropdown_list(self) -> None:
        xml_data = get_docx_xml(self.file_path)

        soup = BeautifulSoup(xml_data, "xml")
        dropdown_lists = soup.findAll("dropDownList")

        for dropdown_list in dropdown_lists:
            for dropdown_list_element in dropdown_list:
                display_text = dropdown_list_element.get("w:displayText")
                display_value = dropdown_list_element.get("w:value")

                self.dropdown_list.append(
                    DropdownListElement(display_text, display_value)
                )

    def parse(self, out_type: OutputTypes):
        self.extract_dropdown_list()

        file_name = get_file_name_from_path(self.file_path, "docx")
        df = pd.DataFrame(self.dropdown_list)

        exporter = get_exporter(out_type)
        exporter(file_name, df)

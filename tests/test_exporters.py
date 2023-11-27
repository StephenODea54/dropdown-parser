import unittest
import pandas as pd
from pathlib import Path
from dropdown_parser.dropdown_parser import (
    csv_exporter,
    json_exporter,
    txt_exporter,
    xlsx_exporter,
)


SCRIPT_DIR = Path(__file__).parent


# Mocking the pandas DataFrame to_csv method
file_name = "test_file"
df = pd.DataFrame({"column1": [1, 2, 3], "column2": ["a", "b", "c"]})

output_file_name = SCRIPT_DIR / f"{file_name}"


class TestExporters(unittest.TestCase):
    def test_csv_exporter(self):
        csv_exporter(output_file_name, df)

        # Assert that the CSV file was created
        csv_path = Path(f"{output_file_name}.csv")
        self.assertTrue(csv_path.is_file())

        # Read the CSV file and compare its contents with the expected DataFrame
        actual_df = pd.read_csv(csv_path)
        pd.testing.assert_frame_equal(df, actual_df)

        # Clean up: remove the created CSV file
        csv_path.unlink()

    def test_json_exporter(self):
        json_exporter(output_file_name, df)

        # Assert that the JSON file was created
        json_path = Path(f"{output_file_name}.json")
        self.assertTrue(json_path.is_file())

        # Read the JSON file and compare its contents with the expected DataFrame
        actual_df = pd.read_json(json_path)
        pd.testing.assert_frame_equal(df, actual_df)

        # Clean up: remove the created JSON file
        json_path.unlink()

    def test_txt_exporter(self):
        txt_exporter(output_file_name, df)

        # Assert that the TXT file was created
        txt_path = Path(f"{output_file_name}.txt")
        self.assertTrue(txt_path.is_file())

        # Read the TXT file and compare its contents with the expected DataFrame
        actual_df = pd.read_csv(txt_path)
        pd.testing.assert_frame_equal(df, actual_df)

        # Clean up: remove the created TXT file
        txt_path.unlink()

    def test_xlsx_exporter(self):
        xlsx_exporter(output_file_name, df)

        # Assert that the XLSX file was created
        xlsx_path = Path(f"{output_file_name}.xlsx")
        self.assertTrue(xlsx_path.is_file())

        # Read the XLSX file and compare its contents with the expected DataFrame
        actual_df = pd.read_excel(xlsx_path)
        pd.testing.assert_frame_equal(df, actual_df)

        # Clean up: remove the created XLSX file
        xlsx_path.unlink()

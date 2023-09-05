import pandas as pd
from src.file_loader.file_loader import Loader
import unittest
import tempfile
import os

class TestLoader(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to store the files
        self.temp_dir = tempfile.mkdtemp()
        self.loader_csv = Loader("data.csv")
        self.loader_parquet = Loader("data.parquet")
        self.loader_xlsx = Loader("data.xlsx")

    def tearDown(self):
        # Clean up: delete temporary directory and its contents
        if os.path.exists(self.temp_dir):
            for root, dirs, files in os.walk(self.temp_dir):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    os.rmdir(os.path.join(root, dir))
            os.rmdir(self.temp_dir)
    def create_temp_csv(self, filename, data):
        # Create a temporary CSV file
        file_path = os.path.join(self.temp_dir, filename)
        with open(file_path, 'w') as csv_file:
            for row in data:
                csv_file.write(','.join(map(str, row)) + '\n')
        return file_path

    def create_temp_xlsx(self, filename, data):
        # You may need to use a library like openpyxl to create XLSX files
        # Here's a simplified example:
        import openpyxl
        file_path = os.path.join(self.temp_dir, filename)
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(file_path)
        return file_path

    def create_temp_parquet(self, filename, data):
        # You may need to use a library like PyArrow or Pandas to create Parquet files
        # Here's a more robust example using PyArrow:
        import pyarrow as pa
        import pyarrow.parquet as pq

        table = pa.Table.from_pandas(data)
        file_path = os.path.join(self.temp_dir, filename)

        # Create a Parquet file writer with a specific schema
        schema = table.schema
        writer = pq.ParquetWriter(file_path, schema)

        try:
            # Write the table to the Parquet file
            writer.write_table(table)
        finally:
            # Close the Parquet writer to ensure the file is properly flushed and closed
            writer.close()

        return file_path

    def test_read_csv(self):
        data = [[1, 'John'], [2, 'Alice'], [3, 'Bob']]
        csv_file = self.create_temp_csv('data.csv', data)
        # Test the _read_csv method
        data = self.loader_csv._read_csv(filepath_or_buffer=csv_file)
        self.assertTrue(isinstance(data, pd.DataFrame))

    def test_read_parquet(self):
        data = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['John', 'Alice', 'Bob']})
        parquet_file = self.create_temp_parquet('data.parquet', data)
        # Test the _read_parquet method
        data = self.loader_parquet._read_parquet(path=parquet_file)
        self.assertTrue(isinstance(data, pd.DataFrame))

    def test_read_xlsx(self):
        data = [['ID', 'Name'], [1, 'John'], [2, 'Alice'], [3, 'Bob']]
        xlsx_file = self.create_temp_xlsx('data.xlsx', data)
        # Test the _read_xlsx method
        data = self.loader_xlsx._read_xlsx(io=xlsx_file)
        self.assertTrue(isinstance(data, pd.DataFrame))

    def test_read_file(self):
        data = [['ID', 'Name'], [1, 'John'], [2, 'Alice'], [3, 'Bob']]

        # Test the read_file method with different file formats
        csv_file = self.create_temp_csv('data.csv', data)
        data_csv = self.loader_csv.read_file(filepath_or_buffer=csv_file)
        self.assertTrue(isinstance(data_csv, pd.DataFrame))

        pdata = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['John', 'Alice', 'Bob']})
        parquet_file = self.create_temp_parquet('data.parquet', pdata)
        data_parquet = self.loader_parquet.read_file(path=parquet_file)
        self.assertTrue(isinstance(data_parquet, pd.DataFrame))

        xlsx_file = self.create_temp_xlsx('data.xlsx', data)
        data_xlsx = self.loader_xlsx.read_file(io=xlsx_file)
        self.assertTrue(isinstance(data_xlsx, pd.DataFrame))

if __name__ == '__main__':
    unittest.main()

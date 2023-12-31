# Code README

## Overview
This Python code provides a `Loader` class that simplifies the process of loading data from various file formats such as CSV, Parquet, and Excel (XLSX) using the pandas library. The code is designed to make it easy to read data from different file formats with a unified interface.

## Prerequisites
Before using this code, make sure you have the following installed:
- Python 3.x
- pandas library

## How to Use
To use the `Loader` class to read data from a file, follow these steps:

1. Import the necessary libraries:
    ```python
    import pandas as pd
    import numpy as np
    ```

2. Create an instance of the `Loader` class by providing the file path as an argument to the constructor:
    ```python
    file_path = "your_data.csv"  # Replace with the path to your data file
    data_loader = Loader(file_path)
    ```

3. Use the `read_file` method to read the data from the specified file. You can pass any keyword arguments that are valid for the corresponding pandas read function (e.g., `pd.read_csv`, `pd.read_parquet`, or `pd.read_excel`):
    ```python
    data = data_loader.read_file()
    ```

4. The `data` variable now contains the loaded data from the file in a pandas DataFrame.

5. You can also specify additional keyword arguments when calling `read_file`. For example:
    ```python
    data = data_loader.read_file(header=0, sep=',')
    ```

## Supported File Formats
The `Loader` class supports the following file formats:
- CSV (Comma-Separated Values)
- Parquet
- Excel (XLSX)

## Error Handling
- If you create a `Loader` instance without providing a file path or with an unsupported file format, it will raise an `AssertionError`.

## Example
Here's an example of how to use the `Loader` class to read a CSV file:

```python
# Import libraries and create a Loader instance
import pandas as pd
import numpy as np
from loader import Loader  # Import the Loader class from your module

file_path = "data.csv"
data_loader = Loader(file_path)

# Read the CSV file
data = data_loader.read_file()

# Now 'data' contains the loaded data in a pandas DataFrame
print(data.head())

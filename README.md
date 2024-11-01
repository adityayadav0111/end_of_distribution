# End of Distribution

`end_of_distribution` is a Python library for detecting outliers in data using common statistical methods. Currently, it includes two methods for outlier detection:
1. **Z-Score Method**: Identifies outliers based on standard deviations from the mean.
2. **Interquartile Range (IQR) Method**: Identifies outliers based on the interquartile range.

## Features

- Detect outliers using Z-score and IQR methods
- Easy integration with other Python projects
- Clear and simple API for outlier detection in any dataset

## Installation

1. **Clone the Repository**: First, clone the repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/end_of_distribution.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd end_of_distribution
   ```

## Usage

1. **Import the Library Functions**: In your Python script, import the `z_score_outliers` and `iqr_outliers` functions from the library.

2. **Example Code**:
   ```python
   from lib.end_of_distribution import z_score_outliers, iqr_outliers

   # Example dataset with a clear outlier
   data = [1, 2, 3, 4, 100, 5]

   # Detect outliers using Z-score method
   z_score_results = z_score_outliers(data)
   print("Z-score outliers detected:", z_score_results)

   # Detect outliers using IQR method
   iqr_results = iqr_outliers(data)
   print("IQR outliers detected:", iqr_results)
   ```

   This will output a boolean list indicating whether each data point is an outlier.

## API Reference

### z_score_outliers(data, threshold=3)

- **Parameters**:
  - `data` (list): List of numerical data points.
  - `threshold` (float): Threshold for Z-score (default is 3).

- **Returns**: List of booleans indicating outliers.

### iqr_outliers(data)

- **Parameters**:
  - `data` (list): List of numerical data points.

- **Returns**: List of booleans indicating outliers.

## Contributing

1. Fork the repository and clone it locally.
2. Create a new branch for your changes.
3. Commit your changes and push them to your branch.
4. Open a pull request to the main branch of this repository.

We welcome all contributions to make `end_of_distribution` better!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

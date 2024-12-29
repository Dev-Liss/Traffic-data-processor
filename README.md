# Traffic Analysis System

## Overview
This traffic analysis system is a Python application designed to process and visualize traffic data from multiple junctions. The program analyzes vehicular movement patterns, generates statistical reports, and displays the data through interactive histograms.

## Features

### Input Validation
- Accepts date input in DD MM YYYY format
- Validates input for correct data types and ranges
- Ensures dates fall within the valid range (2000-2024)

### Data Processing
- Calculates comprehensive traffic statistics including:
  - Total vehicle counts
  - Vehicle type distributions
  - Electric vehicle counts
  - Speed limit violation tracking
  - Directional movement analysis
  - Weather condition impacts
- Processes data from two major junctions:
  - Elm Avenue/Rabbit Road
  - Hanley Highway/Westway

### Data Visualization
- Interactive histogram display using Tkinter
- Dual-junction comparison with color-coded bars
- Hourly traffic distribution visualization
- Clear legends and axis labels
- Dynamic scaling based on traffic volumes

### Results Management
- Automatic saving of analysis results to a text file
- Supports multiple dataset analysis in a single session
- Appends new results to existing records

### Error Handling
- Robust file existence verification
- Data format validation
- Empty file detection
- Graceful error recovery with user prompts

## Technical Requirements
- Python 3.x
- Tkinter (included in standard Python distribution)
- Required file structure:
  - CSV files named in format: `traffic_dataXXXXXXXX.csv` (where X represents date digits)
  - Output file: `results.txt` (created automatically)

## Usage Instructions

1. Run the program:
   ```python
   python Traffic_Data_Processor.py
   ```

2. Enter the date for analysis:
   - Day (DD): 1-31
   - Month (MM): 1-12
   - Year (YYYY): 2000-2024

3. Review the analysis results:
   - Statistical data will be displayed in the console
   - A histogram will appear in a separate window
   - Results are automatically saved to results.txt

4. Choose to analyze another date or exit:
   - Enter 'Y' to process another dataset
   - Enter 'N' to terminate the program

## Class Structure

### MultiCSVProcessor
- Main class handling the program flow
- Manages file loading and data processing
- Controls user interaction flow

### HistogramApp
- Manages the visualization component
- Creates and controls the Tkinter window
- Renders the traffic data histogram

## Error Handling Features
- File not found errors
- Data format validation
- Empty file detection
- Invalid date inputs
- Type conversion errors

## Output Files
The program generates and maintains a `results.txt` file containing:
- Detailed traffic statistics
- Analysis timestamps
- Cumulative data from multiple sessions

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Author
DEV-Liss

## License
This project is available for educational purposes. Please get in touch with the author for any other usage.

## Acknowledgements
Special thanks to the referenced sources that guided specific implementation details. All references are properly documented in the source code.

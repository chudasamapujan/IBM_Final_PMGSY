# Data Directory

This directory contains the datasets used for the Infrastructure Prediction Dashboard project.

## Structure

- `raw/` - Original, unprocessed data files
- `processed/` - Cleaned and preprocessed data ready for analysis
- `sample/` - Sample datasets for testing and demonstration

## Data Description

### Infrastructure Data Variables

1. **Road_Works_Sanctioned**: Number of road construction projects approved
2. **Bridges_Sanctioned**: Number of bridge construction projects approved  
3. **Road_Works_Completed**: Number of road projects completed
4. **Bridges_Completed**: Number of bridge projects completed
5. **Bridges_Balance**: Number of bridge projects in progress

### Time Series Format

The data follows a monthly time series format with the following columns:
- Year: Calendar year (2020-2022)
- Month: Month number (1-12)
- Various infrastructure metrics as described above

## Usage

### For AutoAI Training
1. Place your training data in the `raw/` directory
2. Use the AutoAI notebook to preprocess and train models
3. Processed data will be saved to `processed/`

### For Dashboard Testing
Use the sample data in `sample/infrastructure_sample.csv` for testing the dashboard functionality without requiring the full AutoAI setup.

## Data Privacy

- Ensure all data files are properly anonymized
- Do not commit sensitive or proprietary data to version control
- Use sample data for public demonstrations

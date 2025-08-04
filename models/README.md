# Infrastructure Prediction Models

This directory contains trained models and model-related files for the Infrastructure Prediction Dashboard.

## Contents

- Trained AutoAI models (`.tar.gz` files)
- Model metadata and configuration files
- Model evaluation reports
- Deployment artifacts

## Model Information

### AutoAI Time Series Model
- **Framework**: IBM Watson AutoAI
- **Type**: Time Series Forecasting
- **Target Variables**: Infrastructure project metrics
- **Input Features**: Historical infrastructure data
- **Training Period**: 2020-2022

### Usage

1. **Training**: Use the AutoAI experiment notebook in `notebooks/`
2. **Deployment**: Models are loaded automatically by the dashboard
3. **Updates**: Retrain models with new data using the notebook

## File Naming Convention

- `autoai_model_YYYYMMDD.tar.gz` - Trained AutoAI models with date
- `model_config.json` - Model configuration and metadata
- `evaluation_report_YYYYMMDD.pdf` - Model performance reports

## Integration

The dashboard loads models using the `model_integration.py` module in the dashboard directory. Models are automatically detected and loaded at startup.

## Backup

Keep backup copies of production models before updating with new versions.

# Infrastructure Prediction Dashboard

A modern web-based frontend for IBM Watson AutoAI time series prediction models, specifically designed for infrastructure project forecasting.

## Features

- **Interactive Prediction Interface**: Enter infrastructure project parameters and get AI-powered forecasts
- **Historical Data Analytics**: Visualize historical trends with interactive charts
- **Model Information Dashboard**: View detailed model metrics and performance indicators
- **Responsive Design**: Modern, mobile-friendly interface with IBM design language
- **Real-time Predictions**: Get instant predictions with confidence intervals

## Project Structure

```
frontend/
├── app.py                 # Main Flask application
├── model_integration.py   # AutoAI model integration module
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
└── static/               # Static assets (CSS, JS, images)
```

## Prediction Variables

The model forecasts the following infrastructure metrics:

- **Road Work Sanctioned**: Number of road projects approved
- **Bridges Sanctioned**: Number of bridge projects approved
- **Road Works Completed**: Number of road projects finished
- **Bridges Completed**: Number of bridge projects finished
- **Bridges Balance**: Number of pending bridge projects

## Input Parameters

- Road Work Sanctioned (count)
- Bridges Sanctioned (count)
- Road Length Sanctioned (km)
- Cost of Works Sanctioned (₹)
- Road Length Completed (km)
- Expenditure Occurred (₹)
- Road Works Balance (count)

## Installation

### Quick Start (Recommended)

If you're experiencing dependency issues, use the simplified version:

1. **Windows users:**
   ```cmd
   start_simple.bat
   ```

2. **Manual installation:**
   ```bash
   pip install Flask
   python app_simple.py
   ```

3. **Access the dashboard:**
   Open your browser and navigate to `http://localhost:5000`

### Full Installation

For the complete version with all features:

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **If you get errors:** See `TROUBLESHOOTING.md` for solutions

### Troubleshooting

❌ **Getting terminal errors?** Use the simplified version:
- Run `start_simple.bat` (Windows) or `python app_simple.py`
- This uses minimal dependencies and mock data
- Perfect for testing the interface before model integration

📖 **Detailed help:** Check `TROUBLESHOOTING.md` for comprehensive error solutions

## Model Integration

To integrate with your actual AutoAI model:

1. **Update the model_integration.py file:**
   - Replace the mock prediction functions with actual model loading code
   - Configure your IBM Watson credentials
   - Set up the experiment metadata from your notebook

2. **Example integration:**
   ```python
   from ibm_watsonx_ai.experiment import AutoAI
   from model_integration import integrate_with_notebook_model
   
   # Use your credentials and experiment metadata
   model_wrapper = integrate_with_notebook_model(credentials, experiment_metadata)
   ```

## Configuration

### Environment Variables

Create a `.env` file with your configuration:

```bash
WATSON_API_KEY=your_api_key_here
WATSON_PROJECT_ID=your_project_id_here
WATSON_DEPLOYMENT_URL=https://eu-gb.ml.cloud.ibm.com
MODEL_PATH=path/to/your/model
```

### Model Configuration

The application expects the following model structure from your AutoAI notebook:

- **Prediction Type**: Time Series
- **Forecast Window**: 1 period
- **Lookback Window**: 10 periods
- **Target Variables**: 5 infrastructure metrics
- **Feature Variables**: 10 input parameters

## Usage

### Making Predictions

1. Navigate to the **"Make Prediction"** tab
2. Enter your infrastructure project parameters
3. Click **"Generate Predictions"**
4. View forecasted values with confidence intervals

### Viewing Analytics

1. Go to the **"Historical Analytics"** tab
2. Click **"Load Historical Data"**
3. Explore interactive time series charts
4. Analyze trends and patterns

### Model Information

1. Access the **"Model Information"** tab
2. Review model details and performance metrics
3. Check deployment status and accuracy measures

## API Endpoints

- `POST /predict` - Generate predictions
- `GET /historical_data` - Retrieve historical data and charts
- `GET /model_info` - Get model information and metrics

## Customization

### Styling

The application uses Bootstrap 5 with custom CSS variables for IBM design language:

```css
:root {
    --primary-color: #0645FF;
    --secondary-color: #AB74FF;
    --accent-color: #2A4FFF;
}
```

### Adding New Features

1. **New Input Parameters**: Update the form in `index.html` and the prediction logic in `app.py`
2. **Additional Charts**: Extend the analytics section with new visualizations
3. **Model Metrics**: Add more performance indicators in the model information tab

## Deployment

### Local Development

```bash
python app.py
```

### Production Deployment

For production deployment, consider using:

- **Gunicorn**: `gunicorn --bind 0.0.0.0:5000 app:app`
- **Docker**: Create a Dockerfile for containerized deployment
- **Cloud Platforms**: Deploy to IBM Cloud, AWS, or Azure

## Performance Considerations

- **Caching**: Implement Redis for caching predictions and historical data
- **Load Balancing**: Use multiple application instances for high traffic
- **Database**: Add a database for storing prediction history and user sessions

## Security

- **Authentication**: Add user authentication for production use
- **API Security**: Implement rate limiting and input validation
- **HTTPS**: Use SSL/TLS encryption for production deployment

## Troubleshooting

### Common Issues

1. **Model Loading Errors**: Check your IBM Watson credentials and project access
2. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Port Conflicts**: Change the port in `app.py` if 5000 is already in use

### Debug Mode

Enable Flask debug mode for development:

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the IBM License Agreement for Non-Warranted Programs.

## Support

For support and questions:

- Check the [IBM Watson Documentation](https://cloud.ibm.com/docs/watson-machine-learning)
- Review the [AutoAI Documentation](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/autoai-overview.html)
- Contact your IBM Watson support team

"""
Simplified Flask application for Infrastructure Prediction Dashboard
This version uses minimal dependencies and mock data to avoid import errors.
"""

from flask import Flask, render_template, request, jsonify
import json
import random
import datetime
from typing import Dict, List, Any

app = Flask(__name__)

# Mock data and functions
def generate_mock_prediction(input_data: Dict[str, float]) -> Dict[str, Any]:
    """Generate mock predictions based on input data"""
    
    # Base predictions with some logic based on inputs
    road_work_base = input_data.get('NO_OF_ROAD_WORK_SANCTIONED', 100)
    bridges_base = input_data.get('NO_OF_BRIDGES_SANCTIONED', 25)
    
    # Add some variation and trends
    predictions = {
        'NO_OF_ROAD_WORK_SANCTIONED': max(50, int(road_work_base * random.uniform(0.9, 1.1))),
        'NO_OF_BRIDGES_SANCTIONED': max(10, int(bridges_base * random.uniform(0.8, 1.2))),
        'NO_OF_ROAD_WORKS_COMPLETED': max(30, int(road_work_base * 0.8 * random.uniform(0.9, 1.1))),
        'NO_OF_BRIDGES_COMPLETED': max(5, int(bridges_base * 0.75 * random.uniform(0.8, 1.2))),
        'NO_OF_BRIDGES_BALANCE': max(0, int(bridges_base * 0.2 * random.uniform(0.5, 1.5)))
    }
    
    # Generate confidence intervals
    confidence_intervals = {}
    for key, value in predictions.items():
        confidence_intervals[key] = {
            'lower': max(0, int(value * 0.85)),
            'upper': int(value * 1.15)
        }
    
    return {
        'predictions': predictions,
        'confidence_intervals': confidence_intervals,
        'model_version': '1.0.0',
        'prediction_timestamp': datetime.datetime.now().isoformat()
    }

def generate_mock_historical_data() -> List[Dict]:
    """Generate mock historical data for charts"""
    data = []
    base_date = datetime.datetime(2023, 1, 1)
    
    for i in range(24):  # 24 months of data
        date = base_date + datetime.timedelta(days=30 * i)
        
        # Generate realistic trends
        trend = i * 2  # Growing trend
        seasonal = 10 * (1 + 0.5 * (i % 12) / 12)  # Seasonal variation
        noise = random.randint(-15, 15)
        
        data.append({
            'date': date.strftime('%Y-%m-%d'),
            'NO_OF_ROAD_WORK_SANCTIONED': max(50, 120 + trend + seasonal + noise),
            'NO_OF_BRIDGES_SANCTIONED': max(10, 25 + trend//2 + seasonal//2 + noise//2),
            'NO_OF_ROAD_WORKS_COMPLETED': max(30, 95 + trend + seasonal * 0.8 + noise),
            'NO_OF_BRIDGES_COMPLETED': max(5, 20 + trend//3 + seasonal//3 + noise//3),
            'NO_OF_BRIDGES_BALANCE': max(0, 8 + trend//4 + seasonal//4 + noise//4)
        })
    
    return data

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        # Extract input data from form
        input_data = {}
        
        # Required fields mapping
        field_mapping = {
            'road_work_sanctioned': 'NO_OF_ROAD_WORK_SANCTIONED',
            'bridges_sanctioned': 'NO_OF_BRIDGES_SANCTIONED',
            'length_road_sanctioned': 'LENGTH_OF_ROAD_WORK_SANCTIONED',
            'cost_sanctioned': 'COST_OF_WORKS_SANCTIONED',
            'length_road_completed': 'LENGTH_OF_ROAD_WORK_COMPLETED',
            'expenditure': 'EXPENDITURE_OCCURED',
            'road_works_balance': 'NO_OF_ROAD_WORKS_BALANCE'
        }
        
        # Extract and validate data
        for form_field, feature_name in field_mapping.items():
            value = request.form.get(form_field, '0')
            try:
                input_data[feature_name] = float(value)
            except (ValueError, TypeError):
                input_data[feature_name] = 0.0
        
        # Generate prediction
        result = generate_mock_prediction(input_data)
        
        return jsonify({
            'success': True,
            **result,
            'input_data': input_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/historical_data')
def get_historical_data():
    """API endpoint to get historical data"""
    try:
        data = generate_mock_historical_data()
        
        # Create a simple plot structure (without plotly dependency)
        plot_data = {
            'data': [],
            'layout': {
                'title': 'Infrastructure Projects Historical Trends',
                'xaxis': {'title': 'Date'},
                'yaxis': {'title': 'Count'}
            }
        }
        
        # Add traces for each metric
        metrics = [
            ('NO_OF_ROAD_WORK_SANCTIONED', 'Road Work Sanctioned'),
            ('NO_OF_BRIDGES_SANCTIONED', 'Bridges Sanctioned'),
            ('NO_OF_ROAD_WORKS_COMPLETED', 'Road Works Completed'),
            ('NO_OF_BRIDGES_COMPLETED', 'Bridges Completed'),
            ('NO_OF_BRIDGES_BALANCE', 'Bridges Balance')
        ]
        
        for metric_key, metric_name in metrics:
            x_values = [item['date'] for item in data]
            y_values = [item[metric_key] for item in data]
            
            plot_data['data'].append({
                'x': x_values,
                'y': y_values,
                'type': 'scatter',
                'mode': 'lines+markers',
                'name': metric_name
            })
        
        return jsonify({
            'plot': json.dumps(plot_data),
            'data': data
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/model_info')
def model_info():
    """API endpoint to get model information"""
    try:
        model_info_data = {
            'model_type': 'Time Series Forecasting',
            'algorithm': 'IBM Watson AutoAI (Mock)',
            'prediction_window': 1,
            'lookback_window': 10,
            'features': [
                'NO_OF_ROAD_WORK_SANCTIONED',
                'NO_OF_BRIDGES_SANCTIONED',
                'LENGTH_OF_ROAD_WORK_SANCTIONED',
                'COST_OF_WORKS_SANCTIONED',
                'LENGTH_OF_ROAD_WORK_COMPLETED',
                'EXPENDITURE_OCCURED',
                'NO_OF_ROAD_WORKS_BALANCE'
            ],
            'target_variables': [
                'NO_OF_ROAD_WORK_SANCTIONED',
                'NO_OF_BRIDGES_SANCTIONED',
                'NO_OF_ROAD_WORKS_COMPLETED',
                'NO_OF_BRIDGES_COMPLETED',
                'NO_OF_BRIDGES_BALANCE'
            ],
            'deployment_status': 'Mock Mode - Ready for Integration',
            'last_updated': '2024-08-04',
            'accuracy_metrics': {
                'SMAPE': '12.5%',
                'MAE': '8.3',
                'RMSE': '15.7',
                'R²': '0.876'
            },
            'model_loaded': False,
            'using_mock_data': True
        }
        
        return jsonify(model_info_data)
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': False,
        'using_mock_data': True,
        'timestamp': datetime.datetime.now().isoformat()
    })

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("🌟 Starting Infrastructure Prediction Dashboard (Simplified)...")
    print("📊 Dashboard will be available at: http://localhost:5000")
    print("⚠️  Currently using mock predictions - integrate with your AutoAI model for real predictions")
    print("🔗 Available endpoints:")
    print("   - GET  /           - Main dashboard")
    print("   - POST /predict    - Make predictions")
    print("   - GET  /historical_data - Historical data")
    print("   - GET  /model_info - Model information")
    print("   - GET  /health     - Health check")
    print("\n💡 Press Ctrl+C to stop the server\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)

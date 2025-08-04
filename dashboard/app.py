from flask import Flask, render_template, request, jsonify, send_from_directory
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.utils
import json
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Mock prediction function - Replace this with your actual model integration
def make_prediction(input_data):
    """
    Mock prediction function that simulates the AutoAI model.
    Replace this with actual model integration from your notebook.
    """
    # Simulate predictions based on input trends
    base_values = {
        'NO_OF_ROAD_WORK_SANCTIONED': np.random.randint(50, 200),
        'NO_OF_BRIDGES_SANCTIONED': np.random.randint(10, 50),
        'NO_OF_ROAD_WORKS_COMPLETED': np.random.randint(30, 150),
        'NO_OF_BRIDGES_COMPLETED': np.random.randint(5, 40),
        'NO_OF_BRIDGES_BALANCE': np.random.randint(5, 30)
    }
    
    # Add some variation based on input
    for key in base_values:
        if key in input_data:
            # Simulate trend continuation
            trend_factor = 0.1 * (input_data[key] - 100) / 100
            base_values[key] = int(base_values[key] * (1 + trend_factor))
    
    return base_values

def generate_historical_data():
    """Generate mock historical data for visualization"""
    dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='M')
    
    data = {
        'date': dates,
        'NO_OF_ROAD_WORK_SANCTIONED': np.random.randint(80, 180, len(dates)),
        'NO_OF_BRIDGES_SANCTIONED': np.random.randint(15, 45, len(dates)),
        'NO_OF_ROAD_WORKS_COMPLETED': np.random.randint(60, 160, len(dates)),
        'NO_OF_BRIDGES_COMPLETED': np.random.randint(10, 35, len(dates)),
        'NO_OF_BRIDGES_BALANCE': np.random.randint(5, 25, len(dates))
    }
    
    return pd.DataFrame(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        input_data = {
            'NO_OF_ROAD_WORK_SANCTIONED': float(request.form.get('road_work_sanctioned', 100)),
            'NO_OF_BRIDGES_SANCTIONED': float(request.form.get('bridges_sanctioned', 25)),
            'LENGTH_OF_ROAD_WORK_SANCTIONED': float(request.form.get('length_road_sanctioned', 1000)),
            'COST_OF_WORKS_SANCTIONED': float(request.form.get('cost_sanctioned', 50000)),
            'LENGTH_OF_ROAD_WORK_COMPLETED': float(request.form.get('length_road_completed', 800)),
            'EXPENDITURE_OCCURED': float(request.form.get('expenditure', 40000)),
            'NO_OF_ROAD_WORKS_BALANCE': float(request.form.get('road_works_balance', 20))
        }
        
        # Make prediction
        predictions = make_prediction(input_data)
        
        # Generate confidence intervals (mock)
        confidence_intervals = {}
        for key, value in predictions.items():
            confidence_intervals[key] = {
                'lower': max(0, int(value * 0.85)),
                'upper': int(value * 1.15)
            }
        
        return jsonify({
            'success': True,
            'predictions': predictions,
            'confidence_intervals': confidence_intervals,
            'input_data': input_data
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/historical_data')
def get_historical_data():
    """API endpoint to get historical data for charts"""
    df = generate_historical_data()
    
    # Create interactive plot
    fig = go.Figure()
    
    # Add traces for each prediction column
    prediction_columns = [
        'NO_OF_ROAD_WORK_SANCTIONED',
        'NO_OF_BRIDGES_SANCTIONED', 
        'NO_OF_ROAD_WORKS_COMPLETED',
        'NO_OF_BRIDGES_COMPLETED',
        'NO_OF_BRIDGES_BALANCE'
    ]
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    for i, col in enumerate(prediction_columns):
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df[col],
            mode='lines+markers',
            name=col.replace('_', ' ').title(),
            line=dict(color=colors[i], width=2),
            marker=dict(size=6)
        ))
    
    fig.update_layout(
        title='Historical Infrastructure Data Trends',
        xaxis_title='Date',
        yaxis_title='Count',
        hovermode='x unified',
        template='plotly_white',
        height=500
    )
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return jsonify({
        'plot': graphJSON,
        'data': df.to_dict('records')
    })

@app.route('/model_info')
def model_info():
    """API endpoint to get model information"""
    model_info = {
        'model_type': 'Time Series Forecasting',
        'algorithm': 'AutoAI Ensemble',
        'prediction_window': 1,
        'lookback_window': 10,
        'features': [
            'NO_OF_ROAD_WORK_SANCTIONED',
            'NO_OF_BRIDGES_SANCTIONED',
            'NO_OF_ROAD_WORKS_COMPLETED',
            'NO_OF_BRIDGES_COMPLETED',
            'NO_OF_BRIDGES_BALANCE',
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
        'deployment_status': 'Active',
        'last_updated': '2024-08-04',
        'accuracy_metrics': {
            'SMAPE': '12.5%',
            'MAE': '8.3',
            'RMSE': '15.7'
        }
    }
    
    return jsonify(model_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

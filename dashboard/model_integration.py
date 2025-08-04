"""
Model Integration Module for IBM Watson AutoAI

This module integrates the trained AutoAI model with the Flask web application.
Replace the mock functions with actual model loading and prediction code.
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, List
import pickle
import os

class AutoAIModelWrapper:
    """Wrapper class for the AutoAI model integration"""
    
    def __init__(self, model_path: str = None):
        """
        Initialize the model wrapper
        
        Args:
            model_path: Path to the saved AutoAI model
        """
        self.model = None
        self.model_path = model_path
        self.is_loaded = False
        
        # Feature columns as defined in the notebook
        self.feature_columns = [
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
        ]
        
        # Target columns as defined in the notebook
        self.target_columns = [
            'NO_OF_ROAD_WORK_SANCTIONED',
            'NO_OF_BRIDGES_SANCTIONED',
            'NO_OF_ROAD_WORKS_COMPLETED',
            'NO_OF_BRIDGES_COMPLETED',
            'NO_OF_BRIDGES_BALANCE'
        ]
        
    def load_model(self):
        """
        Load the trained AutoAI model
        
        This should be replaced with actual model loading code from your notebook.
        You would typically load the pipeline_model from your AutoAI experiment.
        """
        try:
            if self.model_path and os.path.exists(self.model_path):
                # Replace this with actual model loading
                # Example:
                # from ibm_watsonx_ai.experiment import AutoAI
                # pipeline_optimizer = AutoAI(credentials, project_id=project_id).runs.get_optimizer(metadata=experiment_metadata)
                # self.model = pipeline_optimizer.get_pipeline()
                
                # For now, using a placeholder
                self.model = None
                self.is_loaded = True
                print(f"Model loaded from {self.model_path}")
            else:
                print("Model path not provided or file doesn't exist. Using mock predictions.")
                self.is_loaded = False
                
        except Exception as e:
            print(f"Error loading model: {e}")
            self.is_loaded = False
    
    def preprocess_input(self, input_data: Dict[str, float]) -> pd.DataFrame:
        """
        Preprocess input data for prediction
        
        Args:
            input_data: Dictionary containing input features
            
        Returns:
            Preprocessed pandas DataFrame
        """
        # Create DataFrame with feature columns
        df = pd.DataFrame([input_data])
        
        # Ensure all required columns are present
        for col in self.feature_columns:
            if col not in df.columns:
                df[col] = 0  # Default value for missing features
        
        # Reorder columns to match training data
        df = df[self.feature_columns]
        
        return df
    
    def predict(self, input_data: Dict[str, float]) -> Dict[str, Any]:
        """
        Make predictions using the loaded model
        
        Args:
            input_data: Dictionary containing input features
            
        Returns:
            Dictionary containing predictions and confidence intervals
        """
        if not self.is_loaded or self.model is None:
            return self._mock_prediction(input_data)
        
        try:
            # Preprocess input
            processed_data = self.preprocess_input(input_data)
            
            # Make prediction using the actual model
            # Replace this with actual prediction code
            # predictions = self.model.predict(processed_data)
            
            # For now, return mock predictions
            return self._mock_prediction(input_data)
            
        except Exception as e:
            print(f"Error making prediction: {e}")
            return self._mock_prediction(input_data)
    
    def _mock_prediction(self, input_data: Dict[str, float]) -> Dict[str, Any]:
        """
        Generate mock predictions for demonstration
        Replace this with actual model predictions
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
                base_values[key] = max(0, int(base_values[key] * (1 + trend_factor)))
        
        # Generate confidence intervals
        confidence_intervals = {}
        for key, value in base_values.items():
            confidence_intervals[key] = {
                'lower': max(0, int(value * 0.85)),
                'upper': int(value * 1.15)
            }
        
        return {
            'predictions': base_values,
            'confidence_intervals': confidence_intervals,
            'model_version': '1.0.0',
            'prediction_timestamp': pd.Timestamp.now().isoformat()
        }
    
    def get_feature_importance(self) -> Dict[str, float]:
        """
        Get feature importance scores from the model
        
        Returns:
            Dictionary mapping feature names to importance scores
        """
        if not self.is_loaded or self.model is None:
            # Mock feature importance
            return {
                'NO_OF_ROAD_WORK_SANCTIONED': 0.25,
                'LENGTH_OF_ROAD_WORK_SANCTIONED': 0.20,
                'COST_OF_WORKS_SANCTIONED': 0.18,
                'NO_OF_BRIDGES_SANCTIONED': 0.15,
                'EXPENDITURE_OCCURED': 0.12,
                'LENGTH_OF_ROAD_WORK_COMPLETED': 0.10
            }
        
        try:
            # Extract feature importance from actual model
            # This depends on the specific AutoAI pipeline structure
            # return self.model.get_feature_importance()
            pass
        except Exception as e:
            print(f"Error getting feature importance: {e}")
            return {}


def integrate_with_notebook_model(credentials, experiment_metadata):
    """
    Function to integrate with the actual AutoAI model from the notebook
    
    Args:
        credentials: IBM Watson credentials
        experiment_metadata: Experiment metadata from the notebook
        
    Returns:
        AutoAIModelWrapper instance with loaded model
    """
    try:
        # Import necessary modules from the notebook
        from ibm_watsonx_ai.experiment import AutoAI
        
        # Get the fitted optimizer (as shown in the notebook)
        pipeline_optimizer = AutoAI(
            credentials, 
            project_id=experiment_metadata['project_id']
        ).runs.get_optimizer(metadata=experiment_metadata)
        
        # Create model wrapper
        model_wrapper = AutoAIModelWrapper()
        
        # Load the best pipeline
        model_wrapper.model = pipeline_optimizer.get_pipeline()
        model_wrapper.is_loaded = True
        
        print("Successfully integrated with AutoAI model from notebook")
        return model_wrapper
        
    except Exception as e:
        print(f"Error integrating with notebook model: {e}")
        print("Falling back to mock predictions")
        return AutoAIModelWrapper()


# Global model instance
model_instance = None

def get_model_instance():
    """Get or create the global model instance"""
    global model_instance
    if model_instance is None:
        model_instance = AutoAIModelWrapper()
    return model_instance

# Imports
import joblib
import pandas as pd

# Load the Model

def load_model():
    """
    Load the trained house price prediction pipeline.
    """
    model = joblib.load("models/house_price_pipeline.pkl")
    return model

# Load the defualt value, median(numerical data), mode(categorical data)
def load_default_values():
    return joblib.load("models/default_values.pkl")


# Drop Down Options

def load_dropdown_options():
    """
    Load dropdown options for categorical features.
    """
    return joblib.load("models/dropdown_options.pkl")

# User Inputs

def create_input_dataframe(user_inputs):
    """
    Create a complete input DataFrame for prediction.
    Missing features are filled using default values.
    """

    # Load default values
    input_data = load_default_values()

    # Update with user inputs
    input_data.update(user_inputs)

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    return input_df


# prediction function

def predict_price(model, input_df):
    """
    Predict the house price.
    """
    prediction = model.predict(input_df)
    return prediction[0]

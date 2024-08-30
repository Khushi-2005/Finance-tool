
   import pandas as pd

def preprocess(data):
    """
    Preprocess the input DataFrame:
    - Convert 'Date' column to datetime
    - Extract 'Month' and 'Day_of_Week' from 'Date'
    """
    # Ensure 'Date' column is in datetime format
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

    # Extract month and day of the week from 'Date'
    data['Month'] = data['Date'].dt.month_name()
    data['Day_of_Week'] = data['Date'].dt.day_name()

    return data

    
    
    
    


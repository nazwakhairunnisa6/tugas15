import pandas as pd
import os

def load_data():
    csv_path = os.path.join('data', 'film.csv')
    return pd.read_csv(csv_path)

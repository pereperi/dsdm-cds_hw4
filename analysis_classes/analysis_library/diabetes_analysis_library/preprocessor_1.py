import pandas as pd

class preprocessor_remove:

    def preprocess_data_remove(data):
        # Remove rows with NaN values in specific columns
        data = data.dropna(subset=['age', 'gender', 'ethnicity'])
        return data
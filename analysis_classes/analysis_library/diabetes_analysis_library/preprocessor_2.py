import pandas as pd

class preprocessor_mean:

    def preprocess_data(data):
        # Fill NaN with mean values in specific columns
        data['height'] = data['height'].fillna(data['height'].mean())
        data['weight'] = data['weight'].fillna(data['weight'].mean())
        return data

    
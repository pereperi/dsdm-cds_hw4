class Preprocessor_Mean:

    def __init__(self, data):
        self.data = data
        self.preprocess_data_mean(self.data)

    def preprocess_data(data):
        # Fill NaN with mean values in specific columns
        data['height'] = data['height'].fillna(data['height'].mean())
        data['weight'] = data['weight'].fillna(data['weight'].mean())
        return data

    
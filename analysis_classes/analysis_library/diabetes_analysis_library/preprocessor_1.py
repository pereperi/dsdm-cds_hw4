class Preprocessor_Remove:

    def __init__(self, data):
        self.data = data
        self.preprocess_data_remove(self.data)

    def preprocess_data_remove(data):
        # Remove rows with NaN values in specific columns
        data = data.dropna(subset=['age', 'gender', 'ethnicity'])
        return data
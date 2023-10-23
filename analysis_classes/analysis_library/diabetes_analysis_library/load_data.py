import pandas as pd
from sklearn.model_selection import train_test_split

class Loader:

    def __init__(self,file_path, test_size=0.2, random_state=42):
        self.file_path = file_path
        self.test_size = test_size
        self.random_state = random_state
        self.load_data(self.file_path, self.test_size, self.random_state)
        
        
    def load_data(file_path, test_size=0.2, random_state=42):
        data = pd.read_csv(file_path)
        X_train, X_test = train_test_split(data, test_size=test_size, random_state=random_state)
        return X_train, X_test
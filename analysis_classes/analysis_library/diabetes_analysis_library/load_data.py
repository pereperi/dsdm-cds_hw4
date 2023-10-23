import pandas as pd
from sklearn.model_selection import train_test_split

class loader:

    def load_data(file_path, test_size=0.2, random_state=42):
        data = pd.read_csv(file_path)
        X_train, X_test = train_test_split(data, test_size=test_size, random_state=random_state)
        return X_train, X_test
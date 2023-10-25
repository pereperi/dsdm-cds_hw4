#Using Logistic Regression from Sklearn
from sklearn.linear_model import LogisticRegression

class Model:
    def __init__(self, feature_columns, target_column, model_hyperparams=None):
        self._feature_columns = feature_columns
        self._target_column = target_column
        self._model_hyperparams = model_hyperparams if model_hyperparams else {}
        self.model = None

    def train(self, train_data):
        X_train = train_data[self._feature_columns]
        y_train = train_data[self._target_column]
        
        self.model = LogisticRegression(**self._model_hyperparams)
        self.model.fit(X_train, y_train)

    def predict(self, data):
        if not self.model:
            raise ValueError("Model has not been trained yet!")
        
        X = data[self._feature_columns]
        return self.model.predict_proba(X)[:, 1]

# Example usage:
feature_cols = ['height', 'weight', 'age', 'aids', 'cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
target_col = 'diabetes_mellitus'

# Initialize the model with features, target, and hyperparameters
model_instance = Model(feature_cols, target_col, {'max_iter': 1000})

# Train the model
# train_data should be a pandas DataFrame with the specified feature and target columns
#model_instance.train(train_data)

# Predict
# test_data should be a pandas DataFrame with the specified feature columns
#test_predictions = model_instance.predict(test_data)

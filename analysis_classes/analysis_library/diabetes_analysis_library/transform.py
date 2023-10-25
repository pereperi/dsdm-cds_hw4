from abc import ABCMeta, abstractmethod
import pandas as pd

class Transform(metaclass=ABCMeta):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def transform(self,data):
        return NotImplementedError
    
class Ethnicity(Transform):

    def transform(self,data):
        data = pd.get_dummies(data, columns=['ethnicity'], prefix='ethnicity')
        return data

class Gender(Transform):

    def transform(self,data):
        data['gender'] = data['gender'].apply(lambda x: 1 if x == 'M' else 0)
        return data

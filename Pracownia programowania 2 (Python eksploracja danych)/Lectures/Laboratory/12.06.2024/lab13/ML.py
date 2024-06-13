from __future__ import annotations
from abc import ABC, abstractmethod
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
import pandas as pd


class Algorithm(ABC):

    def __init__(self, target, factors, df):
        self.target = target
        self.factors = factors
        self.df = df
        self.test = self.get_df().sample(frac=0.3)
        self.train = self.get_df().drop(self.test.index)
        self.model = self.create_model()

    def get_result(self):
        return self.model.predict(self.test[self.factors])

    def get_accuracy(self):
        return accuracy_score(self.get_result(), self.test[self.target])

    def get_precision(self):
        return precision_score(self.get_result(), self.test[self.target])

    def get_df(self) -> pd.DataFrame:
        return self.df

    def predict(self):
        return self.model.predict(self.test[self.target])

    def print_information(self, name_model):
        print(f'Model: {name_model}')
        print(f'Accuracy: {self.get_accuracy()}')
        print(f'Precision: {self.get_precision()}')
        print()

    @abstractmethod
    def create_model(self):
        raise NotImplementedError


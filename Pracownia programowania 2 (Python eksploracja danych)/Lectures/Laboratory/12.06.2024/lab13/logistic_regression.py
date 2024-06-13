from ML import Algorithm
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt


class LR(Algorithm):
    def create_model(self):
        model = LogisticRegression()
        model.fit(self.train[self.factors], self.train[self.target])
        return model


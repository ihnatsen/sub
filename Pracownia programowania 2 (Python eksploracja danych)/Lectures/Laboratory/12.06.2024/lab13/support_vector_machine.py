from ML import Algorithm
from sklearn import svm
from matplotlib import pyplot as plt


class SVC(Algorithm):
    def create_model(self):
        model = svm.SVC()
        model.fit(self.train[self.factors], self.train[self.target])
        return model


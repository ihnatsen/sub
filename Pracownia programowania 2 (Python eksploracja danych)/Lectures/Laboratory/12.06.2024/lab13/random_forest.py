from ML import Algorithm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt


class RF(Algorithm):

    def __init__(self, target, factors, df, max_depth):
        self.max_depth = max_depth
        super().__init__(target, factors, df)

    def print_information(self, name_model):
        super().print_information(name_model)
        tree.plot_tree(self.model.estimators_[0], feature_names=self.factors)
        plt.title("Graf Random forest(One of tree)")
        plt.show()

    def create_model(self):
        model = RandomForestClassifier(max_depth=self.max_depth)
        model.fit(self.train[self.factors], self.train[self.target])
        return model

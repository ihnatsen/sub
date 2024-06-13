from ML import Algorithm
from sklearn import tree
from matplotlib import pyplot as plt


class ST(Algorithm):

    def __init__(self, target, factors, df, max_depth):
        self.max_depth = max_depth
        super().__init__(target, factors, df)

    def create_model(self):
        model = tree.DecisionTreeClassifier(max_depth=self.max_depth)
        model.fit(self.train[self.factors], self.train[self.target])
        return model

    def print_information(self, name_model):
        super().print_information(name_model)
        tree.plot_tree(self.model, feature_names=self.factors)
        plt.title("Graf Simple tree")
        plt.show()


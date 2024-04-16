import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class CellOne:
    @staticmethod
    def task_one():
        X = np.array([
            50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150,
            160, 170, 180, 190, 200, 210, 220, 230, 240, 250,
            260, 270, 280, 290, 300, 310, 320, 330, 340, 350
        ]).reshape(-1, 1)

        y = np.array([
            10, 20, 380, 400, 430, 450, 480, 500, 520, 540, 560,
            580, 600, 620, 640, 660, 680, 700, 720, 740, 760,
            780, 800, 820, 840, 860, 880, 900, 920, 1200, 1300
        ])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        print("Accuracy of the model:", model.score(X_test, y_test))

        plt.scatter(X_train, y_train, color='blue', label='Training data')
        plt.scatter(X_test, y_test, color='green', label='Testing data')
        plt.plot(X, model.predict(X), color='red', label='Linear regression')
        plt.title('House prices prediction')
        plt.xlabel('House size (sq meters)')
        plt.ylabel('Price (thousand dollars)')
        plt.legend()
        plt.show()


def answer():
    """10% = 0.55; 50% = 0.88; 80% = 0.79; 90% = 0.79"""
    pass


def main():
    CellOne.task_one()


if __name__ == '__main__':
    main()
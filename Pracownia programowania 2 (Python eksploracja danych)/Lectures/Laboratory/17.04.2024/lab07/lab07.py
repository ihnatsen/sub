
from sklearn.datasets import fetch_california_housing  # Funkcja fetch_california_housing z biblioteki scikit-learn służy do pobierania zestawu danych dotyczących cen domów w Kalifornii
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split  # Funkcja train_test_split z biblioteki scikit-learn jest używana do dzielenia danych na zestawy treningowe i testowe, co pozwala ocenić skuteczność modelu na danych
from sklearn.linear_model import LinearRegression  # Klasa LinearRegression z biblioteki scikit-learn jest używana do budowania modelu regresji liniowej
import pandas as pd

class CellOne:

    @staticmethod
    def task_one():
        california = fetch_california_housing()
        X = pd.DataFrame(california.data, columns=california.feature_names)
        y = pd.DataFrame(california.target, columns=[
            'MedianHouseValue'])  # tutaj mogło by być dowolnie co innego nie tylko MedianHouseValue

        # Podział na zbiór treningowy i testowy
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Inicjalizacja modelu
        model = LinearRegression()

        # Trenowanie modelu
        model.fit(X_train, y_train)

        # Przewidywanie cen na zbiorze testowym
        y_pred = model.predict(X_test)

        # Obliczenie błędu średniokwadratowego
        mse = mean_squared_error(y_test, y_pred)
        print(f'Mean Squared Error: {mse}')

    @staticmethod
    def task_two():
        pass

    @staticmethod
    def task_three():
        pass

    @staticmethod
    def task_four():
        pass


def main():
    pass

if __name__ == '__main__':
    main()

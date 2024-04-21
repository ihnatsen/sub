# 17.04.2024 Ivan Ihnatsenkau 21595
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing, load_diabetes
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns


class Predicate:
    def __init__(self, X_train, X_test, y_train, y_test, name=None, y_predict=None):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.name = name
        self.y_predict = y_predict


class Task:
    @staticmethod
    def one():

        """
1 - MedInc 0.475;
2 - AveRooms 0.023;
3 - Latitude 0.021.

Z tych czynników może być jakieś użyteczny('MedInc' lub/i 'AveRooms'), lecz zgodnie z tradycją nauki: Nie formułuję
wstępnych ocen przed przeprowadzeniem badania - zmusze mnie do milczenia.

MSE
Accuracy of the model: 5.176022117131482 - MedInc
Accuracy of the model: 863.0347283669297 - HouseAge
Accuracy of the model: 18.01029360308177 - AveRooms
Accuracy of the model: 2.5539112842240903 - AveBedrms
Accuracy of the model: 3245922.7212283886 - Population
Accuracy of the model: 109.30534692368873 - AveOccup
Accuracy of the model: 1133.750468656949 - Latitude
Accuracy of the model: 14803.2800702342 - Longitude

Najlepszy czynik jest AveBedrms 2.554. Czym bliże MSE do zera czym mniej jest błąd od prawdziwej wartości."""

        # Rozszerzone metraże i ceny domów
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

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        print("Accuracy of the model:", model.score(X_test, y_test))

        plt.scatter(X_train, y_train, color='blue', label='Training data')
        plt.scatter(X_test, y_test, color='green', label='Testing data')
        plt.plot(X, model.predict(X), color='red', label='Linear regression')
        plt.title('House prices prediction')
        plt.xlabel('House size (sq meters)')
        plt.ylabel('Price (thousand dollars)')
        plt.legend()
        plt.show()

    @staticmethod
    def two():
        """
1 - MedInc 0.475;
2 - AveRooms 0.023;
3 - Latitude 0.021.

Z tych czynników może być jakieś użyteczny('MedInc' lub/i 'AveRooms'), lecz zgodnie z tradycją nauki:
Nie formułuję wstępnych ocen przed przeprowadzeniem badania - zmusze mnie do milczenia.

MSE
Accuracy of the model: 5.176022117131482 - MedInc
Accuracy of the model: 863.0347283669297 - HouseAge
Accuracy of the model: 18.01029360308177 - AveRooms
Accuracy of the model: 2.5539112842240903 - AveBedrms
Accuracy of the model: 3245922.7212283886 - Population
Accuracy of the model: 109.30534692368873 - AveOccup
Accuracy of the model: 1133.750468656949 - Latitude
Accuracy of the model: 14803.2800702342 - Longitude

Najlepszy czynik jest AveBedrms 2.554. Czym bliże MSE do zera czym mniej jest błąd od prawdziwej wartości."""
        california = fetch_california_housing()
        print(california.data[:10])

        predicates = [california.data[:, [i]] for i in range(len(california['feature_names']))]
        predicates_data = predicates
        y = california.target

        predicates = [Predicate(*(train_test_split(X, y, test_size=0.2, random_state=42))) for X in predicates]
        for predicate, name in zip(predicates, california['feature_names']):
            predicate.name = name

        models = [LinearRegression() for _ in range(len(california['feature_names']))]
        for model, predicate in zip(models, predicates):
            model.fit(predicate.X_train, predicate.y_train)

        for model, predicate in zip(models, predicates):
            predicate.y_pred = model.predict(predicate.X_test)
            print(f'Accuracy of the model: {model.score(predicate.X_test, predicate.y_test)} - {predicate.name}')
        print('MSE')
        for model, predicate in zip(models, predicates):
            predicate.y_pred = model.predict(predicate.X_test)
            print(f'Accuracy of the model: {mean_squared_error(predicate.X_test, predicate.y_test)} - {predicate.name}')
        for model, predicat, data in zip(models, predicates, predicates_data):
            plt.scatter(predicat.X_train, predicat.y_train, color='blue', label='Training data')
            plt.scatter(predicat.X_test, predicat.y_test, color='green', label='Testing data')
            plt.plot(data, model.predict(data), color='black', label='Linear regression')
            plt.title('Predykcja cen domów w Kalifornii')
            plt.xlabel(predicat.name)
            plt.ylabel('Mediana ceny domu (x100,000 $)')
            plt.legend()
            plt.show()

    @staticmethod
    def three():
        """
#1. Jakie cechy mają największy wpływ na postęp cukrzycy?

Accuracy of the model: 0.38269153958537394 - s5 Accuracy of the model: 0.23335039815872138 - bmi Accuracy of the model:
0.1734118396354255 - bp

#2. Przy najlepszej cesze jakie są wartości MSE i R^2

R^2 Accuracy of the model: 0.38269153958537394 - s5

MSE Accuracy of the model: 26545.789689841265 - s5

#3. Czy dodanie większej ilości danych poprawi model? Liczba rekordów w danym zbiorze danych wynosi 442
(print(len(diabetes.data))), co może być niewystarczające do przeprowadzenia adekwatnej analizy. Im więcej rekordów, na
których uczy się model, tym wyższa jego dokładność.

Rownież zalełność między danymi nieobowiązkowo musi być liniowa."""

        # Wczytanie zestawu danych dotyczących cukrzycy
        diabetes = datasets.load_diabetes()
        number_feature = len(diabetes['feature_names'])
        # print(len(diabetes.data))
        predicates = [diabetes.data[:, [i]] for i in range(number_feature)]
        X = predicates
        y = diabetes.target

        # Krok 2: Podział danych na zestaw treningowy i testowy
        predicates = [Predicate(*(train_test_split(X, y, test_size=0.2, random_state=42))) for X in predicates]
        for predicate, name in zip(predicates, diabetes['feature_names']):
            predicate.name = name

        # Krok 3: Budowa i trening modelu regresji liniowej

        models = [LinearRegression() for _ in range(number_feature)]
        for model, predicate in zip(models, predicates):
            model.fit(predicate.X_train, predicate.y_train)

        # Krok 4: Ocena modelu, Dokonaj predykcji i sprawdź współczynnik determinacji R^2 i średni błąd kwadratowy MSE

        for model, predicate in zip(models, predicates):
            predicate.y_pred = model.predict(predicate.X_test)
            print(f'Accuracy of the model: {r2_score(predicate.y_test, predicate.y_pred)} - {predicate.name}')

        print('MSE')
        for model, predicate in zip(models, predicates):
            predicate.y_pred = model.predict(predicate.X_test)
            print(f'Accuracy of the model: {mean_squared_error(predicate.X_test, predicate.y_test)} - {predicate.name}')

        # Krok 5: Wizualizacja wyników
        for model, predicat, _x in zip(models, predicates, X):
            plt.scatter(predicat.X_train, predicat.y_train, color='blue', label='Training data')
            plt.scatter(predicat.X_test, predicat.y_test, color='green', label='Testing data')
            plt.plot(_x, model.predict(_x), color='black', label='Linear regression')
            plt.title('Predykcja cen domów w Kalifornii')
            plt.xlabel(predicat.name)
            plt.ylabel('Mediana ceny domu (x100,000 $)')
            plt.legend()
            plt.show()

    @staticmethod
    def four():

        # Do liczenia Korelacji potrzebujemy dataFrame, bierzemy cel "progression" i dodajemy do danych
        diabetes = load_diabetes()
        X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
        y = pd.Series(diabetes.target, name="Progression")

        # Dodanie kolumny Progression do DataFrame
        X['Progression'] = y

        # Obliczenie współczynnika korelacji Pearsona dla X jak na poprzednich zajęciach
        print(f'The dataset contains a large number of records - {len(X)}')
        print(X.corr())

        # Wyświetlenie macierzy korelacji jak na poprzednich zajęciach
        sns.heatmap(X.corr(), annot=True, cmap='coolwarm')
        plt.title('Korelacja między cechami danych cukrzycy')
        plt.show()

    @staticmethod
    def five():
        """Pytania finalne

1. Jakie mamy wnioski z dwóch poprzednich zadań?
Jakie elementy miały najlepszą korelację dla zbioru cukrzycy?

Jakie elementy miały najlepszą korelację dla zbioru domów z Californi?

Zbiór danych 'fetch_california_housing' zawiera wystarczającą liczbę rekordów (20640 rekordów), aby umożliwić normalną
ocenę korelacji. Natomiast zbiór danych 'load_diabetes' może zawierać niewystarczającą liczbę wierszy (441),
aby umożliwić adekwatną ocenę korelacji.

Widać, że niektóre czynniki mają niską wartość korelacji, co oznacza brak wyraźnej zależności między nimi a odpowiedzią.
Niektóre czynniki są zmiennymi kategorycznymi (np. płeć), dlatego korelacja nie jest adekwatnym modelem dla tych
zmiennych.

#2

BMI 0.586450
#3

MedianHouseValue 0.688075"""

        california = fetch_california_housing()
        X = pd.DataFrame(california.data, columns=california.feature_names)
        y = pd.Series(california.target, name="MedianHouseValue")
        print(f'The dataset contains a large number of records - {len(X)}')
        # Dodajemy medianę cen domów do DataFrame
        X['MedianHouseValue'] = y

        # Rysujemy macierz korelacji
        print(X.corr())

        sns.heatmap(X.corr(), annot=True, cmap='coolwarm')
        plt.title('Korelacja między cechami danych domów z Kalifornii')
        plt.show()


def main():
    Task.one()
    Task.two()
    Task.three()
    Task.four()
    Task.five()


if __name__ == '__main__':
    main()

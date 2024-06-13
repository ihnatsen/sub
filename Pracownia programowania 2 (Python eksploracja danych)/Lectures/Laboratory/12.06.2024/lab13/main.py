from matplotlib import pyplot as plt
from ML import Algorithm
from logistic_regression import LR
from simple_tree import ST
from random_forest import RF
from support_vector_machine import SVC
import pandas as pd


def filter_data() -> pd.DataFrame:
    data = pd.read_csv('Titanic-Dataset.csv')
    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
    data['Embarked'] = data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
    avg_age = round(data['Age'].dropna().mean())
    data['Age'] = data['Age'].fillna(avg_age)
    data = data.dropna()
    return data


def main():
    df = filter_data()
    target = ['Survived']
    factors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Fare', 'Embarked']

    name_models = ['Simple tree',
                   'Random forest',
                   'Support Vector Machine \n(Classificator)',
                   'Logical Regression'
                   ]
    models: list[Algorithm] = [
        ST(target, factors, df, max_depth=3),
        RF(target, factors, df, max_depth=3),
        SVC(target, factors, df),
        LR(target, factors, df)
    ]

    for model, name in zip(models, name_models):
        model.print_information(name)

    # accuracy_score
    values_accuracy_score = [model.get_accuracy() for model in models]
    fig, ax = plt.subplots()
    ax.barh(name_models, values_accuracy_score, label=name_models)
    ax.set_ylabel('accuracy_score')
    ax.set_title('Value of accuracy score by model')
    plt.show()

    # precision_score
    values_precision_score = [model.get_precision() for model in models]
    fig, ax = plt.subplots()
    ax.barh(name_models, values_precision_score, label=name_models)
    ax.set_ylabel('precision_score')
    ax.set_title('Value of precision_score by model')
    plt.show()


if __name__ == '__main__':
    main()

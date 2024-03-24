# 23.03.2024 Ivan Ihnatsenkau
from pandas import *
from collections import Counter
import matplotlib.pyplot as plt
df = read_csv('titanic.csv')


class CellOne:

    @staticmethod
    def task_one():
        print(f'_DataSet Titanic_')
        print(df)

    @staticmethod
    def task_two():
        print('First 5 records')
        print(df.head(5))

    @staticmethod
    def task_three():
        print('DataSet summary')
        print(df.isnull().sum())

    @staticmethod
    def task_four():

        df['Age'].fillna(df['Age'].median(), inplace=True)
        popular = tuple(Counter(df['Embarked']))[0]
        df['Embarked'].fillna(popular, inplace=True)
        print(df.isnull().sum())

    @staticmethod
    def task_five():
        print(df.describe)


class CellTwo:
    @staticmethod
    def task_one():
        print(f'Number of passengers on the Titanic {len(df)}.')

    @staticmethod
    def task_two():
        print(f'The number of females on the Titanic was {len(df[df['Sex'] == 'female'])}.')
        print(f'The number of male on the Titanic was {len(df[df['Sex'] == 'male'])}.')

    @staticmethod
    def task_three():
        presents_for_sex = dict(df.groupby(['Sex'])['Survived'].mean())
        values = [f'{present * 100:_.2f}%' for present in presents_for_sex.values()]

        presents_for_sex = {name: value for name, value in zip(presents_for_sex, values)}

        print(presents_for_sex)

    @staticmethod
    def task_four():
        df['IsChild'] = list(df['Age'] <= 18)
        print(df)

    @staticmethod
    def task_five():
        num_children = dict(Counter(list(df['Age'] <= 18)))[True]
        print(f'num children is {num_children}')


class CellThree:

    @staticmethod
    def task_one():
        values_ages = [age for age in list(df['Age'].fillna(-1)) if age != -1]
        plt.title('Rozkład wieku pasażerów')
        plt.xlabel('Wiek')
        plt.ylabel('Liczba pasażerów')
        plt.hist(values_ages, edgecolor='black')

        plt.show()

    @staticmethod
    def task_two():
        data = [20, 21, 22, 23, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 24, 26, 64, 100]
        plt.boxplot(data)
        plt.title('Box plot')
        plt.xlabel('DataSet')
        plt.ylabel('Procent')

        plt.show()

    @staticmethod
    def task_three():
        len(df[df['Survived'] == '1'])
        survived = len(df[df['Survived'] == 1])
        deceased = len(df[df['Survived'] == 0])

        data = [survived, deceased]
        labels = ['liczba przeżyć', 'liczba zgonów']

        plt.bar(labels, data, color=['green', 'red'])

        plt.title('Stosunek liczby przeżyć do liczby zgonów')
        plt.xlabel('Status')
        plt.ylabel('Ilość')

        plt.show()

    @staticmethod
    def task_four():
        pclass_num_surv = dict(df.groupby('Pclass')['Survived'].sum())

        data = pclass_num_surv.values()
        labels = pclass_num_surv.keys()

        plt.bar([str(cls) for cls in labels], data)

        plt.title('Zależność między klasą biletu (Pclass) a przeżywalnością')
        plt.xlabel('Pclass')
        plt.ylabel('Ilość')

        plt.show()

    @staticmethod
    def task_five():
        groups = tuple(df.groupby('Pclass')['Fare'])
        column = {name: tuple(values) for name, values in groups}
        data = column.values()
        plt.boxplot(data, labels=['One', 'Two', 'Three'])
        plt.xlabel('Pclass')
        plt.ylabel('Fare')
        plt.show()


class CellFour:
    @staticmethod
    def task_one():
        df['Sex'] = [1 if sex == 'male' else 0 for sex in list(df['Sex'])]


def main():

    # CellOne.task_one()
    # CellOne.task_two()
    # CellOne.task_three()
    # CellOne.task_four()
    # CellOne.task_five()

    # CellTwo.task_one()
    # CellTwo.task_two()
    # CellTwo.task_three()
    # CellTwo.task_four()
    # CellTwo.task_five()

    # CellThree.task_one()
    # CellThree.task_two()
    # CellThree.task_three()
    # CellThree.task_four()
    # CellThree.task_five()

    # CellFour.task_one()
    pass


if __name__ == '__main__':
    main()

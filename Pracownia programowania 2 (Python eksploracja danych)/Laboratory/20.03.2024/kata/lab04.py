# 20.03.2024

from pandas import *

# wybranie kolumn df[<>]
# Filtrowanie df[df[<>] <warunrek>]
# Sortowanie df.sort_value(<>)
# app column df['window'] = [value]
# df = df.drop('amount', axis=1)
# df = df.rename(colums ={'devieId: 'id'})
# df[<>] = df[<>].apply(np.<foo>) -> применяет ф-кции до значение кол
# df = df.fillna(value=0)
# df = df.fillna(df['Age'].median())
# df = df.dropna() # usujecia wierszy
# df = df.drop_duplicates()

df = read_csv('titanic.csv')


def task_one():
    pass


def main():
    task_one()


if __name__ == '__main__':
    main()

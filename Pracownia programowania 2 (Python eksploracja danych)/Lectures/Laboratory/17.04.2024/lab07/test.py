from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Хреновая абстракция dataseta
# нормально только представляет ее документацию

x, y = [*range(100)], [y*2 for y in range(100)]
x, y = pd.DataFrame(x), pd.DataFrame(y)

fetch_train, fetch_test, target_train, target_test = train_test_split(
    x, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(fetch_train, target_train)



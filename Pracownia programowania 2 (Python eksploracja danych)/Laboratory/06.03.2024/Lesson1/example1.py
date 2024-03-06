# 06.03.2024

from collections import Counter
from typing import Any


def foo1() -> None:
    return print('Hello, World!')


def foo2(arg1: int, arg2: int) -> tuple | None:
    try:
        return arg1+arg2, arg1-arg2, arg1*arg2, arg1/arg2
    except ZeroDivisionError:
        print('Can\'t divide by zero')


def foo3(collection: list) -> Any:
    return collection[::-1]


def foo4(num: int) -> bool:
    return num % 2 == 0


def foo5(n: int) -> int:
    lst = [0] * n
    lst[0] = 1
    lst[1] = 1
    for i in range(2, len(lst)):
        lst[i] = lst[i-1] + lst[i-2]
    return lst[-1]


def foo6(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]


def foo7(lst: list) -> dict:
    return dict(Counter(lst))


def foo8(lst: list) -> tuple:
    return max(lst), min(lst)


def main():
    lst = [*range(10)]
    foo1()
    print(foo2(10, 0))
    print(foo3(lst))
    print(foo4(5))
    print(foo5(12))
    print(foo6("A man a plan a canal Panama"))
    print(foo7([1, 2, 2, 3, 3, 3, 4]))
    print(foo8([*range(10)]))


if __name__ == '__main__':
    main()

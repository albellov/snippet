import random


def print2(value):
    print('#####')
    print(value)
    print('#####')


def predict_ids(count):
    return [random.randint(1000, 100000) for _ in range(count)]

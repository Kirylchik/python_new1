from functools import reduce

def increase_and_multiply_by_two(number):
    return (number + 10) * 2

""" список чисел"""
numbers = [1, 2, 3, 4, 5]

""" используем map() с лямбда-функцией"""
result = list(map(lambda x: (x + 10) * 2, numbers))

"""выводим результат"""
print(result)

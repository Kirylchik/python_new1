# def decorator_1(fuck):
#     def wrapper(*args, **kwargs):
#         print('Начало')
#         fuck(*args, **kwargs)
#         print('Конец')
#     return wrapper

# a =1
# b=2
# @decorator_1
# def calc(a,b):
#     print(f'Cама функция {a} {b}')

# @decorator_1
# def sum(a,b,c):
#     print(f'сама функция {a} {b} {c}')
# calc(a,b)
# print('-----------------')
# sum(a,b,4)





# def calc_1(list_obj: list):
#     print(list_obj)

# def calc_2(list_obj: list):
#     print(list_obj)

# def calc_3(list_obj: list):
#     print(list_obj)











# from datetime import datetime

# # Декоратор для измерения времени выполнения функции
# def measure_execution_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = datetime.now()
#         result = func(*args, **kwargs)
#         end_time = datetime.now()
#         execution_time = end_time - start_time
#         print(f"Время выполнения функции '{func.__name__}': {execution_time}")
#         return result
#     return wrapper
# #Функция 1
# @measure_execution_time
# def function_one(n):
#     for _ in range(n):
#         pass
# #Функция 2
# @measure_execution_time
# def function_two(a, b):
#     return a + b

# function_one(10000000)  #время выполнения будет заметным
# result = function_two(5, 10)
# print("Результат функции function_two:", result)

import datetime


def timelapse(func):
    def wrapper(a, b):
        start = datetime.datetime.now()
        result = func(a, b)
        finish = datetime.datetime.now()
        total_time = finish - start
        print(f"Total time: {total_time}")
        return result

    return wrapper


@timelapse
def some_function(text, text_1):
    print("Меня зовут", text, text_1)


some_function("Иван", "Петрович")
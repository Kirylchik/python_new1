Задача 1

chislo= lambda x: 'чётное' if x%2==0 else 'нечётное'
number= int(input('Введите число'))
result= chislo(number)
print (f' число {number} - {result}')

Задача 2

numbers = [1, 2, 3, 4, 5]
string_numbers = list(map(lambda x: str(x), numbers))
print(string_numbers)

Задача 3

def is_palindrome(word):
    return word == word[::-1]
words_tuple = ("раздолбай", "топот", "шалаш", "радар","tenet","довод", "удалёнка", "олег")
palindromes = tuple(filter(lambda word: is_palindrome(word), words_tuple))
print("Полиндромы:", palindromes)

Задача 4

from datetime import datetime

# Декоратор для измерения времени выполнения функции
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f"Время выполнения функции '{func.__name__}': {execution_time}")
        return result
    return wrapper
#Функция 1
@measure_execution_time
def function_one(n):
    for _ in range(n):
        pass
#Функция 2
@measure_execution_time
def function_two(a, b):
    return a + b

function_one(10000000)  #время выполнения будет заметным
result = function_two(5, 10)
print("Результат функции function_two:", result)





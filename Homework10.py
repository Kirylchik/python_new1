class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль запретили математики")
        return a / b


calculator = Calculator()

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Выберите операцию (+, -, *, /): ")

    if operation == "+":
        result = calculator.add(num1, num2)
    elif operation == "-":
        result = calculator.subtract(num1, num2)
    elif operation == "*":
        result = calculator.multiply(num1, num2)
    elif operation == "/":
        result = calculator.divide(num1, num2)
    else:
        print("Неверная операция")

    print("Результат:", result)

except ValueError as ve:
    print("Ошибка:", ve)
except ZeroDivisionError:
    print("Ошибка: Деление на ноль")
except Exception as e:
    print("Произошла ошибка:", e)

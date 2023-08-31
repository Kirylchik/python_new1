def geometric_progression(a, r, n):
    current_term = a
    for _ in range(n):
        yield current_term
        current_term *= r

start = float(input("Введите начальный элемент: "))
ratio = float(input("Введите знаменатель: "))
count = int(input("Введите количество элементов: "))

# Создаем генератор
progression = geometric_progression(start, ratio, count)

# Выводим элементы прогрессии + дебаггинг
for term in progression:
    print("Текущий элемент:", term)



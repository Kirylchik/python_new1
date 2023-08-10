a='a'
b='b'
c='c'
res= '   '+a+' ,'+b+'   '+c+'   !'
print(res)

f_string= f'  {a}   ,{b}  ,{c}   !'
print(f_string)

name='Kirill'
ola=f'Hello, {name}!'
print(ola)

name='Maria!'
hey='Ola, {c}'.format(c=name)
print(hey)

firstname= input('Введите Имя')
lastname= input('Введите Фамилию')
enter='Hello,{}{}'.format(firstname,lastname)
print(enter)

first=('Oleg')
second=(' Kvasov')
third='Hello, %s%s'%(first, second)
print(third)

name_1= 'Kirill'
name_2= 'Anton'
name_3= 'Maria'
if name_1== 'Kirill':
    print('Отличное имя!')
if name_2== 'Anton':
    print('Норм')
if name_3== 'Maria':
     print('Сойдёт:)')
else:
      print('Значит, не повезло с именем')



veritas= 'Женская логика(Ну-ну:))' if True else 'Вот вот:)'
print(veritas)



name= '' # Проверяем Тру, Фолс. Тру(числа в т.ч отрицательные кроме 0,заполненные строки,кортежи,словари), если пишем Нот, то наоборот
if not name:
     print('Ничего')



# 3 задание

name= input('Введите Ваше имя')
age= input('Введите Ваш возраст')
infinity= 0
while infinity!=0:
    if type(age)!= int or age<=0:
     print('Ворнинг, повторите ввод')
    elif 0<age<10:
     print(f'Привет, шкет {name}!')
    elif 10<=age<=18:
     print(f'Как житуха,{name}')
    elif 18<age<100:
     print(f'Что желаете,{name}?')
else:
     print(f'{name}, вы лжёте- в наше время столько не живут!')
#  Не могу понять, почему не работает, если пытаюсь в цикл завернуть


# 4 задание

a = 1
b = int(input("Введите число: "))
for summa in range(a, b +1):
    result = sum(summa ** 3 for summa in range(a, b + 1))
print(result)

# 5 задание. Подсмотрел в интернете

import random
number= random.randint(1,10)
user=-1
while user!= number:
    user= int(input('Угадай число'))
    if user> number:
        print('Число должно быть меньше!')
    elif user< number:
        print('Число должно быть больше!')
    else:
        print('Ты угадал! Это число= '+ str(number))
        break



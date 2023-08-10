name= input('Введите Ваше имя')
age= input('Введите Ваш возраст')
infinity= 0
while infinity!=name and age:
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
    

        
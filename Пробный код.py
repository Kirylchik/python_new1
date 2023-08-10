# name_1= 'Kirill'
# name_2= 'Anton'
# name_3= 'Maria'
# if name_1== 'Kirill':
#     print('Отличное имя!')
# if name_2== 'Anton':
#     print('Норм')
# if name_3== 'Maria':
#      print('Сойдёт:)')
# else:
#       print('Значит, не повезло с именем')


# veritas= 'Женская логика(Ну-ну:))' if True else 'Вот вот:)'
# print(veritas)



# name= '' # Проверяем Тру, Фолс. Тру(числа в т.ч отрицательные кроме 0,заполненные строки,кортежи,словари), если пишем Нот, то наоборот
# if not name:
#      print('Ничего')










# a='a'
# b='b'
# c='c'
# c=a==b
# if c:
#      print('Равны')
# else:
#      print('Не равны')     





# c=[1, 2, 3, 4,]
# a= 'abce'
# print('a' in a)


# a=1
# b=1
# print(a==b)
# print(a is b)



# a=[1,2]
# b=[1,2]
# print(a==b)
# print(a is b)




# a=10
# while a>0:
#     print(a)
#     a-=1
# else:
#     print(a)


# a=[1, 2, 3, 4, 5]
# n=10
# for item in range(n+1):
#     # if item ==2:
#     #     continue
#     # if item == 4:
#     #     break
#     print(item)
# res= range(1,n)

a=[23, 11, 273, 23, 43, 764, 35]
b=[]
for  item in a:
    if item== 273:
        b.append(87)
    else:
        b.append(item)    
a=b
print(b)

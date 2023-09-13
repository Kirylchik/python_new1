 # Задание 3

import re
input = str(input("Введите адрес почты:"))
def input_data(e_mail):
    testmail = r"^(?!\.)(?!.*\.@)(?!.*\.\.)[A-Za-z0-9.!#  %&'*+—/=?^_`{|}~]+@(?!\-)[a-z0-9{63}\-]+\.[a-z]+(?!\-)$"
    result = re.match(testmail,input) is not None
    print(result)
input_data(input)

#  Задание 4

import random
MY_LIST = ["q", "w", "e", "r", "t", "y"]
def new_generator(numbers):
    for number in range(1,numbers+1):
        name = "".join([random.choice(MY_LIST) for i in range(random.randint(1, 10))])
        yield name + str(number)
for item in new_generator(5):
    print(item)


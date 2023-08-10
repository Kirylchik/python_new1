# def square (n):
#     """ принимает число  и возводит его в квадрат""" 
#     return (n**2)
# print (square.__doc__)


# print (list(map(lambda x: x*x, [4,5,6])))


result = map(lambda x: (x+10)*2, [1, 2, 3, 4, 5, 6])
print(list(result))

# result = filter(lambda x: x%2==0, [1, 2, 3, 4, 5, 6])
# print(list(result))

# from functools import reduce
# result= reduce(lambda a, x: a+x**2, [1,2,3], 0)
# print (result)


# res= lambda x, y: x+y
# print(res(1,2))

# res= [1,2,3,4,5,6,7,8,9,10]
# print(tuple(filter(lambda x: x>5, res)))


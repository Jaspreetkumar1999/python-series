# ---------------------------------------Function------------------------------------------
# def hello():
    # pass   if we want to keep our function blank just put pass statement in it it will not show any error we can fill this function in future
    # print("hello World!")
    # return 'Hello World!'
# hello() it will not print anything in case of return statement
# print(hello()) ----- in case of return it will show return ...hence return statement means we are getting something back from function we can use it similar as we use data type
# print(hello().upper())
# ----------------------------------pass the argument--------------------------------
# def message(greeting,name):
#     # return '{} function'.format(greeting)
#       return  f"{greeting} {name}"
#     # print(greeting + name)
#
# print(message(("you are most welcome"),("jaspreet")))


#-----------*args is a special type of argument it no necessary to use name as *args  we can use any name but make sure it have * before the name this type of argument is used where
# we have scalable list or tupple as a argument for scalable dictionary we use **kwargs there is convention it should be in order = normal argument, *args ,**kwargs
# def student_info(normal, *args , **kwargs):
#     print(normal)
#     print(args)
#     print( kwargs)
# a=['jaspreet','kumar','jassi','jeet','jas','annahat']
# b= {'name': 'jaspreet','age':20,'profession':'engineer'}
# student_info('normal',*a,**b)
# def student_info( *args , **kwargs):
#     print(args)
#     print( kwargs)
# student_info('jaspreet','kumar', name ='jassi', std='BA')




#----------------------------------program to implement  functions----------------------------------
month_days =[0,31,28,31,30,31,30,31,31,30,31,30,31]
#   ---------------------to check wheather entered year is leep or not
def is_leep(year):
    return year % 4 ==0 and ( year % 100 !=0 or year%400 ==0)
#
# x=is_leep(2019)
# print(x)
def  days(year, month):
    if not 1<=month<=12:
        return 'invalid month'
    elif month ==2 and is_leep(year):
        return 29
    else:
        return month_days[month]
print(days(2019,3))
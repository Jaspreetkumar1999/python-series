# language ='java'
# # language='python'
# if language == 'python':
#     print('language  is python')
# elif language=='java':
#     print('language is java')
# elif language == 'javascript':
#     print('language is javascript')
# else :
#     print('not match')
    # python does not have case statements elif condition is pretty much good to deal with cases
# -------------------------------------------------symbolian operations we have----------------------------------------------
# user ='admin'
# legged_in ="false"
# if user=='admin' and legged_in: AND operation if both the conditions are true
#     print('you are allowed')
# if user=='admin' and legged_in:
#     print('you are most welcome')
# else :
#     print('sorry')
# user ='admin1'
# legged_in =False
# if user=='admin' or legged_in:    OR operation
#     print('welcome')
# else:
#     print('sorry')
# if not legged_in =='true':  It will simply perform NOT operation convert true to false and false into true
#     print("please logged in")
# else:
#     print("welcome")
a =[1,2,3]
# b =[1,2,3]
# print(a==b)  it will return true bcz there value is same
# print(a is b) it will return false bcz these are two objects in memory
# print(id(a))
# print(id(b))
# b = a
# print(a is b) it will true bcz now these two are same objects
# condition = None it will also consider as false
# condition = 0   it will also consider as false
# condition = -2      ,2 if assign condition as non zero value it will consider as true
# condition = []    if there is any empty sequence(list,set,tuple, etc) it will consider it as false

if condition:
    print('evaluated to true')
else:
    print('evaluated to false')

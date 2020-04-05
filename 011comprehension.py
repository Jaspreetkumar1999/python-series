# -----------to creat list in single line of code  ---------------

# list1 =[1,3,4,5,3,5,7,8,6,68,9,0]
# # print(list1)
# my_list =[]
# # for n in list1:
# #     my_list.append(n)
# #     # to copy one list to another
# # print(my_list)
# list2= [n for n in list1]
# # to copy one list to another
#
# print(list2)
# list = [i*3 for i in range(1,12,2)]
# print(list)
# list2 =[1,2,3,4,5,6,6]
# # to roduce square of each element
# list1 =[]
# for n in list :
#     list1.append(n*n)
# print(list1) --------------------------
# my_list = map(lambda n: n*n, range(0,5))
#---------------------------------lamda function is a anonymouse function means we can use it our normal function
# my_list = lambda x,y:x+y   ==============================lambda funcion============
# print(my_list(4,5))
# list1 = list(map(lambda n: n*n,list2))
# # in map funtion we use two parameter first we pass function in it and second one we pass a list or we can say set of data on which we want to perform operation
# print(list1)
# list1 =[]
# for i in list2:
#     if i%2==0:
#         list1.append(i)
# print(list1)
# list2 =[1,2,3,4,5,6,6]
# list1 = list(filter(lambda n: n*n%2==0,list2 ))
# print(list1)
# list1= []
# for letter in 'abcd':
#     for num in range(4):
#         list1.append((letter,num))   #------in general append takes only one argument but if we want to pass more than one argument than we have to pass an extra pair of()
# print(list1)
# list2 =[(letter, num) for letter in 'abcd' for num in range(5) ] #------------------list comprehension
# print(list2)
#--------------------zip function-----------------
# list1 =['jaspreet', 'nikhil','karan', 'manjit','neeraj','maniram']
# list2 = ['kumar', 'sharma', 'duggal', 'singh','kumar', ' aaka']
# print( list(zip( list1,list2))) ----------zip function combine both the lists make tuple
# my_dict ={}
# for i,j in zip(list1,list2):
#     my_dict[i] = j
# print(my_dict)
# my_dict ={ name: surname for name, surname in zip(list1,list2) if i !='aaka'}           -------to add restrictions to it
# print(my_dict)
# ---------------------------set comprehension----------------------
nums = [1,2,2,3,3,4,5,6,7,8,9,10]
# myset =set()   # -------we cannt declare empty set just writing as {} we have to write it as set()
# for i in nums:
#     myset.add(i)
# print(myset)
myset ={ i for i in nums } # -------------set comprehension
print(myset) 
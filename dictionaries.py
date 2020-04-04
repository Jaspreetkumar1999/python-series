#----------------------------------------------------- dictionary-----------------------------------------

# data is stored in the form of key value pair
student ={'name':'jaspreet','age':20, 'courses':['math','english','computer']}
# print(student['courses'])  to acces data via key
# student ={1:'jaspreet',2:20, 'courses':['math','english','computer']} we can also assign key as integer value
# print(student.get('name'))  via key
# print(student.get('jas','not found')) if key is not present then we can also assign default key value
# student['phone'] ='123456789' to add value into dictonary
# print(student.get('phone','not found'))
# student['name']='jassi'  if we give new key similiar to existing key it will update
# student.update({'name': 'james','age':34,'phone':765432123456654}) to update multiple value
# del student['age'] to delete via key
# age = student.pop('age') deletion via pop method but it also return the value
# print(len(student)) to find length of dictonary

# print(age)
# print(student.values()) to print only values
# print(student.keys()) to print keys
# print(student.items()) to print key and value in the pair
# for i in student:
#     print(i)  this will show us keys via loop
# for key ,value in student.items():
#     print(key,value)  to print items in key value pair


# person ={'name':'jaspreet','age':'20'}
# sentence = "my name is "+ person['name']+' and I am '+ str(person['age']) + ' years old'
# # ordinary method of string formating
# sentence = f"my name is {person['name'].upper()} and I am {person['age']} year old. "
# # # f string method of string method
# print(sentence)
# for n in range(1,11):
#     sentence = f" The value is {n:03}"
#     # 03 will show answere in 3 digits eg 001,002 etc
#     print(sentence)
# pi = 3.146457856
# sentence = f" the value of pi is {pi:.3f}"
# # .3f show the digits after the point
# print(sentence)
from datetime import datetime
birthday = datetime(1990,2,15)
# year month day format
sen = f"jen has birthday on {birthday:%B,    %d ,%Y}"
print(sen)
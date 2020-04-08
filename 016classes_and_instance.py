# grouping of similar data and funcion which allows us easy to reuse and other neccesaary operations
class Employe:
    def __init__(self, name,clas,id):
        self.name = name
        self.clas = clas
        self.id = id
        self.email = name + '.' + "@gmail.com"
    def info(self):
        info = f" My Name is {self.name}. I'm studying in {self.clas}. My college id is {self.id}. My email is {self.email} "
        return info
        # special init method we can say constructor or to intilialize. automatically it have self instance you give other argument or instances you want to pass init it alongwith self
#class is necessary to creat object /instances
emp_1 = Employe('jaspreet','b.tech',123) # arguments that we want to pass on
emp_2 = Employe('kumar','BA',321)
    # both are the objects of same class but they are stored at different locations of memory
# emp_1.name = 'jaspreet'
# emp_1.clas = 'b.tech'
# emp_1.id = 1234
# emp_2.name = 'kumar'
# emp_2.clas = 'b.tech'
# emp_2.id = 321
#instance variable re those which are changing instantly . setting instance variable mannually is not an efficient way when we dealing with class we want to make it automatically so we use special init method
# print(emp_1)
# print(emp_2)
# print(emp_1.name)
# print(emp_1.email)
# print(emp_1.info())
# # accesing of info function using objects
# print(emp_2.info())
print(Employe.info(emp_1))
# acrss of info function using class in that case we have to pass object in it

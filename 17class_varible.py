#instance vriable can be unique at instances
# class variables are variable that are shared among all instances of class for eg bonus for employee which remains same for everyone
class Employee:
    bonus = 50 # class variable we can access it with class name Employee.bonus or self.bonus . fist variable is checked in that funcion after that it will checked in that class
    no_cp_tk = 0
    def __init__(self,name,id,pay,department):
        self.name = name
        self.id = id
        self.pay = pay
        self.department = department
        Employee.no_cp_tk += 1

    def biodata(self):
        bio = f"My Name is {self.name}. I'm working for New Millenium Coders in {self.department} department. My employee id is {self.id}. ${self.pay} is my basic monthly Income." \
              f" After the addition of bonus it will became {self.bonus + self.pay}"

        return bio
# name = input("enter the name")
# id = int(input("enter the unique id no in integer form"))
# pay = int(input("enter your pay in integer form"))
# department = input("enter your department")
print( " No of copies taken:",Employee.no_cp_tk) # here it will print zero bcz no object is created yet and we set   indtial value zero if we put this statement after the object it will  increament by one
Emp_1 = Employee('jaspreet',1234, 300, 'technical')
Emp_2 = Employee('kumar',4556, 500, 'HR')
# print(Employee.no_cp_tk)
Emp_1.bonus = 100 # to set local variable outside the class or with the help of object. if we change it through object it will affect only that object and if change it through class it will effect the  whole class means for every object
# print(Emp_1.biodata())
# print(Emp_2.biodata())
# print( " No of copies taken:",Employee.no_cp_tk)
# print(Employee.biodata(Emp_1))
# print(Emp_1.__dict__) # there is no bonus amount is added in this case bcz bonus is our class variable

#regular method takes instance as a first argument by convention we call it self we can change it how it takes class as a first argument
# static method dont take any of them as a default



class Employee:
    noOfEmployee = 0
    raise_amt = 1.04
    def __init__(self,name,pay,age):
        self.name1 = name
        self.pay = pay
        self.age = age
        Employee.noOfEmployee +=1
    def info(self):
        return f"my name is {self.name1}. I'm {self.age} yrs old. My monthly salary is ${self.pay} "
    def pay1(self):
        return int(self.pay*self.raise_amt )
    # @classmethod # decorator to set class method. decorator alter the fnx of method
    # def set_raise_amt (cls,amount): # bydefault method takes self as first argument but now it takes class as a first argument cls is used to denote the class
    #     cls.raise_amt = amount
    #     print(amount)
    @classmethod
    def from_string(cls,emp_str):
        name, salary, age = emp_str.split('-')
        return cls(name, salary, age)
    @classmethod
    def fromtimestamp(cls,t):
        #construct a date from a postfix (like.time())
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y,m,d)
    @staticmethod
    def is_work_day(day):
        if day.weekday() ==5 or day.weekday() == 6:
            return False
        return True
import datetime
my_date = datetime.date(2016,7,11)
print(Employee.is_work_day(my_date))
# print(Employee.noOfEmployee)
emp1 = Employee('jas',300,20)
# print(emp1.info())
# print(emp1.pay1())
# print(Employee.noOfEmployee)
# print(Employee.raise_amt) # it will show 1.04 bcz we set class variable as 1.04
# Employee.set_raise_amt(1.05) # it will set our class variable raise_amt = 1.05
# print(emp1.raise_amt)
# emp_str_1=  'preet-100-25'
# emp_str_2 = 'kumar-200-30'
# emp_str_3 = 'manpret-500-24 '
# # name, salary, age = emp_str.split('-')
# # emp2 = Employee(name,salary,age)
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.info()) # we pass string to class via classmethod first we split it and instances are created from this string
# print(new_emp_1.name1)

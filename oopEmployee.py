# oopEmployee.py 
# author: Joe Oakes 
# 10/20/2013

class Employee: 
 'Common base class for all employees' 
 # class variable whose value would be shared among the instances 
 empCount = 0

 # method __init__() class constructor or initialization method 
 # called when you create a new instance of this class 
 def __init__(self, name, salary): 
  self.name = name 
  self.salary = salary 
  Employee.empCount += 1

 # Class method similar to functions but includes self argument 
 # Do not include the self when calling the method 
 def displayCount(self): 
  print "Total Employee %d" % Employee.empCount

 def displayEmployee(self): 
  print "Name : ", self.name,  ", Salary: ", self.salary


opEmployee.py
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





# Create instance objects using the Employee class
# This will call the __init__() constructor method
# Create three new Employee objects
emp1 = Employee("John Oakes", 1000)
emp2 = Employee("Joe Oakes", 2000)
emp3 = Employee("Sue Oakes", 3000)

# Using the object dot operator call the displayEmployee() method
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()

# Access and print the class variable empCount
print "Total Employee %d" % Employee.empCount


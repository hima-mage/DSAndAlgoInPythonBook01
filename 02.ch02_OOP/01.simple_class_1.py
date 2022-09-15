class Empolyee :
    empCount = 0
    # self represents the instance of the class
    # it is clearly seen that self and obj is referring to the same object
    # The Default __init__ Constructor
    # __name__ is a built-in variable which evaluates to the name of the current module.
    def __int__(self , name , salary):
        self.name = name
        self.salary = salary
        Empolyee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print( "Name : ", self.name, ", Salary: ", self.salary)
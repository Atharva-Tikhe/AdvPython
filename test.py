# two variables, function to add and another function to get the result

# class Addition:
#     def __init__(self):
#         pass

#     def addition(self, a, b):
#         return a + b       


class Organisation:
    # def set_name_org(self, org_name):
    #     self.org_name = org_name

    def display(self):
        print(f"Organisation Name: {self.org_name}")

class Department(Organisation):
    # def set_name(self, dep_name, code):
    #     self.dep_name = dep_name
    #     self.code = code

    def display(self):
        print(f"Department Name: {self.dep_name} - Department code: {self.code}")        

class Employee(Department):
    def get_data(self, org_name, dep_name, code,  eid, ename):
        self.eid = eid
        self.ename = ename
        self.org_name = org_name
        self.dep_name = dep_name
        self.code = code


    def display(self):
        Organisation.display(self)
        Department.display(self)
        print(f"Employee ID: {self.code}{self.eid} - Employee Name: {self.ename}")
        

emp1 = Employee()
emp1.get_data(org_name= "MIT", dep_name= "BioEngg", code= 503 , eid = 1, ename= "ABC")
# emp1.set_name("BioEngg", 512)
# emp1.set_name_org("MIT")
# emp1.display()


# Assignment: Multipath inheritance

# Student class 
#     Sports var/50 
#     Test 2 vars / 50
#     |
#     v
#     Results (object)


class Student:
    def set_data(self, org, code):
        self.org = org 
        self.code = code
    
class Sports(Student):
    def set_name(self, sport, marks):
        self.sport = sport
        self.marks = marks

class Test(Student):
    def set_test(self, subject, test_marks):
        self.subject = subject
        self.test_marks = test_marks

class Result(Sports, Test):
    def set_result(self, id, name):
        self.id = id
        self.name = name
    
    def display(self):
        print(f'Student ID: {self.code}{self.id}\n Student Name: {self.name}\n Department: {self.org}')
        print(f'\n Sports marks: {self.sport} - {self.marks}')
        print(f'\n Subject marks: {self.subject} - {self.test_marks}')


student = Result()
student.set_result(25, "Atharva Tikhe")
student.set_name("Football", "45/50")
student.set_test("Advanced Python", "47/50")
student.set_data("MIT ADT University", "MITU19IMBI00")
student.display()
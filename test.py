
# Assignment: Multipath inheritance example of hybrid inheritence

# Student class 
#     Sports var/50 
#     Test 2 vars / 50
#     |
#     v
#     Results (object)


class Student:
    def set_data(self, org, stu_code):
        self.org = org 
        self.code = stu_code
    
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

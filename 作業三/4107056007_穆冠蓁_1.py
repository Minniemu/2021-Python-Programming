class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    # finish the logic in the class
    def __repr__(self):
        return self.name
            
    def __lt__(self,another_student):
        return self.grade < another_student.grade

AList = [student("Mary", 80), student("Jack", 66), student("Eric", 93), student("June", 86), student("Jupiter", 79)]
AList.sort(reverse=True)
print(AList)
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def Setting_ratings(self,lecturer,course,l_grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [l_grade]
            else:
                lecturer.grades[course] = [l_grade]
        else:
            return 'Ошибка'
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_Reviewers = Reviewer('Some','Buddy')
cool_Reviewers.courses_attached += ['Python']

lecturer = Lecturer('Oleg','Bob')
lecturer.courses_attached += ['Python']

best_student.Setting_ratings(lecturer, 'Python', 5)

cool_Reviewers.rate_hw(best_student, 'Python', 10)
cool_Reviewers.rate_hw(best_student, 'Python', 10)
cool_Reviewers.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
print(lecturer.grades)

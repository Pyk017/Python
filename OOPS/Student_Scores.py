class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.code_score = {}

    def add_score(self, sub_code, exam_score):
        self.code_score[sub_code] = exam_score   # adding the pair of subjects code as string and exam score as integer
        return self.code_score                   # to the dictionary code_score

    def print_score(self):
        print(self.name, self.code_score)    # Printing the name of the student with its Score dictionary

    def get_best_exam_score(self):      # Sorting in descending order by score by using lambda expression and print the
        ls = list(sorted(self.code_score.items(), key=lambda x: (x[1], x[0]), reverse=True))    # first element
        return ls[0][0]

    def get_failed_modules(self):
        for i, j in self.code_score.items():  # For looping through dictionary elements I use .items() method over dict.
            if j < 40:
                print(i, end=" ")


student = Student(input("Enter Name of the Student :- "), int(input("Enter Roll Number of the Student :- ")))
student.add_score('RCS-501', 65)
student.add_score('RCS-502', 35)
student.add_score('RCS-503', 85)
student.add_score('RAS-501', 95)
student.print_score()
student.get_best_exam_score()
student.get_failed_modules()

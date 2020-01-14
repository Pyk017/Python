class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
        self.__course_id = None
        self.__fees = None
        self.__discount = None

    def set_student_id(self, id):
        self.__student_id = id

    def get_student_id(self):
        return self.__student_id

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def get_course_id(self):
        return self.__course_id

    def validate_marks(self):
        return True if self.__marks >=0 and self.__marks <= 100 else False

    def validate_age(self):
        return True if self.__age > 20  else False

    def check_qualification(self):
        return True if self.validate_age() and self.validate_marks() and self.__marks >= 65 else False

    def choose_course(self, course_id):
        if self.check_qualification():
            self.__course_id = course_id
            if self.__course_id == 1001:
                self.__fees = 25575
            elif self.__course_id == 1002:
                self.__course_id = 15500
            else:
                print("Invalid Course ID.")

            if self.__marks > 85 :
                self.__discount = self.__fees - (0.25 * self.__fees)

            return True

        return False


maddy=Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(65)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")

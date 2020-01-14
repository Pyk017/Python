class Instructor:
    def __init__(self, instructor_name, technology_skill, experience, avg_feedback):
        self.__instructor_name = instructor_name
        self.__technology_skill = technology_skill
        self.__experience = experience
        self.__avg_feedback = avg_feedback

    def check_eligibility(self):
        if (self.__experience > 3) and (self.__avg_feedback >= 4.5):
            return True

        elif (self.__experience <= 3) and (self.__avg_feedback >= 4):
            return True

        return False

    def allocate_course(self, technology):
        if self.check_eligibility() and technology in self.__technology_skill:
            return True

        return False

instrust = Instructor("Prakhar Kumar", ['JAVA', "C++"], 4, 4.5)
print(instrust.allocate_course('C++'))

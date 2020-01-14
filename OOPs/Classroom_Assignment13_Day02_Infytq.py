class Classroom:
    classroom_list = ['S12', 'D11', 'D12', 'D13', 'D14', 'E13', 'B23']

    @staticmethod
    def search_classroom(class_room):
        if class_room in Classroom.classroom_list:
            return "Found"
        return -1

classroom = Classroom()
print (Classroom.search_classroom('b23'.upper()))

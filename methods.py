class Student:
    id_number = 0

    def __init__(self):
        Student.id_number += 1
        self.name = ''

    @staticmethod
    def utility():
        print(Student.id_number)
        print('Im here to help you')

    @staticmethod`
    def print_me(self):
        Student.utility()
        print('me')

    @classmethod
    def print_id(cls):
        print(cls.id_number)


s1 = Student()
Student.print_id()
s2 = Student()
Student.print_id()
#utility()
Student.utility()

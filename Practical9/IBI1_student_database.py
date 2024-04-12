class students(object):
    def __init__(self,name,major,portfolio,group,exam):
        self.name = name
        self.major = major
        self.portfolio=portfolio
        self.group=group
        self.exam=exam
    def print_details(self):
        detail=f"Student Name: {self.name}, Major: {self.major}, Code Portfolio Score: \
            {self.portfolio}, Group Project Score: {self.group}, Exam Score: {self.exam}"
        return detail
student_instance = students("Bob", "BMS", "99", "98", "97")
print(student_instance.print_details())


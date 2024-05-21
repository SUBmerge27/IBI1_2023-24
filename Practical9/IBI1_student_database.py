class students(object):# Define a class named 'students' to store and print student information
    def __init__(self,name,major,portfolio,group,exam): # Initializer method to set properties when creating an instance of a class
# Student's name
# Student's major can be BMI or BMS
# Student's code portfolio score
# Students' group project scores
# Students' test scores
        self.name = name
        self.major = major
        self.portfolio=portfolio
        self.group=group
        self.exam=exam
    def print_details(self):# Define a method for printing student details
        # Format string that contains all information about the student
        detail=f"Student Name: {self.name}, Major: {self.major}, Code Portfolio Score: \
            {self.portfolio}, Group Project Score: {self.group}, Exam Score: {self.exam}"
        return detail
    #Create an instance of the 'students' class, representing a student named "Bob" with a major of "BMS"
student_instance = students("Bob", "BMS", "99", "98", "97")
# Calls the instance's print_details method and prints the returned detail string
print(student_instance.print_details())


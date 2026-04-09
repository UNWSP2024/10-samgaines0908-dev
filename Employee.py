# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

#Author: Sam Gaines
#Date: 3/6/2026
# Title: Employee Class

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
    def display_information(self):
        print("name:", self.name)
        print("id_number:", self.id_number)
        print("department:", self.department)
        print("job_title:", self.job_title)
        print("-"*30)
        print()

employee1 = Employee("Adam", "930218", "Software Engineering","Software Architect")

employee2=Employee("Bob", "363272", "Aerospace Engineering","Propulsion Engineer ")

employee3=Employee("Sam", "394025", "Electrical Engineering", "Audio Circuit Designer")

employee4=Employee("Mason", "363272", "Business", "Business management")

employee1.display_information()

employee2.display_information()

employee3.display_information()

employee4.display_information()
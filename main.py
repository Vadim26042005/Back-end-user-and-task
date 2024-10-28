from asyncio import Task
from datetime import datetime
current_year = datetime.now().year

class Car:
    def __init__(self,make,model,year,transmission):
        self.make=make
        self.model=model
        self.year=year
        self.transmission=transmission

    def start_engine(self):
        print(f"the engine of {self.make} {self.model} {self.year} is starting")

    def age_auto(self):
        age_of_auto=current_year-self.year
        print(f"the age of auto is {age_of_auto}")
    
    def trans_info(self):
        print(f"car {self.make} transmission is {self.transmission}")
    
my_car1=Car("Toyota", "Corolla", 2020, "manual")
my_car2=Car("TESLA", "VPT", 2024, "automatic")
my_car1.start_engine()
my_car2.start_engine()
my_car1.age_auto()
my_car2.age_auto()
my_car1.trans_info()
my_car2.trans_info()




class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    
    def book_description(self):
        print(f"this book named {self.title} and was writen by {self.author} since {self.year}")

my_book=Book("LOTR","Some Guy",2010)
my_book.book_description()


class Student:
    def __init__(self,name,grade,subject):
        self.name=name
        self.grade=grade
        self.subject=subject
    
    def display_info(self):
        print(self.name, self.grade, self.subject)

info_student=Student("Vadim", "BTS", "SIO")
info_student.display_info()
        
       
class Dog:
    species = "Canine"

    def __init__(self, name, age,):
        self.name = name
        self.age = age

   
    def bark(self):
        year=self.age*7
        print(f"{self.name} is {self.age} and in dogs year its {year}")


dog1 = Dog("Buddy", 3,)
dog1.bark()  
       

#Create an object of tasks     in one task i have a name      created date    an user id     a duration   an object of user   and the user have a name and an id     mark date 


class Tasks:
    def __init__(self, name, created_date, id, duration, user_object, mark_date):
        self.name = name
        self.created_date = created_date
        self.id = id
        self.duration = duration
        self.user_object = user_object
        self.mark_date = mark_date

    def display_data(self):
        print(f"Data: {self.name}, {self.created_date}, {self.id}, {self.duration}, {self.user_object}, {self.mark_date}")

info_task = Tasks("Job", "05/01/2024", 12604, "3 months", "Clone", "Global")
info_task.display_data()


#create a gihub repository for the back end      the back end will have a objects 
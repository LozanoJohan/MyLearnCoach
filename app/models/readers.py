import json
from cursos import *

class CoursesReader:
    def __init__(self):
        pass

    def get_sia_courses(self, query):
        courses = []
        # Read from json file
        with open('D:\Users\Usuario\Documents\GitHub\MyLearnCoach\app\data\courses_data.json', "r") as file:
            courses = json.load(file)
            for course in courses['SIACourses']:
                SIACourse(course['name'], course['professor'], course['description'], course['id'], course['credits'], course['type'])
                
        return courses
        
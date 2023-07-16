from models.course import Course
import json

class Group:
    '''
    Grupo de horarios en el SIA
    ejemplo: Grupo 1, Lunes a Viernes, Martes y Jueves, Prof. Juan
    '''

    def __init__(self, id:int, schedule:str, professor:str):
        self.id = id
        self.schedule = schedule
        self.professor = professor

class SIACourse(Course):
    
    def __init__(self, name, groups, description, code, credits, type):
        super().__init__(name, description)
        
        self.groups = groups
        self.code = code
        self.credits = credits
        self.type = type
    
    
    def __str__(self):
        return super().__str__() + f' - {self.code} - {self.credits} - {self.type}'
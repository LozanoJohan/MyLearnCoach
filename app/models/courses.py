import json

# ---- Modelos de cursos ----

class Course:
    '''Superclase de cursos de coursera y del SIA'''

    def __init__(self, name, professor, description):
        self.name = name
        self.professor = professor
        self.description = description

    def __str__(self):
        return f'{self.name} - {self.professor} - {self.description}'

class CourseraCourse(Course):
    '''Modelo de curso de coursera'''

    def __init__(self, name, professor, description, url, skills, score, reviews):
        super().__init__(name, professor, description)

        self.url = url
        self.skills = skills
        self.score = score
        self.reviews = reviews

    def to_json(self):
        '''Convierte un objeto de tipo Course de coursera a un json
        return: json de Course de coursera
        '''
        
        return json.dumps(self.__dict__)

class SIACourse(Course):
    def __init__(self, name, professor, description, code, credits, type):
        super().__init__(name, professor, description)

        self.code = code
        self.credits = credits
        self.type = type
    
    def to_json(self):
        '''Convierte un objeto de tipo Course de coursera a un json
        return: json de Course de coursera
        '''
        
        return json.dumps(self.__dict__)
    
    def __str__(self):
        return super().__str__() + f' - {self.code} - {self.credits} - {self.type}'
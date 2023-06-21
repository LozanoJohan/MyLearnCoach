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

    def __init__(self, name, professor, description, url, skills, score, duration):
        super().__init__(name, professor, description)

        self.url = url
        self.skills = skills
        self.score = score
        self.duration = duration
    
    def from_json(json_data):
        '''Convierte un json a un objeto de tipo Course de coursera
        json_data: json a convertir
        return: Course de coursera
        '''

        data = json.loads(json_data)
        return CourseraCourse(data['name'], data['professor'], data['description'], data['url'], data['skills'], data['score'], data['duration'])

    def to_json(self):
        '''Convierte un objeto de tipo Course de coursera a un json
        return: json de Course de coursera
        '''
        
        return json.dumps(self.__dict__)

class SIACourse(Course):
    def __init__(self, name, professor, description, id, credits, type):
        super().__init__(name, professor, description)

        self.id = id
        self.credits = credits
        self.type = type
    
    def from_json(json_data):
        '''Convierte un json a un objeto de tipo Course del SIA
        json_data: json a convertir
        return: Course de coursera
        '''

        data = json.loads(json_data)
        return SIACourse(data['name'], data['professor'], data['description'], data['id'], data['credits'], data['type'])
    
    def to_json(self):
        '''Convierte un objeto de tipo Course de coursera a un json
        return: json de Course de coursera
        '''
        
        return json.dumps(self.__dict__)
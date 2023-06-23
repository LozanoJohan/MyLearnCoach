import json

from models.course import Course

class CourseraCourse(Course):
    '''Modelo de curso de coursera'''

    def __init__(self, name, professor, description, url, skills, score, reviews):
        super().__init__(name, description)

        self.url = url
        self.skills = skills
        self.score = score
        self.reviews = reviews

    def to_json(self):
        '''Convierte un objeto de tipo Course de coursera a un json
        return: json de Course de coursera
        '''
        
        return json.dumps(self.__dict__)
from models.course import Course


class CourseraCourse(Course):
    '''Modelo de curso de coursera'''

    def __init__(self, name, professor, description, url, skills, score, reviews):
        super().__init__(name, description)

        self.url = url
        self.professor = professor
        self.skills = skills
        self.score = score
        self.reviews = reviews
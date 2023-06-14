from curso import Curso

class CursoCoursera(Curso):
    def __init__(self, name, professor, description, url, skills, score, duration):
        super().__init__(name, professor, description)

        self.url = url
        self.skills = skills
        self.score = score
        self.duration = duration
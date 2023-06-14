from curso import Curso

class CursoSia(Curso):
    def __init__(self, name, professor, description, id, credits, type):
        super().__init__(name, professor, description)

        self.id = id
        self.credits = credits
        self.type = type
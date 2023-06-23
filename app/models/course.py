
# ---- Modelos de cursos ----

class Course:
    '''Superclase de cursos de coursera y del SIA'''

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name} - {self.description}'
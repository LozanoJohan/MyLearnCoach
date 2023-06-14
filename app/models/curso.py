class Curso:
    def __init__(self, name, professor, description):
        self.name = name
        self.professor = professor
        self.description = description

    def __str__(self):
        return f'{self.name} - {self.professor} - {self.description}'
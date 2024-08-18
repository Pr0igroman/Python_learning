class Student:
    def __init__(self, name):
        self.name = name
        self.notebook = self.Notebook

    def winner(self):
        return print(
            f"{self.name} => {self.notebook.manufactured()}, {self.notebook.model()}, {self.notebook.memory()}")

    class Notebook:
        @staticmethod
        def manufactured():
            return "HP"

        @staticmethod
        def model():
            return "I7"

        @staticmethod
        def memory():
            return "16"


first_winner = Student("Maxim")
first_winner.winner()

second_winner = Student("Vladimir")
second_winner.winner()

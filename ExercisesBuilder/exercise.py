import datetime


class Exercise:

    def __init__(self):
        self.data = datetime.date.today()
        self.exercise = ""
        self.reps = ""
        self.weight = ""
        self.difficulty = ""
        self.restTime = ""

    def add_exercise(self, exercise_name):
        self.exercise = exercise_name
        return self

    def add_reps(self, num_reps):
        self.reps = num_reps
        return self

    def add_weight(self, total_weight):
        self.weight = total_weight
        return self

    def add_difficulty(self, perceived_difficulty):
        self.difficulty = perceived_difficulty
        return self

    def add_rest_time(self, total_rest_time):
        self.restTime = total_rest_time
        return self

    def csv_format(self):
        return [self.data, self.exercise, self.reps, self.weight, self.difficulty, self.restTime]

    def __str__(self):
        return self.data.__str__()+" "+self.exercise+" "+self.reps+" "+self.weight+" "+self.difficulty+" "+self.restTime+"\n"
import csv
import os
from ExercisesBuilder.exercise import Exercise

class FileManager:

    def __init__(self, path):
        self.save_file = "exercises_list.csv"
        self.HEADER = ['date', 'exercise', 'reps', 'weight (Kg)', 'difficulty', 'rest_time(sec)']
        file_path = os.path.join(path, self.save_file)
        if not os.path.exists(path):
            os.mkdir(path)
            self.file = open(file_path, 'w+')
            csv.writer(self.file).writerow(self.HEADER)
        else:
            if not os.path.isfile(file_path):
                self.file = open(file_path, 'w+')
                csv.writer(self.file).writerow(self.HEADER)
            else:
                self.file = open(file_path, 'a')

    def write_element(self, exercise):
        csv.writer(self.file).writerow(exercise.csv_format())

    def close_file(self):
        self.file.close()

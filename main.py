from ExercisesBuilder.exercise import Exercise
from FileManager.file_manager import FileManager
import csv
import os

PATH = 'C:/Users/Public/GymTrakerData'
HEADER = ['date', 'exercise', 'reps', 'weight (Kg)', 'difficulty', 'rest_time(sec)']

if __name__ == '__main__':
    fm = FileManager(path=PATH)
    selection = input("#####################\nWelcome to GymTracker\n#####################\nDo you want to register a new exercise? [Y/N]:").upper()
    while selection == "Y":
        exercise = Exercise().add_exercise(input("Name of the exercise:")).add_weight(input("Weight:")).add_reps(input("Number of reps:")).add_difficulty(input("Difficulty perceived for the exercise:")).add_rest_time(input("Total rest time after:"))
        print("Exercises added.")
        fm.write_element(exercise=exercise)
        selection = input("Do you want to insert a new exercise? [Y/N]:")
    fm.close_file()
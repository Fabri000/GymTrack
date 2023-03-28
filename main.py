from Objects.exercise import Exercise
import csv
import os

PATH = "D:\\exercise.csv"
HEADER = ['date', 'exercise', 'reps', 'weight (Kg)', 'difficulty', 'rest_time(sec)']

if __name__ == '__main__':
    if not os.path.isfile(PATH):
        f = open(PATH, 'w+')
        writer = csv.writer(f)
        writer.writerow(HEADER)
    else:
        f = open(PATH, 'w')
        writer = csv.writer(f)
    selection = input("#####################\nWelcome to GymTracker\n#####################\nDo you want to register a new exercise? [Y/N]:").upper()
    while selection == "Y":
        exercise = Exercise().add_exercise(input("Name of the exercise:")).add_weight(input("Weight:")).add_reps(input("Number of reps:")).add_difficulty(input("Difficulty perceived for the exercise:")).add_rest_time(input("Total rest time after:"))
        print("Exercises added.")
        writer.writerow(exercise.csv_format())
        selection = input("Do you want to insert a new exercise? [Y/N]:")
    f.close()
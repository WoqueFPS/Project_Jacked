import csv
import os

class Storage:
    def __init__(self):
        self.workout_file = "data/workouts.csv"
        self.exercise_file = "data/exercises.csv"

        os.makedirs("data", exist_ok=True)

    def save_exercise(self, exercise):
        with open(self.exercise_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([exercise.name, exercise.sets, exercise.reps, exercise.weight])

    def save_workout(self, workout):
        with open(self.workout_file, "a", newline="") as f:
            writer = csv.writer(f)
            for ex in workout.exercises:
                writer.writerow([workout.date, ex.name, ex.sets, ex.reps, ex.weight])

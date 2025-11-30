import csv

class Storage:
    def __init__(self, filename="data/workouts.csv"):
        self.filename = filename

    def save_workout(self, workout):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            for ex in workout.exercises:
                writer.writerow([workout.date, ex.name, ex.sets, ex.reps, ex.weight])

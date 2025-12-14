import csv
import os

class Storage:
    def __init__(self):
        #data directory en file paths
        self.data_dir = "data"
        os.makedirs(self.data_dir, exist_ok=True)
        self.workout_file = os.path.join(self.data_dir, "workouts.csv")
        self.exercise_file = os.path.join(self.data_dir, "exercises.csv")

        #maak CSV files aan als ze nog niet bestaan
        if not os.path.exists(self.exercise_file):
            with open(self.exercise_file, "w", newline="") as f:
                csv.writer(f).writerow(["name", "sets", "reps", "weight"])
        if not os.path.exists(self.workout_file):
            with open(self.workout_file, "w", newline="") as f:
                csv.writer(f).writerow(["date", "name", "sets", "reps", "weight"])

    def save_exercise(self, exercise):
        with open(self.exercise_file, "a", newline="") as f:
            csv.writer(f).writerow([exercise.name, exercise.sets, exercise.reps, exercise.weight])

    def save_workout(self, workout):
        with open(self.workout_file, "a", newline="") as f:
            writer = csv.writer(f)
            for ex in workout.exercises:
                writer.writerow([workout.date, ex.name, ex.sets, ex.reps, ex.weight])

    def load_exercises(self):
        exercises = []
        try:
            with open(self.exercise_file, "r", newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    exercises.append((
                        row["name"],
                        int(row["sets"]),
                        int(row["reps"]),
                        float(row["weight"])
                    ))
        except FileNotFoundError:
            return []

        return exercises

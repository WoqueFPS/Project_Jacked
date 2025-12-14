import csv
import os

class Storage:
    def __init__(self):
        self.data_dir = "data"
        os.makedirs(self.data_dir, exist_ok=True)

        self.workout_file = os.path.join(self.data_dir, "workouts.csv")
        self.exercise_file = os.path.join(self.data_dir, "exercises.csv")

        # Zorg dat de files een header hebben als ze nieuw zijn
        if not os.path.exists(self.exercise_file):
            with open(self.exercise_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "sets", "reps", "weight"])

        if not os.path.exists(self.workout_file):
            with open(self.workout_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["date", "name", "sets", "reps", "weight"])

    def save_exercise(self, exercise):
        with open(self.exercise_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([exercise.name, exercise.sets, exercise.reps, exercise.weight])

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
                    # converteer naar juiste types waar nodig
                    try:
                        name = row.get("name") or row.get("exercise") or row.get("Naam") or row.get("naam")
                        sets = int(row.get("sets", 0))
                        reps = int(row.get("reps", 0))
                        weight = float(row.get("weight", 0))
                    except (ValueError, TypeError):
                        # Als conversie faalt, sla dit record over
                        continue
                    exercises.append((name, sets, reps, weight))
        except FileNotFoundError:
            # Bestand bestaat nog niet
            return []

        return exercises

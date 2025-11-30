class Workout:
    def __init__(self, date):
        self.date = date
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def __repr__(self):
        return f"Workout on {self.date} with {len(self.exercises)} exercises"

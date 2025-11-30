class Exercise:
    def __init__(self, name, sets, reps, weight):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight

    def __repr__(self):
        return f"{self.name} - {self.sets}x{self.reps} @ {self.weight}kg"

from exercises import Exercise
from workouts import Workout
from storage import Storage

storage = Storage()

def add_exercise_interactive():
    print("=== Oefening toevoegen ===")

    # Error handling (lege input of verkeerde input)
    name = input("Naam oefening: ").strip()
    if name == "":
        print("FOUT: Naam mag niet leeg zijn.")
        return None

    try:
        sets = int(input("Sets: "))
        reps = int(input("Reps: "))
        weight = float(input("Gewicht (kg): "))
    except ValueError:
        print("FOUT: Voer een geldig nummer in.")
        return None

    exercise = Exercise(name, sets, reps, weight)
    print("Oefening toegevoegd:", exercise)
    return exercise

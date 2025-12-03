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

def log_workout():
    date = input("Datum van workout (bijv 2025-03-01): ")

    workout = Workout(date)

    while True:
        ex = add_exercise_interactive()
        if ex:
            workout.add_exercise(ex)

        doorgaan = input("Nog een oefening toevoegen? (y/n): ").lower()
        if doorgaan != "y":
            break

    # Opslaan in CSV
    storage.save_workout(workout)

    print("Workout succesvol opgeslagen!")

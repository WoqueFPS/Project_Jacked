from exercises import Exercise
from workouts import Workout
from storage import Storage

storage = Storage()

def add_exercise_interactive(save=True):
    print("Exercise toevoegen")

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

    if save:
        storage.save_exercise(exercise)
        print("Oefening opgeslagen in exercises.csv")

    return exercise

def log_workout():
    date = input("Datum van workout (bijv 2025-03-01): ")

    workout = Workout(date)

    while True:
        add = add_exercise_interactive(save=False)
        if add:
            workout.add_exercise(add)
        doorgaan = input("Nog een oefening toevoegen? (y/n): ").lower()
        if doorgaan != "y":
            break

    storage.save_workout(workout)
    print("Workout succesvol opgeslagen!")

def show_exercises():
    exercises = storage.load_exercises()

    if not exercises:
        print("Geen oefeningen om te tonen.")
        return

    print("\nOpgeslagen oefeningen:")
    print("----------------------------")

    for i, (name, sets, reps, weight) in enumerate(exercises, start=1):
        print(f"{i}. {name} - {sets} sets, {reps} reps, {weight}kg")

def main():
    while True:
        print("\nGym Progress")
        print("1. Oefening toevoegen")
        print("2. Workout loggen")
        print("3. Oefeningen bekijken")
        print("4. Stoppen")

        keuze = input("Maak een keuze: ").strip()

        if keuze == "1":
            add_exercise_interactive()
        elif keuze == "2":
            log_workout()
        elif keuze == "3":
            show_exercises()
        elif keuze == "4":
            print("Programma afgesloten.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main()

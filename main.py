from exercises import Exercise
from workouts import Workout
from storage import Storage

storage = Storage()

def add_exercise_interactive():
    print("Exercise toevoegen")

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
        add = add_exercise_interactive()
        if add:
            workout.add_exercise(add)
        doorgaan = input("Nog een oefening toevoegen? (y/n): ").lower()
        if doorgaan != "y":
            break
    # Opslaan in CSV
    storage.save_workout(workout)
    print("Workout succesvol opgeslagen!")

def main():
    while True:
        print("Gym Progress")
        print("1. Oefening toevoegen")
        print("2. Workout loggen")
        print("3. Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            add_exercise_interactive()
        elif keuze == "2":
            log_workout()
        elif keuze == "3":
            print("Programma afgesloten.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main()

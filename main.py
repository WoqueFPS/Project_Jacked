from exercises import Exercise
from workouts import Workout
from storage import Storage

storage = Storage()

def add_exercise():
    print("Add Exercise")
    name = input("Exercise name: ")
    
    if name == "":
        print("Naam kan niet leeg zijn")
        return
    
    try:
        sets = int(input("Sets: "))
        reps = int(input("Reps: "))
        weight = float(input("Weight (kg): "))
    except:
        print("voer alleen nummers in")
        return
    
    exercise = Exercise(name, sets, reps, weight)
    storage.save_exercise(exercise)
    print(f"Exercise '{name}' saved!")

def log_workout():
    print("Log Workout")
    date = input("Date (e.g. 14-12-2025): ")
    workout = Workout(date)
    
    keep_adding = True
    while keep_adding == True:
        name = input("Exercise name: ")
        if name == "":
            print("Naam kan niet leeg zijn")
            continue
        
        try:
            sets = int(input("Sets: "))
            reps = int(input("Reps: "))
            weight = float(input("Weight (kg): "))
        except:
            print("Voer alleen nummers in")
            continue
        
        exercise = Exercise(name, sets, reps, weight)
        workout.add_exercise(exercise)
        print(f"'{name}' added!")
        
        answer = input("\nAdd another? (yes/no): ")
        if answer.lower() != "yes":
            keep_adding = False
    
    storage.save_workout(workout)
    print("Workout saved!")

def view_exercises():
    print("My Exercises")
    exercises = storage.load_exercises()
    
    if len(exercises) == 0:
        print("No exercises yet.")
        return
    
    number = 1
    for ex in exercises:
        print(f"\n{number}. {ex[0]}")
        print(f"   Sets: {ex[1]} | Reps: {ex[2]} | Weight: {ex[3]} kg")
        number = number + 1

def main():
    print("\n" + "="*40)
    print("GYM PROGRESS TRACKER")
    print("="*40)
    
    running = True
    while running == True:
        print("1. Add exercise")
        print("2. Log workout")
        print("3. View exercises")
        print("4. Quit")
        
        choice = input("Choose (1-4): ")
        
        if choice == "1":
            add_exercise()
        elif choice == "2":
            log_workout()
        elif choice == "3":
            view_exercises()
        elif choice == "4":
            print("Thanks for using Gym Progress Tracker!")
            running = False
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
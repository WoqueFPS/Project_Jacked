import unittest
import os
from storage import Storage
from exercises import Exercise

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.storage = Storage()
        self.storage.exercise_file = "data/test_exercises.csv"

        #Maak een test CSV aan met header
        with open(self.storage.exercise_file, "w") as f:
            f.write("name,sets,reps,weight\n")

    def tearDown(self):
        #verwijder test file na elke test
        if os.path.exists(self.storage.exercise_file):
            os.remove(self.storage.exercise_file)

    def test_save_exercise(self):
        #test of we een oefening kunnen opslaan
        exercise = Exercise("Bench Press", 3, 8, 80)
        self.storage.save_exercise(exercise)

        #checkt of het echt in het bestand staat
        with open(self.storage.exercise_file, "r") as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 2)
        self.assertIn("Bench Press", lines[1])

    def test_load_exercises(self):
        #Voeg handmatig eerst een oefening toe aan het bestand
        with open(self.storage.exercise_file, "a") as f:
            f.write("Squat,4,6,120\n")

        #Laad de oefeningen in
        exercises = self.storage.load_exercises()

        #Check of we 1 oefening terug krijgen
        self.assertEqual(len(exercises), 1)
        self.assertEqual(exercises[0][0], "Squat")
        self.assertEqual(exercises[0][3], 120.0)  # Gewicht moet float zijn

if __name__ == "__main__":
    unittest.main()
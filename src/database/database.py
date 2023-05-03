import csv
from database.question import Question
import random


class Database:
    """Luokka joka sisältää pelin kysymykset
    """

    def __init__(self):
        """Luokkaan on tallennettu listana kaiki pelin kysymykset

        Args:
            file_path (str): polku CSV-tiedostoon, joka sisältää kysymykset
        """
        self.questions = []
        file_path = "src/database/questionsdb.csv"
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                text = row[0]
                answers = row[1:5]
                random.shuffle(answers)
                correct_answer = row[5]
                question = Question(text, answers, correct_answer)
                self.questions.append(question)

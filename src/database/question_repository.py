import csv
from database.question import Question
import random


class QuestionRepository:
    """Luokka joka lukee kysymykset tiedostosta ja alustaa ne helpommin käsiteltävään muotoon
    """

    def __init__(self):
        """Luokkaan on tallennettu listana kaiki pelin kysymykset

        """
        self.questions = []
        file_path = "src/database/questions_db.txt"
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                text = row["text"]
                answers = [row["answer1"], row["answer2"],
                           row["answer3"], row["answer4"]]
                random.shuffle(answers)
                correct_answer = row["correct_answer"]
                question = Question(text, answers, correct_answer)
                self.questions.append(question)

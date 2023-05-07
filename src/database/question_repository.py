import csv
import random
from database.question import Question


class QuestionRepository:
    """Luokka joka lukee kysymykset tiedostosta ja alustaa ne helpommin käsiteltävään muotoon
    """

    def __init__(self, file_path):
        """ Luokan konstruktori, joka tallentaa kysymyseket Question-oliona listaan

        Args:
            file_path (str): polku tiedostoon, jossa on pelin kysymykset
        """
        self.questions = []
        self.file_path = file_path
        self.read_questions_from_file()

    def read_questions_from_file(self):
        """Avaa tiedoston ja käy sen läpi. Vastausvaihtoehtojen järjestys sekoitetaan,
           jotta ne eivät ole samassa aina kohdassa. Tiedoston riveistä muodostetaan
           Question-oliota, jotka lisätään listaan.
        """
        with open(self.file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                text = row["text"]
                answers = [row["answer1"], row["answer2"],
                           row["answer3"], row["answer4"]]
                random.shuffle(answers)
                correct_answer = row["correct_answer"]
                question = Question(text, answers, correct_answer)
                self.questions.append(question)

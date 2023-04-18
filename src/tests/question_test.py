import unittest
from question import Question


class TestQuestion(unittest.TestCase):
    def setUp(self):
        text = "What is the capital of France?"
        answers = ["London", "Paris", "Berlin", "Madrid"]
        correct_answer = 1
        self.q = Question(text, answers, correct_answer)

    def test_correct_answer(self):
        self.assertEqual(self.q.correct_answer, self.q.answers.index("Paris"))

    def test_wrong_answer(self):
        self.assertNotEqual(self.q.correct_answer,
                            self.q.answers.index("Berlin"))

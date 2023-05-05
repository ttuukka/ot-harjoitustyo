import unittest
from database.question_repository import QuestionRepository


class TestQuestionRepository(unittest.TestCase):
    def setUp(self):
        self.repo = QuestionRepository()

    def test_question_text(self):
        for question in self.repo.questions:
            self.assertIsNotNone(question.text)
            self.assertNotEqual(question.text, "")

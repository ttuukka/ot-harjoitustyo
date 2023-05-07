import unittest
from database.question import Question
from database.question_repository import QuestionRepository


class TestQuestionRepository(unittest.TestCase):
    def setUp(self):
        self.question_repo = QuestionRepository(
            "src/tests/testfile_questions.txt")

    def test_read_questions_from_file(self):
        self.assertEqual(len(self.question_repo.questions), 3)
        self.assertIsInstance(self.question_repo.questions[0], Question)
        self.assertEqual(
            self.question_repo.questions[0].text, 'What is the smallest planet in our solar system?')
        self.assertCountEqual(self.question_repo.questions[0].answers, [
            'Mercury', 'Venus', 'Mars', 'Jupiter'])
        self.assertEqual(
            self.question_repo.questions[0].correct_answer, 'Mercury')
        self.assertIsInstance(self.question_repo.questions[1], Question)
        self.assertEqual(
            self.question_repo.questions[1].text, 'What is the largest mammal on Earth?')
        self.assertCountEqual(self.question_repo.questions[1].answers, [
            'Blue Whale', 'Elephant', 'Giraffe', 'Hippopotamus'])
        self.assertEqual(
            self.question_repo.questions[1].correct_answer, 'Blue Whale')
        self.assertIsInstance(self.question_repo.questions[2], Question)
        self.assertEqual(
            self.question_repo.questions[2].text, 'What is the currency of India?')
        self.assertCountEqual(self.question_repo.questions[2].answers, [
            'Rupee', 'Dollar', 'Euro', 'Pound'])
        self.assertEqual(
            self.question_repo.questions[2].correct_answer, 'Rupee')

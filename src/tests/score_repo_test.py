import unittest
from database.score_repository import ScoreRepository
import os


class TestScoreRepository(unittest.TestCase):

    def setUp(self):
        self.file_path = "src/tests/testfile.txt"
        self.repository = ScoreRepository(self.file_path)

    def test_save_score_and_get_top10(self):
        self.repository.save_score("testi1", 10, "normal")
        self.repository.save_score("testi2", 20, "normal")
        self.repository.save_score("testi3", 30, "normal")
        self.repository.save_score("testi4", 5, "normal")
        self.repository.save_score("testi5", 25, "normal")
        self.repository.save_score("testi6", 60, "normal")
        self.repository.save_score("testi7", 70, "normal")
        self.repository.save_score("testi8", 80, "normal")
        self.repository.save_score("testi9", 900, "normal")
        self.repository.save_score("testi10", 100, "normal")
        self.repository.save_score("testi11", 2, "normal")
        self.repository.save_score("testi1", 10.5, "time")
        self.repository.save_score("testi2", 12.5, "time")
        self.repository.save_score("testi3", 13.5, "time")
        self.repository.save_score("testi4", 14.5, "time")
        self.repository.save_score("testi5", 11.5, "time")
        self.repository.save_score("testi6", 16.5, "time")
        self.repository.save_score("testi7", 100.5, "time")
        self.repository.save_score("testi8", 100.9, "time")
        self.repository.save_score("testi9", 1.5, "time")
        self.repository.save_score("testi10", 0, "time")
        self.repository.save_score("testi11", 0, "time")

        normal_scores, time_scores = self.repository.get_top10_scores()
        self.assertEqual(normal_scores, ["testi9 - 900", "testi10 - 100", "testi8 - 80", "testi7 - 70",
                         "testi6 - 60", "testi3 - 30", "testi5 - 25", "testi2 - 20", "testi1 - 10", "testi4 - 5"])
        self.assertEqual(time_scores, ["testi8 - 100.9", "testi7 - 100.5", "testi6 - 16.5",
                         "testi4 - 14.5", "testi3 - 13.5", "testi2 - 12.5", "testi5 - 11.5", "testi1 - 10.5", "testi9 - 1.5", "testi10 - 0.0"])

    def tearDown(self):
        os.remove(self.file_path)

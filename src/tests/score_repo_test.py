import unittest
from unittest.mock import mock_open, patch
from database.score_repository import ScoreRepository
import csv
from pathlib import Path


class TestScoreRepository(unittest.TestCase):

    def setUp(self):
        self.repository = ScoreRepository()
        self.filename = Path("src/tests/testfile.txt")
        header = ["name", "score", "mode"]
        with open(self.filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)

        self.repository.file_path = self.filename

    def test_get_top10_scores(self):

        mock_file = mock_open(read_data="name,score,mode\n"
                              "Eka,100,normal\n"
                              "TOka,50.77,time\n"
                              "Kolmas,200,normal\n"
                              "Neljäs,75.28,time\n")

        with patch('builtins.open', mock_file):

            normal_scores, time_scores = self.repository.get_top10_scores()

            self.assertEqual(normal_scores, ["Kolmas - 200", "Eka - 100"])
            self.assertEqual(time_scores, ["Neljäs - 75.28", "TOka - 50.77"])

    def test_save_score(self):
        self.repository.save_score("eka", 10, "normal")
        self.repository.save_score("toka", 20, "normal")
        normal_scores, time_scores = self.repository.get_top10_scores()
        self.assertEqual(normal_scores, ["toka - 20", "eka - 10"])

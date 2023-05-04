import csv
from pathlib import Path


class ScoreRepository:

    def __init__(self):
        self.file_path = Path("src/database/high_scores.txt")

    def get_top10_scores(self):
        normal_scores = []
        time_scores = []
        with open(self.file_path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row["name"]
                score = int(row["score"]) if row["mode"] == "normal" else float(
                    row["score"])
                mode = row["mode"]
                if mode == "normal":
                    normal_scores.append(f"{name} - {score}")
                elif mode == "time":
                    time_scores.append(f"{name} - {score}")

        normal_scores = sorted(normal_scores, key=lambda x: int(
            x.split(" - ")[1]), reverse=True)[:10]
        time_scores = sorted(time_scores, key=lambda x: float(
            x.split(" - ")[1]), reverse=True)[:10]
        return normal_scores, time_scores

    def save_score(self, name, score, mode):
        with open(self.file_path, "a", newline='') as csvfile:
            csvfile.seek(0)
            writer = csv.writer(csvfile)
            writer.writerow([name, score, mode])

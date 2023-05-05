import csv
from pathlib import Path


class ScoreRepository:
    """Luokka joka hoitaa tuloksien tallentamisen ja 10 parhaan tuloksen rajaamisen ja järjestelyn
    """

    def __init__(self):
        """Alustetaan tiedosto, johon tulokset tallennetaan
        """
        self.file_path = Path("src/database/high_scores.txt")
        header = ["name", "score", "mode"]
        if not self.file_path.exists():
            with open(self.file_path, "w", newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(header)

    def get_top10_scores(self):
        """Lukee tiedostosta tallennetetut tulokset ja jakaa ne pelimuodon mukaan

        Returns:
            Lista: Palauttaa kaksi listaa,
            joissa on molempien pelimuotojen 10 parasta tulosta ja nimierkit
        """
        normal_scores = []
        time_scores = []
        with open(self.file_path, "r", encoding='utf-8') as csvfile:
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
        """Tallentaa valmiiseen tiedostoon pelaajan tuloksen

        Args:
            name (str): pelaajan antama nimi
            score (float): pelaajan keräämät pisteet
            mode (str): pelimuoto, jolla peli pelattiin
        """
        with open(self.file_path, "a", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, score, mode])

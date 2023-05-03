import random
from pathlib import Path
from database.high_score import HighScore


class Logic:

    """Luokka joka sisältää pelin logiikan. 


    """

    def __init__(self, question_db):
        """Luokan konstruktori, joka luo uuden "peli-instanssin"

        Args:
            question_db : Pelin kysymykset
            score : pelaajan tämän hetkiset pisteet
            question : tämän hetkinen kysymys sisältäen itse kysymyksen, vastausvaihtoehdot, sekä oikean vastauksen
            asked_questions : pelaajalta jo kysytyt kysymykset
            game_over: Kertoo onko peli edennyt loppuun
        """
        self.question_db = set(question_db)
        self.score = 0
        self.question = None
        self.asked_questions = set()
        self.game_over = False

    def get_correct_answer(self):
        """Palauttaa Questions-luokan kautta tämän hetkisen kysymyksen oikean vastauksen

        Returns:
            Merkkijono, joka on oikea vastaus
        """
        return self.question.correct_answer

    def get_next_question(self):
        """Aluksi tarkistaa onko uusia kysymyksiä jäljellä, jos ei niin kysymukset alkvat alusta.
        Tämän jälkeen otetaan satunnainen uusi kysymys, joka lisätään kysyttyihin kysymyksiin.


        Returns:
            Question: tämän hetken aktiivisen kysymyksen
        """
        remaining_questions = self.question_db - self.asked_questions
        if not remaining_questions:
            remaining_questions = set(self.question_db)
        self.question = random.choice(list(remaining_questions))
        self.asked_questions.add(self.question)
        return self.question

    def check_answer(self, button):
        """Tarkistaa vatauksen. 
        Tarkistus tapahtuu vertailemalla klikatun vastauspainikkeen tekstiä oikeaan vastaukseen.
        Jos vastaus on oikein, suoritetaan oikean vastauksen käsittely, muuten suoritetaan väärän vastauksen käsittely.


        Args:
            button (Button): Klikattu vastauspainike

        Returns:
            True: Jos vastaus oli oikeain
            False: Jos vastaus oli väärin
        """
        if button.text == self.get_correct_answer():
            self.handle_correct_answer()
            return True
        self.handle_incorrect_answer()
        return False

    def handle_correct_answer(self):
        """Suorittaa oikean vastauksen jälkeiset toimenpiteet.
        Kasvattaa pelaajan pisteitä
        """
        self.score += 1

    def handle_incorrect_answer(self):
        """Suorittaa väärän vastauksen jälkeiset toimenpiteet.
        Asettaa game_over "tilan" aktiviiksesi"
        """
        self.game_over = True

    def restart_game(self):
        """Alustaa uuden pelin
        """
        self.score = 0
        self.question = None
        self.asked_questions = set()
        self.game_over = False

    def save_high_score(self, player_name):
        """Tallentaa pelaajan tuloksen tiedostoon.
        Aluksi tarkistaa onko tiedosto valmiiksi luotu.
        Tämän jälkeen tallentaa sinne nimen, sekä tuloksen

        Args:
            player_name: pelaajan syöttämä nimi merkkijonona
        """
        score = HighScore(player_name, self.score)
        file_path = Path("src/database/high_scores.txt")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "a",  encoding="utf-8") as file:
            file.write(f"{str(score)}\n")
            file.flush()

    def get_top10_high_score(self):
        with open("src/database/high_scores.txt", "r", encoding="utf-8") as file:
            scores = [HighScore.from_string(score_str) for score_str in file]
        sorted_scores = sorted(scores, key=lambda s: s.score, reverse=True)
        return sorted_scores[:10]

import random
import os


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
        # self.question_index = 0
        self.question = None
        self.asked_questions = set()
        self.game_over = False
        # self.high_scores = None

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
        # self.question_index = 0
        self.question = None
        self.asked_questions = None
        self.game_over = False

    def save_high_score(self, player_name):
        """Tallentaa pelaajan tuloksen tiedostoon.
        Aluksi tarkistaa onko tiedosto valmiiksi luotu.
        Tämän jälkeen tallentaa sinne nimen, sekä tuloksen

        Args:
            player_name: pelaajan syöttämä nimi merkkijonona
        """

        file_path = "src/database/high_scores.txt"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "a",  encoding="utf-8") as file:
            file.write(f"{player_name}: {self.score}\n")
            file.flush()

    def get_top10_high_score(self):
        """Avaa tiedoston, joka sisältää tulokset.
        Tämän jälkeen käy ne läpi ja tallentaa ne listaan, jonka jälkeen järjestää 10 parasta tulosta pisteiden mukaan.


        Returns:
            Lista: lista joka sisältää 10 parasta tulosta pisteiden mukaan järjestettynä
        """
        with open("src/database/high_scores.txt", "r",  encoding="utf-8") as file:
            scores = file.readlines()
        top_scores = []
        for score in scores:
            try:
                score_parts = score.strip().split(":")
                name = str(score_parts[0].strip())
                score_value = int(score_parts[1].strip())
                top_scores.append(f"{name} : {score_value}")
            except (ValueError, IndexError):
                pass
        top_scores = sorted(top_scores, key=lambda x: int(
            x.split(" : ")[1]), reverse=True)[:10]
        return top_scores

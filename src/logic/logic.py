import random
import time


class Logic:

    """Luokka joka sisältää pelin logiikan. 


    """

    def __init__(self, question_db):
        """Luokan konstruktori, joka luo uuden "peli-instanssin"

        Args:
            question_db : Pelin kysymykset
            score : pelaajan tämän hetkiset pisteet
            question : tämän hetkinen kysymys sisältäen
            itse kysymyksen, vastausvaihtoehdot, sekä oikean vastauksen
            asked_questions : pelaajalta jo kysytyt kysymykset
            game_over: Kertoo onko peli edennyt loppuun
            game_mode: asetaan joko "normal" tai "time" riippuen kumpaa pelimuotoa pelataan
        """
        self.question_db = set(question_db)
        self.score = 0
        self.question = None
        self.asked_questions = set()
        self.game_over = False
        self.game_mode = ""
        self.start_time = None
        self.end_time = None

    def get_correct_answer(self):
        """Palauttaa Questions-luokan kautta tämän hetkisen kysymyksen oikean vastauksen

        Returns:
            Merkkijono, joka on oikea vastaus
        """
        return self.question.correct_answer

    def get_next_question(self):
        """Aluksi tarkistaa onko uusia kysymyksiä jäljellä, jos ei niin kysymukset alkvat alusta.
        Tämän jälkeen otetaan satunnainen uusi kysymys, joka lisätään kysyttyihin kysymyksiin.
        Aloittaa ajastimen kysymykselle


        Returns:
            Question: tämän hetken aktiivisen kysymyksen
        """
        remaining_questions = self.question_db - self.asked_questions
        if not remaining_questions:
            remaining_questions = set(self.question_db)
        self.question = random.choice(list(remaining_questions))
        self.asked_questions.add(self.question)
        self.start_time = self.get_time()
        return self.question

    def check_answer(self, button):
        """Tarkistaa vatauksen. 
        Tarkistus tapahtuu vertailemalla
        klikatun vastauspainikkeen tekstiä oikeaan vastaukseen.
        Jos vastaus on oikein, suoritetaan oikean vastauksen käsittely,
        muuten suoritetaan väärän vastauksen käsittely.


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
        """Suorittaa oikean vastauksen jälkeiset toimenpiteet. Lopettaa kysymyksen ajastimen
        Kasvattaa pelaajan pisteitä
        """
        self.end_time = self.get_time()
        if self.game_mode == "normal":
            self.score += 1
        else:
            time_score = 10 - (self.end_time - self.start_time)
            if time_score > 0:
                time_score = round(time_score, 2)
                self.score += time_score
                self.score = round(self.score, 2)

    def handle_incorrect_answer(self):
        """Suorittaa väärän vastauksen jälkeiset toimenpiteet.
        Asettaa game_over "tilan" aktiviiksesi"
        """
        self.game_over = True

    def restart_game(self):
        """Alustaa uuden pelin
        """
        self.game_mode = ""
        self.score = 0
        self.question = None
        self.asked_questions = set()
        self.game_over = False

    def get_time(self):
        """metodi vastausajan mittausta varten

        Returns:
            time (float): palauttaa ajan sekunneissa
        """
        return time.time()

    def set_time_game_mode(self):
        """Asettaa pelimuodoksi "time"
        """
        self.game_mode = "time"

    def set_normal_game_mode(self):
        """Asettaa pelimuodoksi "normal"
        """
        self.game_mode = "normal"

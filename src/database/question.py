

class Question:
    """Luokka, jonka avulla kysymykset on rakennettu

    """

    def __init__(self, text, answers, correct_answer):
        """Luokan konstruktori, joka luo uuden kysymykset

        Args:
            text (str): Itse kysymys, johon haetaan vastausta
            answers (list): lista, joka sisältää 4 eri vastausvaihtoehto
            correct_answer (str): oikea vastaus, joka on yksi vastaus vaihtoehdoista
        """
        self.text = text
        self.answers = answers
        self.correct_answer = correct_answer

    def __str__(self):
        return self.text

class HighScore:

    def __init__(self, player_name, score):
        self.player_name = player_name
        self.score = score

    def __str__(self):
        return f"{self.player_name}:{self.score}"

    @staticmethod
    def from_string(score_str):
        player_name, score = score_str.strip().split(':')
        return HighScore(player_name.strip(), int(score.strip()))

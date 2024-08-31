from random import randint

class VideoGame:
    def __init__(self, previous_scores = {}):
            if not isinstance(previous_scores, dict):
                  raise ValueError
            self.playes = previous_scores.keys
            self.scores = previous_scores.values
            self.games_played = 0
            self.high_score = self.high_score()

    class User:
            def __init__(self, previous_scores = []):
                  self.scores = []

            def play_game(self):
                score = randint(0, 10000000000)
                self.games_played += 1
                self.scores[self.games_played] = score
                if self.high_score < score:
                    self.high_score = (self.games_played, score)
    
    def check_high_score(self):
            return

class Score:
    lives = 3
    score = 0

@classmethod


def UpdateScore():
    Score.score += 100

@classmethod


def PopeyeDead():
    Score.lives -= 1

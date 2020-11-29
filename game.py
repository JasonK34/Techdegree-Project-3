from phrase import Phrase
import random

class Game:
    
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("Go Ahead Make My Day"), Phrase("Say Hello To My Little Friend"), Phrase("May the Force be with you"), Phrase("Hasta la vista baby"), Phrase("Yo Adrien")]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]


    def get_random_phrase(self):
        return random.choice(self.phrases)


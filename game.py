from phrase import Phrase
import random

class Game:
    
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("Go Ahead Make My Day"), Phrase("Say Hello To My Little Friend"), 
            Phrase("May the Force be with you"), Phrase("Hasta la vista baby"), Phrase("Yo Adrien")]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]


    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("\n>>>>> Welcome to Phrase Hunter! <<<<<\n")

    def start(self):
        self.welcome()
        print(f"Number Missed: {self.missed}")
        self.active_phrase.display(self.guesses)
        self.user_guess = self.get_guess()
        self.guesses.append(self.user_guess)
        if self.active_phrase.check_guess(self.user_guess):
            print("YAY")
        else:
            print("Bummer!")



    def get_guess(self):
        self.letter = input("\n\nPlease enter a letter: ")
        return self.letter
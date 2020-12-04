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
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) is False:
            print(f"Number Missed: {self.missed}")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()
            
    def get_guess(self):
        letter = input("\n\nPlease enter a letter: ")
        return letter

    def game_over(self):
        if self.missed == int(5):
            print("Sorry, you lose. GAME OVER")
        else:
            print("Great job, YOU WIN!!")



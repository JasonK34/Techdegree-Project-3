from game import Game

if __name__ == "__main__":

    def print_phrase(phrase_object):
        print(f"The phrase is: {phrase_object}")
        
    game = Game()
    print(game.active_phrase)
    print(game.active_phrase.phrase)

   
    

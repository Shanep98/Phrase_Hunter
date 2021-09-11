# Create your Game class logic in here.
from phrase import Phrase
import random


class Game():
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("Stand in a straight circle"), Phrase("Both of you stand together separately"), Phrase("I am laughing so hard glitter came out my nose"), Phrase("What the voices in my head tell me to do"), Phrase("Taste the Rainbow")
                       ]
        self.Valid_Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.active_phrase = self.get_random_phrase()
        self.guesses = [' ']

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("=============================\n  Welcome to Phrase Hunters\nLets see if you have what it takes to join us \n=============================")

    def start(self):
        while self.missed != 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f'\nNumber missed: {self.missed}')
            self.active_phrase.display(self.guesses)
            current_guess = self.get_guess()
            print(f'\nYour guess was {current_guess}')
            self.guesses.append(current_guess)
            if not self.active_phrase.check_guess(current_guess):
                self.missed += 1
            self.active_phrase.check_complete(self.guesses)
        self.game_over()
        self.restart()

    def get_guess(self):
        guess = input("\nWhat letter would you like to guess?  >")
        while guess.lower() not in self.Valid_Letters:
            print('Your guess was not valid. please try again.')
            guess = input("\nWhat letter would you like to guess?  >")
        return guess.lower()

    def game_over(self):
        if self.missed == 5:
            print('You have guess 5 incorrect letters.\nGame Lost')
        else:
            print('Congrats you have guessed the phrase. Welcome to the Phrase Hunters.')

    def restart(self):
        again = input('Would you like to try again?(yes/no)  >')
        again = again.lower()
        if again == 'yes':
            self.guesses = [' ']
            self.start()
        else:
            print('Thank you for playing.')

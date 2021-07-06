from random import randint
import sys
sys.path.append(".")
from Card import *

class Deck:
    def __init__(self, empty = False):
        self.contents = []
        if not empty:
            self.construct_deck().shuffle_deck()

    def construct_deck(self):
        suits = ["Diamonds", "Hearts", "Spades", "Clubs"]

        for suit in suits:
            for value in range(1, 14):
                rank = ""

                if value == 1:
                    rank = "Ace"
                elif value > 1 and value < 11:
                    rank = str(value)
                elif value == 11:
                    rank = "Jack"
                elif value == 12:
                    rank = "Queen"
                else:
                    rank = "King"

                self.contents.append(Card(suit, rank, value))
        return self

    def printMe(self):
        for card in self.contents:
            print(card)
        return self

    def shuffle_deck(self):
        for i in range(len(self.contents)):
             rand = randint(0, 51)
             self.contents[i], self.contents[rand] = self.contents[rand], self.contents[i]
        return self

    def draw_card(self, amount = 1):
        if len(self.contents) <= 0:
            return None
        return self.contents.pop()

    def count_cards(self):
        return len(self.contents)

    def add_card(self, card):
        self.contents.append(card)
        return self

game = True
main_deck = Deck()
main_deck.shuffle_deck().shuffle_deck()

while(game):
    currentCard = main_deck.draw_card()
    print(f"Your card is {currentCard}")
    nextCard = main_deck.draw_card()
    user_input = input("next card higher or lower(or same)?: ")
    if user_input == "quit":
        game = False
    elif user_input == "higher":
        if nextCard.value > currentCard.value:
            print(nextCard)
            print("you win!")
        else:
            print(nextCard)
            print("you lose!")
            game = False
    elif user_input == "lower":
        if nextCard.value < currentCard.value:
            print(nextCard)
            print("you win!")
        else:
            print(nextCard)
            print("you lose!")
            game = False
    elif user_input == "same":
        if nextCard.value == currentCard.value:
            print(nextCard)
            print("damn how'd you guess that!?")
        else:
            print(nextCard)
            print("you lose!")
            game = False
    else:
        print(f"your command was: {user_input}")
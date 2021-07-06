class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
        # A would be 1, Jack would be 11, Queen 12, King 13

    def __repr__(self):
        return(f"{self.rank}({self.value}) of {self.suit}")
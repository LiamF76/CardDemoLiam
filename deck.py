import random
import playing_card

class Deck:
    """A deck of playing cards."""

    def __init__(self):
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        """Generate a full deck of 52 cards."""
        for suit in playing_card.SUITS:
            for rank in playing_card.RANKS:
                self.cards.append(playing_card(rank, suit))

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw(self):
        """Draw a card from the deck."""
        if not self.cards:
            raise ValueError("Deck is empty")
        return self.cards.pop()

    def __len__(self):
        """Return the number of cards in the deck."""
        return len(self.cards)
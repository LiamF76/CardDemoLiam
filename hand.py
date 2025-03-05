import playing_card

class Hand:
    """A hand of playing cards."""

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Add a card to the hand."""
        if not isinstance(card, playing_card):
            raise ValueError("Can only add PlayingCard objects")
        self.cards.append(card)

    def display(self):
        """Display the cards in the hand."""
        for card in self.cards:
            print(card)

    def __len__(self):
        """Return the number of cards in the hand."""
        return len(self.cards)
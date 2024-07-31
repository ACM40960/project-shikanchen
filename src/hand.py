class Hand:
    def __init__(self):
        self.cards = []  # cards in the hand
        self.value = 0  # total value of the hand
        self.visible_value = 0  # visible value of the hand
        self.aces = 0  # count of aces in the hand

    def add_card(self, card, face_up=True):
        card.face_up = face_up
        self.cards.append(card)
        self.value += self.get_card_value(card)
        if face_up:
            self.visible_value += self.get_card_value(card)
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # If total value > 21, and I have an ace, then change my ace to be a 1 instead of 11
        while (self.value > 21 or self.visible_value > 21) and self.aces:
            self.value -= 10
            if self.visible_value > 21:
                self.visible_value -= 10
            self.aces -= 1

    def get_card_value(self, card):
        if card.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif card.rank == 'Ace':
            return 11
        else:
            return int(card.rank)

    def __repr__(self):
        return f"Hand({' '.join([str(card) for card in self.cards])}) with value {self.value}"

from deck import Deck
from hand import Hand
from agent import BlackjackAI


class Game:
    def __init__(self, q_table_filename=None):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.dealer_reveal = False
        self.ai_agent = BlackjackAI(q_table_filename=q_table_filename)
        self.game_over = False

    def start_new_game(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deal_initial_cards()

    def deal_initial_cards(self):
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal(), face_up=False)

    def reveal_dealer_hand(self):
        self.dealer_hand.cards[1].face_up = True  # Reveal hole card
        self.dealer_reveal = True

    # def player_turn(self, state):
    #     action = self.ai_agent.choose_action(state)
    #     return action  # 0 for hit, 1 for stand

    def hit(self):
        card = self.deck.deal()
        self.player_hand.add_card(card)
        self.player_hand.adjust_for_ace()
        if self.player_hand.value > 21:
            self.game_over = True
        return card, self.player_hand.value

    def stand(self):
        self.reveal_dealer_hand()
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal())
            self.dealer_hand.adjust_for_ace()
        self.game_over = True
        return self.dealer_hand.cards, self.dealer_hand.value

    def get_hand_values(self):
        return self.player_hand.value, self.dealer_hand.value

    def get_hand_visible_values(self):
        return self.player_hand.visible_value, self.dealer_hand.visible_value

    def calculate_reward(self):
        # Basic reward system: +1 for win, 0 for draw, -1 for loss
        if self.game_over:
            if self.player_hand.value > 21:
                return - 1.0 / (self.player_hand.value - 21)  # Player busts
            elif self.dealer_hand.value > 21:
                return 1.0 / (22 - self.player_hand.value) + 1.0 / (self.dealer_hand.value - 21)  # Dealer busts
            elif self.player_hand.value > self.dealer_hand.value:
                return 1.0 / (self.player_hand.value - self.dealer_hand.value)  # Player wins
            elif self.player_hand.value < self.dealer_hand.value:
                return - 1.0 / (self.dealer_hand.value - self.player_hand.value)  # Player loses
            else:
                return 0.5 + 1.0 / (22 - self.player_hand.value)  # Draw
        else:
            return 1.0 / (22 - self.player_hand.value)

    def update_game_status(self):
        if self.player_hand.value > 21 or self.dealer_hand.value > 21:
            self.game_over = True

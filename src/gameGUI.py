import tkinter as tk
from game import Game
from PIL import Image, ImageTk


class GameGUI:
    def __init__(self, master, q_table_filename=None):
        self.master = master
        master.title("Blackjack Game")
        self.game = Game(q_table_filename=q_table_filename)

        # Layout
        self.status = tk.StringVar()
        self.status.set("Welcome to Blackjack!")

        # Dealer label and card images
        self.dealer_label = tk.Label(master, text="Dealer's Hand:")
        self.dealer_label.grid(row=0, column=0, columnspan=6)
        self.dealer_card_frames = [tk.Label(master) for _ in range(5)]
        for i, frame in enumerate(self.dealer_card_frames):
            frame.grid(row=1, column=i)

        # Player label and card images
        self.player_label = tk.Label(master, text="Player's Hand:")
        self.player_label.grid(row=2, column=0, columnspan=6)
        self.player_card_frames = [tk.Label(master) for _ in range(5)]
        for i, frame in enumerate(self.player_card_frames):
            frame.grid(row=3, column=i)

        # Status label
        self.status_label = tk.Label(master, textvariable=self.status)
        self.status_label.grid(row=4, column=0, columnspan=6)

        # Buttons
        self.hit_button = tk.Button(master, text="Hit", command=self.hit)
        self.hit_button.grid(row=5, column=1)

        self.stand_button = tk.Button(master, text="Stand", command=self.stand)
        self.stand_button.grid(row=5, column=2)

        self.restart_button = tk.Button(master, text="Restart", command=self.start_new_game)
        self.restart_button.grid(row=5, column=3)

        self.ai_play_button = tk.Button(master, text="AI Play", command=self.ai_play)
        self.ai_play_button.grid(row=7, column=2)

        # Initialize game
        self.start_new_game()

    def display_cards(self, hand, frames):
        for i, frame in enumerate(frames):
            if i < len(hand.cards):
                card = hand.cards[i]
                if card.face_up:
                    img = Image.open(card.image_path)
                else:
                    img = Image.open("../images/face back.png")
                img = img.resize((100, 140), Image.Resampling.LANCZOS)
                img = ImageTk.PhotoImage(img)
                frame.config(image=img)
                frame.image = img
            else:
                frame.config(image='')  # clear the frame if no card

    def update_ui(self):
        self.display_cards(self.game.dealer_hand, self.dealer_card_frames)
        self.display_cards(self.game.player_hand, self.player_card_frames)
        self.status_label.config(text=f'Player: {self.game.player_hand.value}, Dealer: {self.game.dealer_hand.value if self.game.dealer_reveal else "hidden"}')

    def disable_buttons(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.ai_play_button.config(state=tk.DISABLED)

    def enable_buttons(self):
        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)
        self.ai_play_button.config(state=tk.NORMAL)

    def ai_play(self):
        """Method to let the AI take control and play the hand."""
        if not self.game.game_over:
            while not self.game.game_over:
                state = self.game.get_hand_visible_values()
                action = self.game.ai_agent.choose_action(state)
                if action == 0:
                    self.hit()
                else:
                    self.stand()
                self.update_ui()

                if action == 1:  # If the AI decides to stand, break the loop
                    break

        self.disable_buttons()  # Disable further actions after the AI completes its turn

    def hit(self):
        card, value = self.game.hit()
        if value > 21:
            self.game.reveal_dealer_hand()
            self.status.set("Player busts!")
        self.update_ui()

    def stand(self):
        cards, value = self.game.stand()
        if value > 21:
            self.status.set("Dealer busts! Player wins!")
        else:
            player_value, dealer_value = self.game.get_hand_values()
            if dealer_value > player_value:
                self.status.set("Dealer wins!")
            elif dealer_value < player_value:
                self.status.set("Player wins!")
            else:
                self.status.set("It's a tie!")
        self.disable_buttons()
        self.update_ui()

    def start_new_game(self):
        self.game.start_new_game()
        self.game.game_over = False
        self.status.set("Hit or stand?")
        self.enable_buttons()
        self.update_ui()

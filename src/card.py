class Card:
    def __init__(self, suit, rank, face_up=True):
        self.suit = suit
        self.rank = rank
        self.face_up = face_up
        self.image_path = f"../images/{self.rank} of {self.suit}.png"

    def __repr__(self):
        return f"{self.rank} of {self.suit}" if self.face_up else "Face Down"

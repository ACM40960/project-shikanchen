import tkinter as tk
from gameGUI import GameGUI

if __name__ == "__main__":
    root = tk.Tk()
    gui = GameGUI(root, q_table_filename="../ai_models/ai_q_table_10000000.npy")
    root.mainloop()

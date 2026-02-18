import tkinter as tk
from tkinter import messagebox
import random

# Theme Constants
BG_COLOR = "#1F1C2C"
FG_COLOR = "#928DAB"
ACCENT_COLOR = "#928DAB"
FONT_FAMILY = "Arial"

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Day 2: Number Guessing Game")
        self.root.geometry("400x350")
        self.root.configure(bg=BG_COLOR)

        self.target_number = 0
        self.attempts = 0

        self.setup_ui()
        self.start_new_game()

    def setup_ui(self):
        # Title
        self.title_label = tk.Label(
            self.root, 
            text="Number Guessing Game", 
            bg=BG_COLOR, 
            fg=ACCENT_COLOR,
            font=(FONT_FAMILY, 16, "bold"),
            pady=20
        )
        self.title_label.pack()

        # Instruction
        self.instruction_label = tk.Label(
            self.root, 
            text="I'm thinking of a number between 1 and 100.\nCan you guess what it is?", 
            bg=BG_COLOR, 
            fg=FG_COLOR,
            font=(FONT_FAMILY, 12),
            pady=10
        )
        self.instruction_label.pack()

        # Entry
        self.entry = tk.Entry(
            self.root, 
            font=(FONT_FAMILY, 14), 
            bg=BG_COLOR, 
            fg=FG_COLOR, 
            insertbackground=FG_COLOR,
            justify="center"
        )
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', lambda event: self.check_guess())

        # Guess Button
        self.guess_button = tk.Button(
            self.root, 
            text="Guess", 
            command=self.check_guess, 
            bg=ACCENT_COLOR, 
            fg=BG_COLOR,
            activebackground=ACCENT_COLOR,
            activeforeground=BG_COLOR,
            font=(FONT_FAMILY, 12, "bold"),
            padx=20, 
            pady=5,
            relief="flat",
            cursor="hand2"
        )
        self.guess_button.pack(pady=10)

        # Feedback
        self.feedback_label = tk.Label(
            self.root, 
            text="", 
            bg=BG_COLOR, 
            fg=FG_COLOR,
            font=(FONT_FAMILY, 12, "italic"),
            pady=10
        )
        self.feedback_label.pack()

        # Reset Button (Initially Hidden)
        self.reset_button = tk.Button(
            self.root, 
            text="Play Again", 
            command=self.start_new_game, 
            bg=BG_COLOR, 
            fg=FG_COLOR,
            activebackground=BG_COLOR,
            activeforeground=FG_COLOR,
            font=(FONT_FAMILY, 10),
            padx=10, 
            pady=5,
            relief="flat",
            cursor="hand2"
        )

    def start_new_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback_label.config(text="", fg=FG_COLOR)
        self.entry.delete(0, tk.END)
        self.entry.config(state="normal")
        self.guess_button.config(state="normal")
        self.reset_button.pack_forget()
        self.entry.focus_set()

    def check_guess(self):
        guess_str = self.entry.get()
        
        if not guess_str.isdigit():
            self.feedback_label.config(text="Please enter a valid number.", fg=FG_COLOR)
            return

        guess = int(guess_str)
        self.attempts += 1

        if guess < self.target_number:
            self.feedback_label.config(text="Too Low! Try again.", fg=FG_COLOR)
        elif guess > self.target_number:
            self.feedback_label.config(text="Too High! Try again.", fg=FG_COLOR)
        else:
            self.feedback_label.config(
                text=f"Correct! You won in {self.attempts} attempts.", 
                fg=ACCENT_COLOR
            )
            self.game_over()
        
        self.entry.delete(0, tk.END)

    def game_over(self):
        self.entry.config(state="disabled")
        self.guess_button.config(state="disabled")
        self.reset_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

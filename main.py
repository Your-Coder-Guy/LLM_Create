import tkinter as tk
from tkinter import messagebox
import pygame

# Initialize main window
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("400x400")

# Center the window
window_width = 400
window_height = 400

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

position_top = int((screen_height - window_height) / 2)
position_right = int((screen_width - window_width) / 2)

window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Function to start the game
def start_game(selected_player):
    global player
    player = selected_player
    start_menu.pack_forget()  # Hide the start menu
    game_frame.pack(expand=True)  # Show the game board
    pygame.mixer.init()
    pygame.mixer.music.load('audio.wav')  # Load the music
    pygame.mixer.music.play(-1)  # -1 means the music will loop

# Create the start menu
start_menu = tk.Frame(window)
start_menu.pack(expand=True)

title = tk.Label(start_menu, text="Tic Tac Toe", font=('Helvetica', 18, 'bold'))
title.pack(pady=20)

choose_label = tk.Label(start_menu, text="Choose who goes first:", font=('Helvetica', 14))
choose_label.pack(pady=10)

x_button = tk.Button(start_menu, text="X", width=10, height=2, command=lambda: start_game('X'))
x_button.pack(pady=5)

o_button = tk.Button(start_menu, text="O", width=10, height=2, command=lambda: start_game('O'))
o_button.pack(pady=5)

# Create the game board
game_frame = tk.Frame(window)
buttons = [[None for _ in range(3)] for _ in range(3)]
player = 'X'

def check_win():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    return False

def check_draw():
    for row in buttons:
        for button in row:
            if button['text'] == "":
                return False
    return True

def on_click(row, col):
    global player
    if buttons[row][col]['text'] == "":
        buttons[row][col]['text'] = player
        if check_win():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {player} wins!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_board()
        else:
            player = 'O' if player == 'X' else 'X'

def reset_board():
    global player
    player = 'X'
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ""

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(game_frame, text="", width=10, height=3, command=lambda row=row, col=col: on_click(row, col))
        buttons[row][col].grid(row=row, column=col)

window.mainloop()
pygame.mixer.music.stop()  # Stop the music when the game window is closed

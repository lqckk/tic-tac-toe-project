import tkinter as tk
from tkinter import messagebox

# Inicializācija
root = tk.Tk()
root.title("Krustiņi-nullītes")

# Spēles laukums
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

def check_winner():
    """Pārbauda uzvarētāju"""
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_draw():
    """Pārbauda, vai ir neizšķirts"""
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def on_click(row, col):
    global current_player

    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state=tk.DISABLED)

        winner = check_winner()
        if winner:
            messagebox.showinfo("Spēle beigusies", f"Spēlētājs {winner} uzvarēja!")
            reset_game()
            return

        if is_draw():
            messagebox.showinfo("Spēle beigusies", "Neizšķirts!")
            reset_game()
            return

        current_player = "O" if current_player == "X" else "X"

def reset_game():
    """Atjauno spēli"""
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ", state=tk.NORMAL)

# Pogas izveide
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                                      command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Poga spēles atiestatīšanai
reset_button = tk.Button(root, text="Atiestatīt spēli", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()

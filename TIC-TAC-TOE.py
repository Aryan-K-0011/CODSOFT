import tkinter as tk
import math

# Initialize the board
def initialize_board():
    return [' ' for _ in range(9)]

# Check for winner
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Check for a draw
def check_draw(board):
    return ' ' not in board

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# AI move
def ai_move(board, buttons):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'
    buttons[move].config(text='O', state='disabled')
    if check_winner(board, 'O'):
        for button in buttons:
            button.config(state='disabled')
        status_label.config(text="AI wins!")
    elif check_draw(board):
        status_label.config(text="It's a draw!")

# Human move
def human_move(index, board, buttons):
    if board[index] == ' ':
        board[index] = 'X'
        buttons[index].config(text='X', state='disabled')
        if check_winner(board, 'X'):
            for button in buttons:
                button.config(state='disabled')
            status_label.config(text="You win!")
        elif check_draw(board):
            status_label.config(text="It's a draw!")
        else:
            ai_move(board, buttons)

# Reset the game
def reset_game(board, buttons):
    board[:] = initialize_board()
    for button in buttons:
        button.config(text='', state='normal')
    status_label.config(text="Your turn!")

# Main game function
def play_game():
    board = initialize_board()
    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    frame = tk.Frame(root)
    frame.pack()

    buttons = []
    for i in range(9):
        button = tk.Button(frame, text='', font=('Arial', 20), width=5, height=2,
                           command=lambda i=i: human_move(i, board, buttons))
        button.grid(row=i//3, column=i%3)
        buttons.append(button)

    global status_label
    status_label = tk.Label(root, text="Your turn!", font=('Arial', 14))
    status_label.pack()

    reset_button = tk.Button(root, text="Reset", font=('Arial', 14), command=lambda: reset_game(board, buttons))
    reset_button.pack()

    root.mainloop()

if __name__ == "__main__":
    play_game()

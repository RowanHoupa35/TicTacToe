import tkinter as tk
from tkinter import messagebox


class TicTacToeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text='', font=('normal', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                self.show_winner()
            elif self.is_board_full():
                self.show_tie()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
                    all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
                all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def show_winner(self):
        messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
        self.reset_board()

    def show_tie(self):
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        self.reset_board()

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='')
        self.current_player = 'X'


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()

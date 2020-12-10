import os

os.system("cls")


class Board:
    def __init__(self):
        # display input as a list, lists starts at 0 but good to use spare space as dummy
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        # displays the cells, %s allows me to add a value into python string
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))

    def update_cells(self, cell_number, player):
        # if the cell is clear, player can enter X or O
        if self.cells[cell_number] == ' ':
            self.cells[cell_number] = player

    def is_winner(self, player):
        # checks if cells 1-3 are taken, if they are return true
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True
        return False

    # check for tie game
    def game_tie(self):
        # cells starts at empty
        used_cells = 0
        # check the cells
        for cell in self.cells:
            # check for space in cells
            if cell != " ":
                # count along
                used_cells += 1
        # if 9 cells are filled, game tie
        if used_cells == 9:
            return True
        else:
            return False

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


board = Board()


def print_header():
    print("Welcome to Tic-Tac-Toe\n")


def refresh_screen():
    # Print the header
    print_header()

    # Show the board
    board.display()


while True:
    refresh_screen()
    # get X input1
    x_choice = int(input("\nX) please choose 1 - 9. > "))

    # Update board
    board.update_cells(x_choice, "X")

    # check for X win
    if board.is_winner("X"):
        print("\nX is the winner!\n")
        play_again = input("Would you like to play again? y/n >")
        if play_again == "y":
            board.reset()
            continue
        else:
            break

    # check for a tie game
    if board.game_tie():
        print("\nThis is a tie game!\n")
        play_again = input("Would you like to play again? y/n >")
        if play_again == "y":
            board.reset()
            continue
        else:
            break

    refresh_screen()
    # get O input1
    o_choice = int(input("\nO) please choose 1 - 9. > "))

    # Update board
    board.update_cells(o_choice, "O")

    # check for O win
    if board.is_winner("O"):
        print("\nO is the winner!\n")
        play_again = input("Would you like to play again? y/n >")
        if play_again == "y":
            board.reset()
            continue
        else:
            break

    if board.game_tie():
        print("\nThis is a tie game!\n")
        play_again = input("Would you like to play again? y/n >")
        if play_again == "y":
            board.reset()
            continue
        else:
            break

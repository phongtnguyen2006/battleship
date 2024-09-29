"""
Battleship class that makes the board and has all the functions to edit it
"""

class BattleShip:

    ships = []
    #makes board and asks for player to put ships on the board
    def set_up_board(self):
        print("Set up your board! Choose any box A-E 1-5 and a position")
        print("Example input is E3 V (V for vertical H for horizontal)")
        count = 0
        while count < 3:
            failed = False
            spot = input("Enter in the location of the ship: ")
            print("")
            if " " in spot:
                rows,direction = spot.split(" ")
            else:
                print("Try again, there was an error")
                continue
            rows = [ord(rows[0])-64,int(rows[1])]

            if direction == 'V':
                if rows[1] <= 3 and rows[1] > 0 and self.board[rows[1]][rows[0]] != "S" and self.board[rows[1]+1][rows[0]] != "S" and self.board[rows[1]+2][rows[0]] != "S":
                    ship = [[rows[0], rows[1]], [rows[0], rows[1]+1], [rows[0],rows[1]+2]]
                    self.ships.append(ship)
                    self.board[rows[1]][rows[0]] = "S"
                    self.board[rows[1]+1][rows[0]] = "S"
                    self.board[rows[1]+2][rows[0]] = "S"
                else:
                    failed = True
            elif direction == "H":
                if rows[0] <= 3 and rows[0] > 0 and self.board[rows[1]][rows[0]] != "S" and self.board[rows[1]][rows[0]+1] != "S" and self.board[rows[1]][rows[0]+2] != "S":
                    ship = [[rows[0], rows[1]], [rows[0]+1, rows[1]], [rows[0]+2, rows[1]]]
                    self.ships.append(ship)
                    self.board[rows[1]][rows[0]] = "S"
                    self.board[rows[1]][rows[0] + 1] = "S"
                    self.board[rows[1]][rows[0] + 2] = "S"
                else:
                    failed = True
            else:
                failed = True

            if failed == False:
                count += 1

                print('\nShip has been added\n')
                self.print_board()
            else:
                print("Try again, there was an error")
        print("Board has been filled")

    #prints board
    def print_board(self):
        for row in self.board:
            print("%5s%5s%5s%5s%5s%5s" % (f'{row[0]} |', f'{row[1]} |',f'{row[2]} |',f'{row[3]} |',f'{row[4]} |',f'{row[5]} |'))
            print("  ----------------------------")
        print('\n')
    board = [
        [0,'A','B','C','D','E'],
        [1, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0]
    ]


    def __init__(self):
        self.set_up_board()


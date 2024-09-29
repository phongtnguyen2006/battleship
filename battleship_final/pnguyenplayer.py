"""
Player class used to control the moves of one of the player
"""
class Player:
    #players own baord with ship positions
    player_board = []
    #used to track where player misses and hits
    attacked_board = [
        [0,'A','B','C','D','E'],
        [1, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0]
    ]
    #all points that have been shot
    attacked_points = []
    #position of opponent ships
    opponent_ships = []

    #makes a board and sees if the player is first to move
    def __init__(self, player_board, is_first):
        self.player_board = player_board
        if is_first:
            print("You are the first player!")
        else:
            print("You are the second player, wait for Player 1 to make their first move!!")


    #handles input of player and calls the corresponding function associated with that input
    def handle_input(self,entered):
        if len(entered) == 2 and entered[0].isalpha() and entered[1].isdigit() and ord(entered[0])-64 > 0 and ord(entered[0])-64 <= 3 and entered[1] and int(entered[1]) >0 and int(entered[1]) < 6:
            rows = [ord(entered[0])-64,int(entered[1])]
            return self.shoot(rows)
        elif entered == "PO":
            self.print_board(self.attacked_board)
            return "printed"
        else:
            return "invalid"

    #Takes a position and wheter or not it is a hit. If it is a hit changes board position to H. If it is a miss changes board position to X
    def update_board(self, position, hits):
        if hits:
            self.attacked_board[position[1]][position[0]] = "H"
        else:
            self.attacked_board[position[1]][position[0]] = "X"
        self.print_board(self.attacked_board)

    #allows player to print the board
    def print_board(self, grid):
        for row in grid:
            print("%5s%5s%5s%5s%5s%5s" % (f'{row[0]} |', f'{row[1]} |',f'{row[2]} |',f'{row[3]} |',f'{row[4]} |',f'{row[5]} |'))
            print("  ----------------------------")
        print("")
        print("")

    #prints all the different commands the player can do
    def print_commands(self):
        print("\nCommands: ")
        print("1. Attack --> Enter in a coordinate on the board (A-E 1-5) Ex: A5")
        print("2. Print your attacking board --> PO")

    #shoots at a position
    def shoot(self, position):
        if position in self.attacked_points:
            print("You have already attacked this point. Try again.")
            return "invalid"
        self.attacked_points.append(position)
        for ship in self.opponent_ships:
            if position in ship:
                ship.remove(position)
                # print(position)
                self.update_board(position, True)
                return self.check_sunk()

        self.update_board(position, False)
        return "missed"

    #checks if a ship is already sunk
    def check_sunk(self):
        # nested for loop to update ships
        # if list empty sinks

        for ship in self.opponent_ships:
            if len(ship) == 0:
                self.opponent_ships.remove(ship)
                won = self.check_win()
                if won:
                    return "won"
                return "sunk"
        return "hit"

    #checks if player has won
    def check_win(self):
        if len(self.opponent_ships) == 0:
            return True
        return False

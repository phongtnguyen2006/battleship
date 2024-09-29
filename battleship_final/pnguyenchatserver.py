"""
Chat server used for one of the players
"""

import pnguyenplayer
import json
import pnguyenbattleship
from socket import *
from codecs import decode

HOST = "0.0.0.0"
PORT = 8889
ADDRESS = (HOST, PORT)
BUFSIZE = 1024
CODE = "ascii"

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)
print("Waiting for connection . . .")
client, address = server.accept()
print("... connected from: ", address)
client.send(bytes("Welcome to Battleship!", CODE))  # Send greeting

myBattleShip = pnguyenbattleship.BattleShip()
myPlayer = player.Player(myBattleShip.board, False)
user_inputs = []

array_string = json.dumps(myBattleShip.ships)
client.send(bytes(array_string, CODE))
opponent = json.loads(decode(client.recv(BUFSIZE), CODE))
myPlayer.opponent_ships = opponent

won = False

while True:
    message = decode(client.recv(BUFSIZE), CODE)
    #Checks to see if other player has already won. If they have gives player opportunity to draw the game
    if not message:
        print("Client disconnected")
        client.close()
        break
    else:
        if message == "won":
            print("your opponent sunk all your ships? Can you Draw!?")
        else:
            print(message)


    myPlayer.print_commands()
    entered = ""
    send_message = ""

    #Takes move from player
    while True:
        entered = input("What would you like to do: ")
        spitted = myPlayer.handle_input(entered)
        if spitted == "invalid" or spitted == "printed":
            if spitted == "invalid":
                print("Try Again.")
            continue
        elif spitted == "missed":
            print("You missed :(")
            send_message = "Your opponent missed your ship!"
        elif spitted == "sunk":
            print(f'You sunk ship #{len(myPlayer.opponent_ships) + 1}!!!')
            send_message = "Oh no! Your opponent sunk your ship!"
        elif spitted == "hit":
            print("You hit a ship!")
            send_message = "BOOM! Your opponent hit your ship!"
        elif spitted == "won":
            send_message = "Your opponent destroyed all your ships. Can you Draw!?"
            won = True
        break

    print("")

    #checks to see if the server has won lost or drew
    if won and message == "won":
        print("You Drew!")
    elif won and message != "won":
        print("You Won!")
    elif message == "won" and won == False:
        print("You Lost!")

    client.send(bytes(send_message, CODE))

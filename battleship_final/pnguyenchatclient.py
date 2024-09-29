"""
Chat server used for one of the players
"""

import pnguyenbattleship
import json
import pnguyenplayer
from socket import *
from codecs import decode

HOST = "10.140.168.171"
PORT = 8889
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = "ascii"

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)

print(decode(server.recv(BUFSIZE), CODE))       # The server's greeting
print("")
myBattleShip = pnguyenbattleship.BattleShip()
myPlayer = pnguyenplayer.Player(myBattleShip.board, True)

array_string = json.dumps(myBattleShip.ships)
opponent = json.loads(decode(server.recv(BUFSIZE),CODE))
myPlayer.opponent_ships = opponent
server.send(bytes(array_string,CODE))
won = False

while True:

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
            print(f'You sunk ship #{3-len(myPlayer.opponent_ships)}!!!')
            send_message = "Oh no! Your opponent sunk your ship!"
        elif spitted == "hit":
            print("You hit a ship!")
            send_message = "BOOM! Your opponent hit your ship!"
        elif spitted == "won":
            send_message = "won"
            print("You destroyed all of your opponents ships!! Let's see if your opponent can Draw!")
            won = True
        break

    print("")

    server.send(bytes(send_message, CODE))



    reply = decode(server.recv(BUFSIZE), CODE)  # Get the server's reply

    #checks to see if client has won lost or drew
    if reply == "won" and won == False:
        print("You Lost!")
        break
    elif reply == "won" and won:
        print("You Drew!")
        break
    elif won and reply != 'won':
        print("You Win!")
        break

    if not reply:
        print("Server disconnected")
        break
    else:
        print(reply)                                # Display the server's reply

server.close()
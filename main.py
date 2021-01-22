#!/usr/bin/python3
import grid
import pickle
import sys

#get input from user and call the function to move the board accordingly
def move_board(board):
    inp = input("Use 'i' for up, 'k' for down, 'j' for left, and 'l' for right or 's' for save: ")
    if inp == "i":
       board.up()
    elif inp == "k":
        board.down()
    elif inp == "j":
        board.left()
    elif inp == "l":
        board.right()
    elif inp == "s":
        save(board)
    else:
        board = move_board(board)
    return board

#save the game
def save(board):
    new_file = open("board.txt", 'wb')
    pickle.dump(board, new_file)
#    new_file.write(str(board.board )+'\n')
#    new_file.write(str(board.score )+'\n')
#    new_file.write(str(board.count )+'\n')
#    new_file.write(str(board.coordx)+'\n')  
#    new_file.write(str(board.coordy)+'\n')
#    new_file.write(str(board.reset )+'\n')
#    new_file.write(str(board.update)+'\n')
    new_file.close()
    sys.exit()
        

#set up game   
myGrid = grid.Grid()
inp = input('Do you want to load a game or start a new game? (l/n): ')
if inp == 'l':
    obj = open('board.txt', 'rb')
    myGrid = pickle.load(obj)
    obj.close()
else:
    newcoord = myGrid.newcoord()
    myGrid.board[newcoord[0]][newcoord[1]] = 2
myGrid.display_board()
                 
while 7:
    myGrid = move_board(myGrid)
    if myGrid.update == True:
        myGrid.update = False
        newcoord = myGrid.newcoord()
        myGrid.board[newcoord[0]][newcoord[1]] = 2
        myGrid.display_board()
        myGrid.is_done()

    
    

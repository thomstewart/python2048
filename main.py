#!/usr/bin/python3
import grid

#get input from user and call the function to move the board accordingly
def move_board(board):
    inp = input("Use 'i' for up, 'k' for down, 'j' for left, and 'l' for right: ")
    if inp == "i":
       board.up()
    elif inp == "k":
        board.down()
    elif inp == "j":
        board.left()
    elif inp == "l":
        board.right()
    else:
        board = move_board(board)
    return board

#set up game   
    myGrid = grid.Grid()
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

    
    

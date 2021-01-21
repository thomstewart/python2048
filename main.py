#!/usr/bin/python3
import grid

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
    return board    
    
myGrid = grid.Grid()
newcoord = myGrid.newcoord()
myGrid.board[newcoord[0]][newcoord[1]] = 2
myGrid.display_board()
                 
while 7:
    board = move_board(myGrid)
    if board == myGrid:
        newcoord = myGrid.newcoord()
        myGrid.board[newcoord[0]][newcoord[1]] = 2
        myGrid.display_board()
        myGrid.is_done()
    
    

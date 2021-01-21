#!/usr/bin/python3
import grid

myGrid = grid.Grid()
#print('original')
myGrid.display_board()
#print(myGrid.newcoord())
#myGrid.display_board()
myGrid.left()#down
#print('after left')
myGrid.display_board()
myGrid.up()#right
#print('after up')
myGrid.display_board()
myGrid.right()#up
#print('after right')
myGrid.display_board()
myGrid.down()#left
#print('after down')
myGrid.display_board()
#myGrid.is_done()





#!/usr/bin/python3
import grid

myGrid = grid.Grid()
myGrid.display_board()

print(myGrid.newcoord())
myGrid.left()
myGrid.up()
myGrid.is_done()
myGrid.display_board()
myGrid.right()
myGrid.down()
myGrid.display_board()





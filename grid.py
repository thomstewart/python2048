#!/usr/bin/python3
import sys #for exit
import random #for random number gen for coordinates
class Grid:
    #initialize the board object    
    def __init__(self):
        self.board = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        self.score = 0
        self.count = 0
        self.coordx= 0
        self.coordy= 0
        self.reset = False
        self.update = False

#    def iter(self):
#        self.coord = (0,0)
    #iterate over the board one step at a time
    def iternext(self):
        if self.coordy != 4:
            retval = self.board[self.coordy][self.coordx]
        if self.coordy < 4:
            if self.coordx < 3:
                self.coordx+=1
            else:
                self.coordx = 0
                self.coordy+=1

        else:
            self.coordy = 0
            self.coordx = 0
            self.reset= True
            return 0
        return retval
    #print out the board and score
    def display_board(self):
        print()
        print('Score:',str(self.score))
        print()
        for i in range(0,4):
            for j in range(0,4):
                k = self.iternext()
                if k > 0:
                    fixed_string="{:^4}".format(str(k))
                    print(fixed_string,end='',flush=True)
                else:
                    print('    ',end='',flush=True)
                if j<3:
                    print('|',end='',flush=True)
            print('')
            if i<3:
                print('----+----+----+----')
        self.iternext()
        self.reset = False
                
    #check whether player has won
    def is_done(self):
        self.reset = False
        self.coordx = 0
        self.coordy = 0
        while self.reset == False:
            if self.iternext() == 2048:
                print('You Win!')
                sys.exit()
        self.reset = False
        
    #generate a random coordinate
    def newcoord(self):
        x = random.randrange(0,4,1)
        y = random.randrange(0,4,1)
        if self.board[x][y] == 0:
            return(x,y)
        else:
            return self.newcoord()
    #move the board contents up
    def up(self):
        for i in range(1,4):
            for y in range(0,4):
                if self.board[i][y] != 0:
                    n = i
                    #check destination square for '0'
                    while n>0 and self.board[n-1][y] == 0:
                        self.update = True
                        self.board[n-1][y] = self.board[n][y]
                        self.board[n][y] = 0
                        n -= 1
                    #check destination square for match
                    if n > 0 and self.board[n-1][y] == self.board[n][y]:
                        self.update = True
                        self.board[n-1][y] += self.board[n][y]
                        self.board[n][y] = 0
                        self.score += self.board[n-1][y]
                        self.score -= 1

    #move board contents left
    def left(self):
        for y in range(0,4):
            for i in range(0,4):
                if self.board[i][y] != 0:
                    n = y
                    #check destination square for '0'
                    while n > 0 and self.board[i][n - 1] == 0:
                        self.update = True
                        self.board[i][n - 1] = self.board[i][n]
                        self.board[i][n] = 0
                        n -= 1
                    #check destination square for match
                    if n > 0 and self.board[i][n - 1] == self.board[i][n]:
                        self.update = True
                        self.board[i][n-1] += self.board[i][n]
                        self.board[i][n] = 0
                        self.score += self.board[i][n-1]
                        self.score -= 1
        
    #move the board contents down
    def down(self):
        #print(0)
        for i in range(3,-1,-1):
            for y in range(3,-1,-1):
                #print(1)
                #print(i,y)
                if self.board[i][y] != 0:
                    n = i
                    #check destination square for '0'
                    while n < 3 and self.board[n+1][y] == 0:
                        self.update = True
                        self.board[n + 1][y] = self.board[n][y]
                        self.board[n][y] = 0
                        n += 1
                    #check destination square for match
                    if n < 3 and self.board[n+1][y] == self.board[n][y]:
                        self.update = True
                        self.board[n + 1][y] += self.board[n][y]
                        self.board[n][y] = 0
                        self.score += self.board[n + 1][y]
                        self.score -= 1
                        
    #move board contents right
    def right(self):
        for y in range(3,-1,-1):
            for i in range(3,-1,-1):
                if self.board[i][y] != 0:
                    n = y
                    #check destination square for '0'
                    while n < 3 and self.board[i][n + 1] == 0:
                        self.update = True
                        self.board[i][n + 1] = self.board[i][n]
                        self.board[i][n] = 0
                        n += 1
                    #check destination square for match
                    if n < 3 and self.board[i][n + 1] == self.board[i][n]:
                        self.update = True
                        self.board[i][n+1] += self.board[i][n]
                        self.board[i][n] = 0
                        self.score += self.board[i][n+1]
                        self.score -= 1


      
      

#!/usr/bin/python3
import sys
import random
class Grid:
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

    def iter(self):
        self.coord = (0,0)

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
            return
        return retval

    def display_board(self):
        print()
        print('Score:',str(self.score))
        print()
        for i in range(0,4):
            for j in range(0,4):
                k=self.iternext()
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
        self.reset = False

    def is_done(self):
        self.reset = False
        self.coordx = 0
        self.coordy = 0
        while self.reset == False:
            if self.iternext() == 2048:
                print('You Win!')
                sys.exit()
        self.reset = False

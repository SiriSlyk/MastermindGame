import pygame
import random

GUESSES = 12
COLS = 4
COLORS = {0: (255, 255, 255), 1: (255, 0, 0), 2: (0, 255, 0), 3: (204, 0, 255), 4: (0, 102, 204), 5: (255, 153, 0)}
pygame.font.init()
FONT = pygame.font.SysFont('Comic Sans MS', 20)

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(COLS)] for _ in range(GUESSES)]
        self.marginX, self.marginY = 300, 100
        self.size = 50
        self.currentRow = GUESSES - 1
        self.correct = [1, 1, 1, 2]
        self.red, self.white = 0,0
        self.redPos = []
        self.whitePos = []
        self.won = False

    def draw(self, win):

        win.fill((50, 50, 50))

        #pygame.draw.line(win, (0, 0, 0), (self.height / TILES * i, 0), (self.height / TILES * i, self.height), 4)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                pygame.draw.rect(win, COLORS[self.board[i][j]], (self.size*j+self.marginX,self.size*i+self.marginY, self.size, self.size)) #(size*i,size*j, size, size)
        # Number of rounds
        for i in range(GUESSES+1):
            pygame.draw.line(win, (0, 0, 0), (0+self.marginX, i*self.size+self.marginY), (self.size*4+self.marginX, i*self.size+self.marginY), 4)
        # Number of colonner
        for i in range(COLS+1):
            pygame.draw.line(win, (0, 0, 0), (self.size*i+self.marginX, self.marginY), (0+self.size*i+self.marginX, GUESSES * self.size+self.marginY), 4)

            # Draw status
            # Red
        for pos in self.redPos:
            position = pos[0]#(self.marginX+self.size*COLS,self.size*(self.currentRow+1)+self.marginY,self.red*self.size/COLS,self.size/COLS)
            pygame.draw.rect(win, (255, 0, 0), position)
            pygame.draw.rect(win, (0,0,0), position, 1)  # (size*i,size*j, size, size)
            redText = FONT.render(str(pos[1]), False, (0, 0, 0))
            win.blit(redText, (pos[0][0]+6, pos[0][1]-2))

            # White
        for pos in self.whitePos:
            position = pos[0]#(self.marginX+self.size*COLS+self.red*(self.size/COLS), self.size*(self.currentRow+1)+self.marginY, self.white * self.size / COLS, self.size / COLS)
            pygame.draw.rect(win, (255, 255, 255), position)
            pygame.draw.rect(win, (0, 0, 0), position, 1)  # (size*i,size*j, size, size)
            whiteText = FONT.render(str(pos[1]), False, (0, 0, 0))
            win.blit(whiteText, (pos[0][0]+6, pos[0][1]-2))


        if self.won or self.currentRow == -1:
            for i in range(COLS):
                pygame.draw.rect(win, COLORS[self.correct[i]],
                                 (self.size * i + self.marginX, int(self.marginY/4), self.size, self.size))

                pygame.draw.rect(win, (0,0,0),
                                 (self.size * i + self.marginX, int(self.marginY / 4), self.size, self.size), 2)

        pygame.draw.rect(win, (128, 128, 128),
                         (self.marginX, self.marginY + (GUESSES) * self.size, self.size * 4 + 2, self.size))
        pygame.draw.rect(win, (0,0,0), (self.marginX,self.marginY+(GUESSES)*self.size, self.size*4+2, self.size),3)



        pygame.display.update()

    def click(self, pos):
        posX, posY = pos
        if self.won:
            pass
        elif self.marginX < posX < self.marginX+self.size * COLS and self.marginY < posY < self.marginY+self.size*GUESSES:

            x = int((posX-self.marginX)/self.size)
            y = int((posY-self.marginY)/self.size)
            if y == self.currentRow:
                self.board[y][x] = (self.board[y][x]+1) % len(COLORS)


        elif self.marginX < posX < self.marginX+self.size * COLS and self.marginY+self.size*GUESSES < posY < self.marginY+self.size*GUESSES + self.size and 0 not in self.board[self.currentRow]:
            self.check_guess()

    def set_ans(self):
        rand = random.Random()

        self.correct = [rand.randint(1, len(COLORS)-1) for _ in range(COLS)]
        print(self.correct)
    def check_guess(self):
        red = 0 # Color in correct index
        white = 0 # Color in answer
        currentRow = self.board[self.currentRow]
        for i in range(COLS):
            if self.correct[i] == currentRow[i]:
                red += 1
        colorsSet = set(currentRow)
        for item in colorsSet:
            c1 = currentRow.count(item)
            c2 = self.correct.count(item)
            white += min(c1, c2)
        white -= red
        self.currentRow -= 1
        self.red, self.white = red, white

        #self.redPos.append((self.marginX+self.size*COLS,self.size*(self.currentRow+1)+self.marginY,self.red*self.size/COLS,self.size/COLS))
        #self.whitePos.append((self.marginX+self.size*COLS+self.red*(self.size/COLS), self.size*(self.currentRow+1)+self.marginY, self.white * self.size / COLS, self.size / COLS))
        print(f'red: {self.red}, white: {self.white}')

        if self.red > 0:
            redPos = (self.marginX+self.size*COLS,self.size*(self.currentRow+1)+self.marginY, self.size/2, self.size/2)
            self.redPos.append((redPos, red))

        if self.white > 0:
            whitePos = (self.marginX+self.size*COLS,self.size*(self.currentRow+1)+self.marginY+(self.size/2), self.size/2, self.size/2)
            self.whitePos.append((whitePos, white))


        if self.red == 4:
            self.won = True





import pygame
import os 

pygame.init()

win = pygame.display.set_mode((500, 350))
win.fill((0,0,0))
pygame.display.set_caption('Game Library')

font = pygame.font.Font('freesansbold.ttf', 32)
text0 = font.render('Main Menu', True, (0,0,0))
textRect0 = text0.get_rect()
textRect0.center = (250, 50)

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    
def redrawWindow():
    win.fill((255,255,255))
    greenButton.draw(win, (0,0,0))
    blueButton.draw(win,(0,0,0))
    
run = True
greenButton = button((0,255,0), 100, 120, 300, 80, 'Snake Game')
blueButton = button((0,0,255), 100, 225, 300, 80, 'Hangman')
while run:
    redrawWindow()
    win.blit(text0, textRect0)
    pygame.display.update()
        
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenButton.isOver(pos):
               
                os.system('python Snake.py')
        
        if event.type == pygame.MOUSEMOTION:
            if greenButton.isOver(pos):
                greenButton.color = (255,0,0)
            else:
                greenButton.color = (0,255,0)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if blueButton.isOver(pos):
               
                os.system('python hangman.py')
        
        if event.type == pygame.MOUSEMOTION:
            if blueButton.isOver(pos):
                blueButton.color = (255,0,0)
            else:
                blueButton.color = (0,0,255)
        
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
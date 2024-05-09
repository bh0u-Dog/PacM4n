import pygame
from pygame import mixer
import random
pygame.init()

width = 560
width2 = 620

mixer.init()

screen = pygame.display.set_mode((width,650))

clock = pygame.time.Clock()

pygame.display.set_caption('PACMAN')

running = True

no_of_tiles = 28

image = pygame.transform.smoothscale(pygame.image.load('background.png'),(width,width2))

rectWid = width//28

class Window():
    def __init__(self):
        self.toggle_border = False
        self.map =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,3,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],
                [2,2,2,2,2,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,2,2,2,2,1],
                [2,2,2,2,2,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,2,2,2,2,1],
                [2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,1],
                [1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1],
                [2,2,2,2,2,2,0,0,0,0,1,2,2,2,2,2,2,1,0,0,0,0,2,2,2,2,2,2],
                [1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1],
                [2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,2],
                [2,2,2,2,2,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,2,2,2,2,2],
                [2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,2],
                [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
                [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
                [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
                [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
                [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
                [1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        
    def makingMap(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 0:
                    pygame.draw.circle(screen,'white',(j*rectWid + rectWid//2,i*rectWid + rectWid//2),rectWid//10)
                elif self.map[i][j] == 1 and self.toggle_border:
                    pygame.draw.rect(screen,'skyblue',(j*rectWid,i*rectWid,rectWid,rectWid),1)
                elif self.map[i][j] == 3:
                    pygame.draw.circle(screen,'orange',(j*rectWid + rectWid//2,i*rectWid + rectWid//2),rectWid//2)
                else:
                    pass

map = Window()

pac_x = rectWid + rectWid//2
pac_y = rectWid + rectWid//2
real_x = pac_x - (rectWid//2 + rectWid//4)
radius = rectWid
dir = 'stop'

pacman = pygame.transform.smoothscale(pygame.image.load('pacman.png'),(2*radius,2*radius))

def displayingPacman():
    pygame.draw.circle(screen,'yellow',(pac_x,pac_y),3/4*radius)

toggle_border = False



def colliding():
    global pac_x,pac_y,dir
    x = pac_x//rectWid
    y = pac_y//rectWid
    if x+1 < len(map.map[0]):
        if map.map[y][x+1] == 1 and dir == 'right':
            dir = 'stop'
    if x - 1 < len(map.map[0]):
        if map.map[y][x-1] == 1 and dir == 'left':
            dir = 'stop'
    if x < len(map.map[0]):
        if map.map[y + 1][x] == 1 and dir == 'down':
            dir = 'stop'
        if map.map[y - 1][x] == 1 and dir == 'up':
            dir = 'stop'


def displaying_borders():
    if toggle_border == True:
        pygame.draw.rect(screen,'red',(pac_x - radius,pac_y - radius,2*(radius),2*radius),1)

score = 0

rainbow_colors = ['violet','indigo','blue','green','yellow','orange','red']
index = 0

def displayingScore():
    global score,rainbow_colors,index
    font = pygame.font.Font('retroFont.ttf',30)
    text = font.render(f'Score: {score}',True,'white')
    text2 = font.render(f'bh0u-|)og',True,rainbow_colors[index])
    screen.blit(text,(0,620))
    screen.blit(text2,(400,615))

rainbow_colors2 = ['violet','blue','green','yellow','orange','red']

def displayingpacman():
    pacman = ['P','A','C','M','A','N']
    font = pygame.font.Font('retroFont.ttf',30)
    for i in range(len(pacman)):
        text = font.render(pacman[i],True,rainbow_colors2[i])
        screen.blit(text,(200+(i*25),620))

def changingColors():
    random_index = random.randint(0,len(rainbow_colors) - 2)
    rainbow_colors2[random_index] = random.choice(rainbow_colors)


colorShuffle = pygame.USEREVENT + 2
pygame.time.set_timer(colorShuffle,100)

def movingPacman():
    global dir,pac_x,pac_y
    
    if dir == 'right':
        pac_x += rectWid
    if dir == 'left':
        pac_x -= rectWid
    if dir == 'up':
        pac_y -= rectWid
    if dir == 'down':
        pac_y += rectWid

def teleportation():
    global pac_x
    if pac_x < rectWid//2:
        pac_x = width-(rectWid//2)
    if pac_x > width-(rectWid//2):
        pac_x = rectWid//2


class Ghosts():
    def __init__(self,color):
        self.color = color
        self.dir = 'stop'
        self.state = 'chasing'
        self.centerx = rectWid * 24 + rectWid//2
        self.centery = rectWid + rectWid//2
        self.centerx2 = rectWid * 24 + rectWid//2
        self.centery2 = rectWid + rectWid//2
        self.dirs = ['right','left','down','up']
        self.increment = rectWid

    def displaying(self):
        pygame.draw.circle(screen,self.color,(self.centerx,self.centery),3/4*radius)
    
    def teleportation(self):
        if self.centerx < rectWid//2:
            self.centerx = width-(rectWid//2)
        if self.centerx > width-(rectWid//2):
            self.centerx = rectWid//2

    def changingDir(self,map):
        if self.dir == 'stop':
            x = self.centerx//rectWid
            y = self.centery//rectWid
            newDir = random.choice(self.dirs)
            if x < len(map[0]):
                if map[y - 1][x] != 1 and newDir == 'up':
                    self.dir = newDir
            if x-1 < len(map[0]):
                if map[y][x - 1] != 1 and newDir == 'left':
                    self.dir = newDir
            if x+1 < len(map[0]):
                if map[y][x + 1] != 1 and newDir == 'right':
                    self.dir = newDir
            if x < len(map[0]):
                if map[y + 1][x] != 1 and newDir == 'down':
                    self.dir = newDir

    
    def moving(self):
        if self.dir == 'right':
            self.centerx += self.increment
        if self.dir == 'left':
            self.centerx -= self.increment
        if self.dir == 'up':
            self.centery -= self.increment
        if self.dir == 'down':
            self.centery += self.increment

    def colliding(self,map):
        x = self.centerx//self.increment
        y = self.centery//self.increment
        if x+1 < len(map[0]):
            if map[y][x+1] == 1 and self.dir == 'right':
                self.dir = 'stop'
        if x - 1 < len(map[0]):
            if map[y][x-1] == 1 and self.dir == 'left':
                self.dir = 'stop'
        if x < len(map[0]):
            if map[y + 1][x] == 1 and self.dir == 'down':
                self.dir = 'stop'
            if map[y - 1][x] == 1 and self.dir == 'up':
                self.dir = 'stop'

state = 'notWin'

pinky = Ghosts('orange')
clyde = Ghosts('pink')
clyde.centery = rectWid * 20 + rectWid//2
clyde.centery2 = rectWid * 20 + rectWid//2
blinky = Ghosts('red')
blinky.centerx = pac_x
blinky.centerx2 = pac_x
blinky.centery = rectWid * 26 + rectWid//2
blinky.centery2 = rectWid * 26 + rectWid//2

cyan = Ghosts('skyblue')
cyan.centerx = rectWid * 9 + rectWid//2
cyan.centery = rectWid * 12 + rectWid//2
cyan.centerx2 = rectWid * 9 + rectWid//2
cyan.centery2 = rectWid * 12 + rectWid//2

def eating():
    global score,enemyState
    x = pac_x//rectWid
    y = pac_y//rectWid
    if x < len(map.map[0]):
        if map.map[y][x] == 0:
            map.map[y][x] = 2
            score += 10
        if map.map[y][x] == 3:
            clyde.state = 'running'
            blinky.state = 'running'
            cyan.state = 'running'
            pinky.state = 'running'
            clyde.color = 'blue'
            blinky.color = 'blue'
            cyan.color = 'blue'
            pinky.color = 'blue'
            map.map[y][x] = 2
            score += 50


movingInterval = pygame.USEREVENT + 0
pygame.time.set_timer(movingInterval,75)

mixer.music.load('start.wav')
mixer.music.play()

def collisionEnemies():
    global state,enemyState,score
    x = pac_x//rectWid
    y = pac_y//rectWid
    clydex = clyde.centerx//rectWid
    clydey = clyde.centery//rectWid
    pinkyx = pinky.centerx//rectWid
    pinkyy = pinky.centery//rectWid
    blinkyx = blinky.centerx//rectWid
    blinkyy = blinky.centery//rectWid
    cyanx = cyan.centerx//rectWid
    cyany = cyan.centery//rectWid
    if clydex == x and clydey == y and clyde.state == 'chasing':
        state = 'Lost'
    if blinkyx == x and blinkyy == y and blinky.state == 'chasing':
        state = 'Lost'        
    if cyanx == x and cyany == y and cyan.state == 'chasing':
        state = 'Lost'
    if pinkyx == x and pinkyy == y and pinky.state == 'chasing':
        state = 'Lost'
    
def collisionenemies2():
    global state,enemyState,score
    x = pac_x//rectWid
    y = pac_y//rectWid
    clydex = clyde.centerx//rectWid
    clydey = clyde.centery//rectWid
    pinkyx = pinky.centerx//rectWid
    pinkyy = pinky.centery//rectWid
    blinkyx = blinky.centerx//rectWid
    blinkyy = blinky.centery//rectWid
    cyanx = cyan.centerx//rectWid
    cyany = cyan.centery//rectWid
    if clydex == x and clydey == y and clyde.state == 'running':
        score += 200
        clyde.state = 'chasing'
        clyde.centerx = clyde.centerx2
        clyde.centery = clyde.centery2
        clyde.color = 'pink'
    if blinkyx == x and blinkyy == y and blinky.state == 'running':
        score += 200
        blinky.state = 'chasing' 
        blinky.centerx = blinky.centerx2
        blinky.centery = blinky.centery2
        blinky.color = 'red'
    if cyanx == x and cyany == y and cyan.state == 'running':
        score += 200
        cyan.state = 'chasing'
        cyan.centerx = cyan.centerx2
        cyan.centery = cyan.centery2
        cyan.color = 'skyblue'
    if pinkyx == x and pinkyy == y and pinky.state == 'running':
        score += 200
        pinky.state = 'chasing'
        pinky.centerx = pinky.centerx2
        pinky.centery = pinky.centery2
        pinky.color = 'orange'


def levelCompleted():
    global state
    no_of_points = 0
    for i in range(len(map.map)):
        for j in range(len(map.map[0])):
            if map.map[i][j] == 0 or map.map[i][j] == 3:
                no_of_points += 1
    if no_of_points == 0:
        state = 'Win'
            
def victory():
    if state == 'Win':
        font = pygame.font.Font('retroFont.ttf',80)
        text1 = font.render('VICTORY',True,'white')
        text2 = font.render('VICTORY',True,'red')
        screen.blit(text2,(120,208))
        screen.blit(text1,(120,200))

movingInterval2 = pygame.USEREVENT + 3
pygame.time.set_timer(movingInterval2,80)

def lost():
    if state == 'Lost':
        font = pygame.font.Font('retroFont.ttf',80)
        text1 = font.render('DEFEAT',True,'white')
        text2 = font.render('DEFEAT',True,'red')
        screen.blit(text2,(120,208))
        screen.blit(text1,(120,200))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == movingInterval:
            if state == 'notWin':
                movingPacman()
        if event.type == movingInterval2:
            if state == 'notWin':
                pinky.moving()
                clyde.moving()
                blinky.moving()
                cyan.moving()
        if event.type == colorShuffle:
            changingColors()
            index += 1
            if index > len(rainbow_colors) - 1:
                index = 0
        if event.type == pygame.KEYDOWN:
            x = pac_x//rectWid
            y = pac_y//rectWid
            if event.key == pygame.K_SPACE:
                if toggle_border == True:
                    toggle_border = False
                elif toggle_border == False:
                    toggle_border = True
            if event.key == pygame.K_w:
                if x < len(map.map[0]):
                    if map.map[y - 1][x] != 1:
                        dir = 'up'
            if event.key == pygame.K_a:
                if x-1 < len(map.map[0]):
                    if map.map[y][x - 1] != 1:
                        dir = 'left'
            if event.key == pygame.K_d:
                if x+1 < len(map.map[0]):
                    if map.map[y][x + 1] != 1:
                        dir = 'right'
            if event.key == pygame.K_s:
                if x < len(map.map[0]):
                    if map.map[y + 1][x] != 1:
                        dir = 'down'


    screen.fill('black')
    screen.blit(image,(0,0))
    if state == 'notWin':
        colliding()
        displaying_borders()
        pinky.teleportation()
        collisionEnemies()
        collisionenemies2()
        pinky.colliding(map.map)
        pinky.changingDir(map.map)
        clyde.teleportation()
        clyde.colliding(map.map)
        clyde.changingDir(map.map)
        blinky.teleportation()
        blinky.colliding(map.map)
        blinky.changingDir(map.map)
        cyan.teleportation()
        cyan.colliding(map.map)
        cyan.changingDir(map.map)
        teleportation()
        eating()
    map.makingMap()
    displayingPacman()
    pinky.displaying()
    blinky.displaying()
    levelCompleted()
    clyde.displaying()
    cyan.displaying()
    displayingpacman()
    displayingScore()
    lost()
    victory()
    clock.tick(60)
    pygame.display.update()
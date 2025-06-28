import pygame # DO NOT FORGET YOUR BLOODY PARENTHESIS
#Screen setup
pygame.init()
clock = pygame.time.Clock()
screenWidth = 1000
screenHeight = 500
screen = pygame.display.set_mode ((screenWidth, screenHeight))
leftField = 100
rightField = 900
#Classes
class character:
    def __init__(self, square: pygame.Rect, left, right, action, colour,):
        self.square = square.copy()
        self.left = left
        self.right = right
        self.action = action
        self.colour = colour
    def drawSquare(self):
        pygame.draw.rect(screen, self.colour, self.square)
    def moveSquare(self):
        key = pygame.key.get_pressed()
        if key[self.left]:
            self.square.x -= 10
        if key[self.right]:
            self.square.x += 10
        if self.square.left <= leftField:
            self.square.left = leftField
        if self.square.right >= rightField:
            self.square.right = rightField
    def summonSquare(self, B: pygame.Rect):
        key = pygame.key.get_pressed()
        if key[self.action]:
            toggle = True
            while (toggle):
                B.centerx += ((self.square.centerx)-B.centerx)*0.1
                B.centery += ((self.square.centery)-B.centery)*0.1
                if self.square.colliderect(B):
                    toggle = False 

class object:
    def __init__(self, circle: pygame.Rect, speed_x, speed_y, colour):
        self.circle = circle.copy()
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.colour = colour
    def drawCircle(self):
        pygame.draw.ellipse(screen, self.colour, self.circle)
    def collideCircle(self, B: pygame.Rect):
        self.circle.centerx += self.speed_x
        self.circle.centery += self.speed_y
        if self.circle.colliderect(B):
            self.speed_x = 0.1 * (self.circle.centerx - B.centerx)
            self.speed_y *= -1
    def tennisCircle(self):
        global redScore, blueScore, bluelatch, redlatch
        if self.circle.left <= leftField or self.circle.right >= rightField:
            self.speed_x *= -1
        if self.circle.top <= 0:
            bluelatch = True
        if self.circle.bottom >= screenHeight:
            redlatch = True
        if bluelatch or redlatch:
            self.circle.center = (screenWidth/2, screenHeight/2)
            self.speed_x = 0
            self.speed_y = 0
    def volleyCircle(self):
        global redScore, blueScore, redlatch, bluelatch
        self.speed_y += 0.035
        if self.circle.left <= leftField or self.circle.right >= rightField:
            self.speed_x *= -1
        if self.circle.bottom >= screenHeight:
            if self.circle.centerx < (screenWidth/2):
                bluelatch = True
                self.circle.center = (screenWidth*0.75, 0)
            elif self.circle.centerx > (screenWidth/2):
                redlatch = True
                self.circle.center = (screenWidth*0.25, 0)
            else: self.circle.center = (screenWidth*0.25, 0)
            self.speed_x = 0
            self.speed_y = 0

# Colours
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
white = (255, 255, 255)

# Squares
RectA = pygame.Rect((leftField, screenHeight-20, 80, 20))
RectB = pygame.Rect((leftField, (screenHeight/2-5), 600, 10))
RectC = pygame.Rect((screenWidth/2, screenHeight/2, 30, 30))
RectD = pygame.Rect((screenWidth/2-5, screenHeight*0.66, 10, screenHeight/3))

# characters
Player1 = character(RectA, pygame.K_a, pygame.K_d, pygame.K_w, red)
Player2 = character(RectA, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP,blue)
LineHor = character(RectB, 0, 0, 0, white)
LineVer = character(RectD, 0, 0, 0, white)
RightWall = character(RectD, 0, 0, 0, white)
LeftWall = character(RectD, 0, 0, 0, white)

# objects
Ball = object(RectC, 0, 0, green)
ScoreLeft = object(RectC, 0, 0, magenta)
ScoreRight = object(RectC, 0, 0, cyan)

# Score
redScore = 0
blueScore = 0
redlatch = False
bluelatch = False

#Game loop
run = True
while run:
    # Score
    if redlatch == True:
            redScore +=1
            redlatch = False
    if bluelatch == True:
        blueScore +=1
        bluelatch = False
    if redScore == 8 or blueScore == 8:
        redScore = 0
        blueScore = 0

    # Mechanics
    screen.fill((0,0,0))

    RightWall.drawSquare()
    RightWall.square.centerx = rightField
    LeftWall.drawSquare()
    LeftWall.square.centerx = leftField
    
    Player1.drawSquare()
    Player1.moveSquare()
    Player1.summonSquare(Ball.circle)

    Player2.drawSquare()
    Player2.moveSquare()
    Player2.summonSquare(Ball.circle)

    LineVer.drawSquare()

    Ball.drawCircle()
    Ball.collideCircle(Player1.square)
    Ball.collideCircle(Player2.square)
    Ball.collideCircle(LineVer.square)
    Ball.volleyCircle()
    
    ScoreLeft.drawCircle()
    ScoreLeft.circle.top = screenHeight*(redScore/8)
    ScoreRight.drawCircle()
    ScoreRight.circle.top = screenHeight*(blueScore/8)
    
    
    #Game mode select
    gameMode = pygame.key.get_pressed()
    if (gameMode[pygame.K_1]) and (state):
        Player1.square.center = (screenWidth*0.25, screenHeight-10)
        Player2.square.center = (screenWidth*0.75, screenHeight-10)
        Ball.circle.center = (screenWidth/2, screenHeight/2)
        ScoreLeft.circle.center = (leftField - 50, 15)
        ScoreRight.circle.center = (rightField + 50, 15)
        state = False
    else: state = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit
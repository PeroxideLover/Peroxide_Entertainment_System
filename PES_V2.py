import pygame # DO NOT FORGET YOUR BLOODY PARENTHESIS
#Screen setup
pygame.init()
clock = pygame.time.Clock()
screenWidth = 840
screenHeight = 640
screen = pygame.display.set_mode ((screenWidth, screenHeight))
leftField = 100
rightField = 700
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
    def bounceCircle(self, B: pygame.Rect):
        global latch, redScore, blueScore, bluelatch, redlatch
        keyup = pygame.key.get_pressed()
        self.circle.centerx += self.speed_x
        self.circle.centery += self.speed_y
        if self.circle.colliderect(B):
            self.speed_x = 0.1 * (self.circle.centerx - B.centerx)
            self.speed_y = 0.1 * (self.circle.centery - B.centery)
        if self.circle.left <= leftField or self.circle.right >= rightField:
            self.speed_x *= -1
        if self.circle.top <= 0:
            self.speed_x = 0
            self.speed_y = 0
            self.circle.center = (screenWidth/2, screenHeight/2)
            bluelatch = True
        if self.circle.bottom >= screenHeight:
            self.speed_x = 0
            self.speed_y = 0
            redlatch = True
            self.circle.center = (screenWidth/2, screenHeight/2)


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
RectD = pygame.Rect((screenWidth/2-5, screenHeight, 10, screenHeight/2))
# characters
Player1 = character(RectA, pygame.K_a, pygame.K_d, pygame.K_w, red)
Player2 = character(RectA, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP,blue)
LineHor = character(RectB, 0, 0, 0, white)
LineVer = character(RectB, 0, 0, 0, white)
Floor = character(RectB, 0, 0, 0, white)
Roof = character(RectB, 0, 0, 0, white)

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

    # Mechanics
    screen.fill((0,0,0))
    
    Player1.drawSquare()
    Player1.moveSquare()
    Player1.summonSquare(Ball.circle)

    Player2.drawSquare()
    Player2.moveSquare()
    Player2.summonSquare(Ball.circle)

    LineHor.drawSquare()

    Ball.drawCircle()
    Ball.bounceCircle(Player1.square)
    Ball.bounceCircle(Player2.square)
    
    ScoreLeft.drawCircle()
    ScoreLeft.circle.top = screenHeight*(redScore/8)
    ScoreRight.drawCircle()
    ScoreRight.circle.top = screenHeight*(blueScore/8)
    
    
    #Game mode select
    gameMode = pygame.key.get_pressed()
    if (gameMode[pygame.K_1]) and (state):
        Player1.square.center = (screenWidth/2, 10)
        Player2.square.center = (screenWidth/2, screenHeight-10)
        LineHor.square.center = (screenWidth/2, screenHeight/2)
        
        Ball.speed_x = 0
        Ball.speed_y = 0
        Ball.circle.center = (screenWidth/2, screenHeight/2)
        ScoreLeft.circle.center = (leftField/2, 15)
        ScoreRight.circle.center = (rightField + 50, 15)
        state = False
    else: state = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit
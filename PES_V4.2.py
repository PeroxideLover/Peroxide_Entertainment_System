import pygame, math # DO NOT FORGET YOUR BLOODY PARENTHESIS
#Screen setup
pygame.init()
clock = pygame.time.Clock()
screenWidth = 800
screenHeight = 700
screen = pygame.display.set_mode ((screenWidth, screenHeight))
ScoreField = 100
pygame.display.set_caption("Peroxide Entertainment System")

test = pygame.image.load("image.png")
test = pygame.transform.scale(test, (screenWidth, screenHeight-ScoreField))
global Key
#Classes
class point:
    def __init__(self, PosX, PosY, radius, colour):
        self.PosX = PosX
        self.PosY = PosY
        self.location = pygame.math.Vector2(self.PosX, self.PosY)
        self.colour = (white)
        self.radius = radius
        self.speedX = 5
        self.speedY = 0
        self.colour = colour
        
    def drawCircle(self):
        pygame.draw.circle(screen, self.colour, self.location, self.radius)
    def drawLine(self):
        pygame.draw.line(screen, self.colour,(self.PosX, self.PosY-300),(self.PosX,self.PosY + 300),self.radius)
    def drawSquare(self):
        self.rectangle=pygame.Rect((self.PosX - self.radius),(self.PosY - self.radius),self.radius*2,self.radius*2)
        pygame.draw.rect(screen, self.colour, self.rectangle)
    def moveLocation(self, direction: list):
        if key[direction[0]]:
            self.PosY -= 15
        if key[direction[1]]:
            self.PosY += 15
        if key[direction[2]]:
            self.PosX -= 15
        if key[direction[3]]:
            self.PosX += 15
        if self.PosX <= 0:
            self.PosX = 0
        if self.PosX >= screenWidth:
            self.PosX = screenWidth
        if self.PosY >= screenHeight - self.radius:
            self.PosY = screenHeight - self.radius
        if self.PosY <= ScoreField + self.radius:
            self.PosY = ScoreField + self.radius
        self.location = (self.PosX, self.PosY)
    def collision(self, A: pygame.Rect):
        if A.collidepoint(self.location):
            self.speedX *= -1
            self.speedY = 0.15 * (self.PosY - A.centery)
    def bounce(self):
        global LeftScore, RightScore
        if self.PosX >= screenWidth or self.PosX <= 0:
            if self.PosX >= screenWidth:
                RightScore += 1
            if self.PosX <= 0:
                LeftScore += 1
            self.speedX *= -1
        if self.PosY >= screenHeight or self.PosY <= ScoreField:
            self.speedY *= -1
        self.PosX += self.speedX
        self.PosY += self.speedY
        self.location = pygame.Vector2(self.PosX, self.PosY)
    def clock(self, wall: pygame.Vector2):
        self.bounce()
        wall[0] = 10
        self.PosY = (screenHeight+ScoreField)/2
        if self.PosX <= wall[0]:
            self.speedX *= -1
    def tag(self, A: pygame.Vector2, respawn):
        if self.rectangle.collidepoint(A):
            self.colour = black
        elif key[respawn]:
            self.colour = white
    def handball(self, wall: pygame.Vector2):
        global LeftScore, RightScore
        wall[0] = 5
        if self.PosX <= wall[0]:
            self.speedX *= -1
        if self.PosY <= ScoreField or self.PosY >= screenHeight:
            self. speedY *= -1
        if self.PosX >= screenWidth:
            if self.PosY >= (screenHeight + ScoreField)/2:
                LeftScore += 1
            else: RightScore += 1
            self.speedX *= -1
        self.PosX += self.speedX
        self.PosY += self.speedY
        self.location = (self.PosX, self.PosY)
        



            
class number:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
    def drawNumber(self):
        font = pygame.font.SysFont(None, 100)
        image = (font.render(self.text, False, white))
        screen.blit(image,(self.x, self.y))

# Colours
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
white = (255, 255, 255)
grey = (128, 128, 128)
black = (0, 0, 0)

# characters
Player1 = point(0, (screenHeight + ScoreField)/2, 35, white)
Player2 = point(screenWidth, (screenHeight + ScoreField)/2, 35, white)
Line = point(screenWidth/2, (screenHeight + ScoreField)/2, 5, white)
Ball = point(screenWidth/2, 400, 15, white)

# Movement
Move1 = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]
Move2 = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]

# Score
LeftScore = 0
RightScore = 0
LeftLatch = False
RightLatch = False
LeftNumber = number(str(LeftScore), 60, 10)
RightNumber = number(str(RightScore), screenWidth-100, 10)

#Games
Blank = False
Tennis = True
Race = False
Hockey = False
Tag = False
Shooter = False
gameSet = [Blank, Tennis, Race, Hockey, Tag, Shooter]
def clearSet():
    for i in range(len(gameSet)):
            gameSet[i] = False

Key = pygame.key.get_pressed()

#Game loop
run = True
while run:
    # Score
    key = pygame.key.get_pressed()
    if LeftLatch == True:
        LeftScore +=1
        LeftLatch = False
    if RightLatch == True:
        RightScore +=1
        RightLatch = False
    if key[pygame.K_SPACE]:
        LeftScore = 0
        RightScore = 0
    LeftNumber.text = str(LeftScore)
    RightNumber.text = str(RightScore)

    #Game mode select
    if key[pygame.K_0]:
        clearSet()
    if key[pygame.K_1]:
        clearSet()
        gameSet[1] = True
    if key[pygame.K_2]:
        clearSet()
        gameSet[2] = True
    if key[pygame.K_3]:
        clearSet()
        gameSet[3] = True
    if key[pygame.K_4]:
        clearSet()
        gameSet[4] = True
    if key[pygame.K_5]:
        clearSet()
        gameSet[5] = True
    
    # Mechanics
    screen.fill((0,0,0))

    if gameSet[1]:
       Line.PosX = screenWidth/2
       Line.drawLine()
       Player1.drawSquare()
       Player1.moveLocation(Move1)
       Player2.drawSquare()
       Player2.moveLocation(Move2)
       Ball.drawCircle()
       Ball.bounce()
       Ball.collision(Player1.rectangle)
       Ball.collision(Player2.rectangle)
       
    if gameSet[2]:
        Player1.drawSquare()
        Player1.moveLocation(Move1)
        Player2.drawSquare()
        Player2.moveLocation(Move2)
        Ball.clock(Line.location)
    
    if gameSet[3]:
        Player1.drawSquare()
        Player1.moveLocation(Move1)
        Player2.drawSquare()
        Player2.moveLocation(Move2)
        Ball.drawCircle()
        Ball.bounce()
        Ball.collision(Player1.rectangle)
        Ball.collision(Player2.rectangle)

    if gameSet[4]:
        screen.blit(test, (0, 100))
        Player1.drawSquare()
        Player1.moveLocation(Move1)
        Player2.drawSquare()
        Player2.moveLocation(Move2)
        Player2.tag(Player1.location, pygame.K_RSHIFT)
        Ball.clock(Line.location)
    
    if gameSet[5]:
        Line.PosX = 200
        Player1.drawSquare()
        Player1.moveLocation(Move1)
        Player2.drawSquare()
        Player2.moveLocation(Move2)
        Ball.collision(Player1.rectangle)
        Ball.collision(Player2.rectangle)
        Ball.drawCircle()
        Ball.handball(Line.location)

    LeftNumber.drawNumber()
    RightNumber.drawNumber()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit
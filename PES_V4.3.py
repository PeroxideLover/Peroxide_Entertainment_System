import pygame, random # DO NOT FORGET YOUR BLOODY PARENTHESIS
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
global Key, LeftScore, RightScore
#Classes
class point:
    def __init__(self, PosX, PosY, radius, colour):
        self.PosX = PosX
        self.PosY = PosY
        self.location = pygame.math.Vector2(self.PosX, self.PosY)
        self.colour = (white)
        self.radius = radius
        self.speedX = 0
        self.speedY = 0
        self.colour = colour
        
    def drawCircle(self):
        pygame.draw.circle(screen, self.colour, self.location, self.radius)
    def drawLine(self):
        pygame.draw.line(screen, self.colour,(self.PosX, self.PosY),(self.PosX,self.PosY + self.radius),10)
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
            self.speedX *= -1
        if self.PosY >= screenHeight or self.PosY <= ScoreField:
            self.speedY *= -1
        self.PosX += self.speedX
        self.PosY += self.speedY
        self.location = pygame.Vector2(self.PosX, self.PosY)
    def clock(self):
        global LeftScore
        self.bounce()
        self.PosY = (screenHeight+ScoreField)/2
        if self.PosX <= 0 or self.PosX >= screenWidth:
            LeftScore += 1
    def tennis(self):
        global LeftScore, RightScore
        self.bounce()
        if self.PosX >= screenWidth:
            LeftScore += 1
        if self.PosX <= 0:
            RightScore += 1
    def hockey(self):
        global LeftScore, RightScore
        self.bounce()
        if self.PosX >= screenWidth:
            if self.PosY >= 300 and self.PosY <= 500:
                LeftScore += 1
        if self.PosX <= 0:
            if self.PosY >= 300 and self.PosY <= 500:
                RightScore += 1
    def tag(self, A: pygame.Vector2):
        if self.rectangle.collidepoint(A) or self.PosX >= screenWidth:
            self.rectangle.right = screenWidth
            self.colour = grey
        self.PosX += self.speedX
        self.PosY += self.speedY
        self.location = pygame.Vector2(self.PosX, self.PosY)
    def gamble(self):
        if key[pygame.K_SPACE]:
            self.PosX = random.randint(0, screenWidth)
            self.PosY = random.randint(ScoreField, (500))
            self.location = (self.PosX, self.PosY)
    def volleyball(self, wall: pygame.Vector2):
        global LeftScore, RightScore
        self.bounce()
        if self.PosY >= screenHeight:
            if self.PosX <= (screenWidth)/2:
                RightScore += 1
            else: LeftScore += 1
        if self.PosY >= 500 and self.PosX == wall[0]:
            self.speedX *= -1
    def handball(self):
        global LeftScore, RightScore
        self.bounce()
        if self.PosX <= 0:
            if self.PosY >= (screenHeight + ScoreField)/2:
                RightScore += 1
            else: LeftScore += 1
            
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
Player1 = point(0, (screenHeight + ScoreField)/2, 40, white)
Player2 = point(screenWidth, (screenHeight + ScoreField)/2, 40, white)
Line = point(screenWidth/2, ScoreField, 600, white)
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
Singles = False
Volleyball = False
Handball = False
gameSet = [Blank, Tennis, Race, Hockey, Tag, Shooter, Singles, Volleyball, Handball]
def clearSet():
    for i in range(len(gameSet)):
            global LeftScore, RightScore
            gameSet[i] = False
            LeftScore = 0
            RightScore = 0

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
        Ball.speedY = 0
        Ball.speedX = 10
        Ball.PosX = Player1.PosX + Player1.radius
        Ball.PosY = Player1.PosY
        Ball.colour = white
        Player2.colour = white

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
    if key[pygame.K_6]:
        clearSet()
        gameSet[6] = True
    if key[pygame.K_7]:
        clearSet()
        gameSet[7] = True
    if key[pygame.K_8]:
        clearSet()
        gameSet[8] = True
    
    # Mechanics
    screen.fill((0,0,0))

    if gameSet[1]: #Tennis
       Line.PosY = ScoreField
       Line.drawLine()
       Player1.drawSquare()
       Player1.moveLocation(Move1)
       Player2.drawSquare()
       Player2.moveLocation(Move2)
       Ball.drawSquare()
       Ball.tennis()
       Ball.collision(Player1.rectangle)
       Ball.collision(Player2.rectangle)
       
    if gameSet[2]: #Race 
        Player1.drawSquare()
        Player1.moveLocation(Move1)
        Player2.drawSquare()
        Player2.moveLocation(Move2)
        Ball.clock()
    
    if gameSet[3]: #Hockey
        Player1.drawSquare()
        Player1.moveLocation(Move1)
        Player2.drawSquare()
        Player2.moveLocation(Move2)
        Ball.drawSquare()
        Ball.hockey()
        Ball.collision(Player1.rectangle)
        Ball.collision(Player2.rectangle)

    if gameSet[4]: #Tag
        screen.blit(test, (0, 100))
        Player2.drawSquare()
        Player2.moveLocation(Move2)
        Player1.drawSquare()
        Player1.moveLocation(Move1)
        Player2.tag(Player1.location)
        Ball.clock()
    
    if gameSet[5]: #Shooter
        Ball.drawSquare()
        Player1.drawSquare()
        Player1.moveLocation(Move1)
        Player2.drawSquare()
        Player2.moveLocation(Move2)
        Player2.tag(Ball.location)
        Ball.tag(Player2.location)
        Ball.bounce
        Ball.collision(Player1.rectangle)

    if gameSet[6]: #singles
        Ball.drawSquare()
        Ball.gamble()

    if gameSet[7]: #Volleyball
        Line.PosY = 500
        Line.drawLine()
        Player1.drawSquare()
        Player1.moveLocation(Move1)
        Player2.drawSquare()
        Player2.moveLocation(Move2)
        Ball.drawSquare()
        Ball.volleyball(Line.location)
        Ball.collision(Player1.rectangle)
        Ball.collision(Player2.rectangle)

    if gameSet[8]: #Handball
        Player1.drawSquare()
        Player1.moveLocation(Move1)
        Player2.drawSquare()
        Player2.moveLocation(Move2)
        Ball.collision(Player1.rectangle)
        Ball.collision(Player2.rectangle)
        Ball.drawSquare()
        Ball.handball()

    LeftNumber.drawNumber()
    RightNumber.drawNumber()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit
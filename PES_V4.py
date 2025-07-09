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
        self.speedX = 2
        self.speedY = 0
        self.colour = colour
        
    def drawCircle(self):
        pygame.draw.circle(screen, self.colour, self.location, self.radius)
    def drawLine(self):
        pygame.draw.line(screen, self.colour, (self.PosX, self.PosY - 300), (self.PosX, self.PosY + 300), 5)
    def drawSquare(self):
        self.rectangle=pygame.Rect((self.PosX - self.radius),(self.PosY - self.radius),self.radius*2,self.radius*2)
        pygame.draw.rect(screen, self.colour, self.rectangle)
    def moveLocation(self, Up, Down, Left, Right):
        if key[Up]:
            self.PosY -= 15
        if key[Down]:
            self.PosY += 15
        if key[Left]:
            self.PosX -= 15
        if key[Right]:
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
        global LeftLatch, RightLatch
        if A.collidepoint(self.location):
            self.speedX *= -1
            self.speedY = 0.1 * (self.PosY - A.centery)
        if self.PosY > screenHeight or self.PosY < ScoreField:
            self.speedY *= -1
        if self.PosX > screenWidth + 50:
            LeftLatch = True
            RightLatch = False
            self.speedX = 0
            self.speedY = 0
        if self.PosX < -50:
            RightLatch = True
            LeftLatch = False
            self.speedX = 0
            self.speedY = 0
        self.PosX += self.speedX
        self.PosY += self.speedY
        self.location = pygame.Vector2(self.PosX, self.PosY)
    def CatandMouse(self, catLeft: pygame.Rect, catRight: pygame.Rect,):
        global LeftLatch, RightLatch
        if catLeft.collidepoint(self.location):
            RightLatch = True
            self.colour = black
        if catRight.collidepoint(self.location):
            LeftLatch = True
            self.colour = black

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
Player1 = point(0, 400, 40, red)
Player2 = point(screenWidth, 400, 40, blue)
Line = point(screenWidth/2, (screenHeight + ScoreField)/2, 10, white)
Ball = point(screenWidth/2, 400, 15, green)

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
Tag = False
Shooter = False
Baseball = False
gameSet = [Blank, Tennis, Tag, Shooter, Baseball]
def clearSet():
    for i in range(len(gameSet)):
            gameSet[i] = False

Key = pygame.key.get_pressed()

#Game loop
run = True
while run:
    # Score
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        if LeftLatch == True:
            LeftScore +=1
            LeftLatch = False
        if RightLatch == True:
            RightScore +=1
            RightLatch = False
        Line.colour = white
        Ball.speedX = 0
        Ball.speedY = 0
        Ball.PosX = screenWidth/2
        Ball.PosY = (screenHeight + ScoreField)/2

    if key[pygame.K_LSHIFT]:
        Ball.speedX = 5
        Ball.speedY = 0
        Ball.PosX = Line.PosX
        Ball.PosY = Line.PosY
    if key[pygame.K_RSHIFT]:
        Ball.speedX = -5
        Ball.speedY = 0
        Ball.PosX = Line.PosX
        Ball.PosY = Line.PosY
        
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
    
    # Mechanics
    screen.fill((0,0,0))

    if gameSet[1]:
       pass

    if gameSet[2]:
        pass

    if gameSet[3]:
        pass

    if gameSet[4]:
        screen.blit(test, (0, 100))
    
    Player1.drawSquare()
    Player1.moveLocation(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    Player2.drawSquare()
    Player2.moveLocation(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    Line.drawLine()
    Line.drawCircle()
    Line.moveLocation(pygame.K_t, pygame.K_g, pygame.K_f, pygame.K_h)
    Line.CatandMouse(Player1.rectangle, Player2.rectangle)
    Ball.drawCircle()
    Ball.collision(Player1.rectangle)
    Ball.collision(Player2.rectangle)
    LeftNumber.drawNumber()
    RightNumber.drawNumber()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit
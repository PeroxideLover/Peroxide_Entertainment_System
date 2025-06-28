import pygame # DO NOT FORGET YOUR BLOODY PARENTHESIS
#Screen setup
pygame.init()
clock = pygame.time.Clock()
screenWidth = 800
screenHeight = 700
screen = pygame.display.set_mode ((screenWidth, screenHeight))
ScoreField = 100
pygame.display.set_caption("Peroxide Entertainment System")
#Classes
class character:
    def __init__(self, square: pygame.Rect, left, right, up, down, colour,):
        self.square = square.copy()
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.colour = colour
        self.OGCol = colour
    def drawSquare(self):
        pygame.draw.rect(screen, self.colour, self.square)
    def moveSquare(self):
        key = pygame.key.get_pressed()
        if key[self.left]:
            self.square.x -= 15
        if key[self.right]:
            self.square.x += 15
        if key[self.up]:
            self.square.y -= 15
        if key[self.down]:
            self.square.y += 15
        if self.square.right <= 0:
            self.square.right = 0 + 10
        if self.square.left >= screenWidth:
            self.square.left = screenWidth -10
        if self.square.top >= screenHeight:
            self.square.top = screenHeight - 10
        if self.square.bottom <= ScoreField:
            self.square.bottom = ScoreField + 10
    def CatandMouse(self, B: pygame.Rect, C: pygame.Rect):
        global redlatch, bluelatch
        if self.square.colliderect(B):
            self.square.center = (screenWidth-30, screenHeight-30)
            B.center = (30, ScoreField+30)
            redlatch = True
        if self.square.colliderect(C):
            self.square.center = (screenWidth-30, screenHeight-30)
            B.center = (30, ScoreField+30)
            bluelatch = True

class Circle:
    def __init__(self, circle: pygame.Rect, speed_x, speed_y, colour):
        self.circle = circle.copy()
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.colour = colour
    def drawCircle(self):
        pygame.draw.ellipse(screen, self.colour, self.circle, )
    def collideCircle(self, B: pygame.Rect):
        self.circle.centerx += self.speed_x
        self.circle.centery += self.speed_y
        if self.circle.colliderect(B):
            self.speed_x = 0.05 * (self.circle.centerx - B.centerx)
            self.speed_y = 0.05 * (self.circle.centery - B.centery)
    def tennisCircle(self, net: pygame.Rect):
        global bluelatch, redlatch
        if self.circle.left <= 0:
            bluelatch = True
        if self.circle.right >= screenWidth:
            redlatch = True
        if self.circle.top <= ScoreField or self.circle.bottom >= screenHeight:
            self.speed_y *= -1
        if bluelatch or redlatch:
            self.circle.center = screenWidth/2, screenHeight-300
            self.speed_x = 0
            self.speed_y = 0
    def summonCircle(self, B: pygame.Rect, action):
        key = pygame.key.get_pressed()
        self.circle.y += self.speed_y
        self.circle.x += self.speed_x
        if key[action]:
            self.speed_x = 0.01*(B.centerx-self.circle.centerx)
            self.speed_y = 0.01*(B.centery-self.circle.centery)
    def shootCircle(self, B: pygame.Rect, left, right):
        key = pygame.key.get_pressed()
        if key[left]:
            self.circle.center = (B.left - 20 , B.centery)
            self.speed_x = -10
        if key[right]:
            self.circle.center = (B.right + 20, B.centery)
            self.speed_x = 10
class number:
    def __init__(self, text, colour, x, y):
        self.text = text
        self.colour = colour
        self.x = x
        self.y = y
    def drawNumber(self):
        font = pygame.font.SysFont(None, 100)
        image = (font.render(self.text, False, self.colour))
        screen.blit(image,(self.x, self.y))


# Colours
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
white = (255, 255, 255)
Grey = (128, 128, 128)

# Squares
RectA = pygame.Rect((0, ScoreField, 60, 60))
RectB = pygame.Rect((0, (screenHeight/2-5), 600, 10))
RectC = pygame.Rect((screenWidth/2-15, screenHeight-315, 30, 30))
RectD = pygame.Rect((screenWidth/2-0.5, 0, 1, screenHeight))
RectE = pygame.Rect((0, 0, screenWidth, ScoreField))

# characters
Player1 = character(RectA, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, red)
Player2 = character(RectA, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, blue)
LineHor = character(RectB, 0, 0, 0, 0, white)
LineVer = character(RectD, 0, 0, 0, 0, white)
Roof = character(RectE, 0, 0, 0, 0, Grey)

# circles
Ball = Circle(RectC, 0, 0, green)
Cheese = Circle(RectC, 0, 0, yellow)

# Score
redScore = 0
blueScore = 0
redlatch = False
bluelatch = False
RedNumber = number(str(redScore), red, 30, 10)
BluNumber = number(str(blueScore), blue, screenWidth-70, 10)

#Games
Blank = True
Tennis = False
Tag = False
Shooter = False
Baseball = False
gameSet = [Blank, Tennis, Tag, Shooter, Baseball, ]
#Game loop
run = True
while run:
    # Score
    if redlatch == True and redScore <= 8:
        redScore +=1
        redlatch = False
    if bluelatch == True and blueScore <= 8:
        blueScore +=1
        bluelatch = False
    RedNumber.text = str(redScore)
    BluNumber.text = str(blueScore)
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        redScore = 0
        blueScore = 0
        Ball.circle.center = (screenWidth/2, screenHeight -300)
        Ball.speed_y = 0
        Ball.speed_x = 0
    #Game mode select
    if key[pygame.K_0]:
        for i in range(len(gameSet)):
            gameSet[i] = False
    if key[pygame.K_1]:
        for i in range(len(gameSet)):
            gameSet[i] = False
        gameSet[1] = True
    if key[pygame.K_2]:
        for i in range(len(gameSet)):
            gameSet[i] = False
        gameSet[2] = True
    if key[pygame.K_3]:
        for i in range(len(gameSet)):
            gameSet[i] = False
        gameSet[3] = True
    if key[pygame.K_4]:
        for i in range(len(gameSet)):
            gameSet[i] = False
        gameSet[4] = True
    # Mechanics
    screen.fill((0,0,0))
    Player1.drawSquare()
    Player1.moveSquare()
    Player2.drawSquare()
    Player2.moveSquare()

    if gameSet[1]:
        LineVer.drawSquare()
        Ball.drawCircle()
        Ball.collideCircle(Player1.square)
        Ball.collideCircle(Player2.square)
        Ball.summonCircle(Player1.square, pygame.K_LSHIFT)
        Ball.summonCircle(Player2.square, pygame.K_RSHIFT)
        Ball.tennisCircle(LineVer.square)

    if gameSet[2]:
        Player2.CatandMouse(Player1.square, Cheese.circle)
        Cheese.drawCircle()

    if gameSet[3]:
        Player2.CatandMouse(Ball.circle, Cheese.circle)
        Ball.drawCircle()
        Ball.collideCircle(Player1.square)
        Ball.collideCircle(Player2.square)
        Ball.shootCircle(Player1.square, pygame.K_q, pygame.K_e)
        Cheese.drawCircle()
        Cheese.circle.center = (200, 200)

    if gameSet[4]:
        Ball.drawCircle()
        Ball.collideCircle(Player1.square)
        Ball.collideCircle(Player2.square)
        Ball.shootCircle(Player1.square, pygame.K_q, pygame.K_e)
        Ball.shootCircle(Player2.square, pygame.K_RSHIFT, pygame.K_KP_1)
        Ball.tennisCircle(LineVer.square)
        LineVer.drawSquare()
        
    Roof.drawSquare()
    RedNumber.drawNumber()
    BluNumber.drawNumber()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit
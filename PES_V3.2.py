import pygame # DO NOT FORGET YOUR BLOODY PARENTHESIS
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

#Classes
class character:
    def __init__(self, square: pygame.Rect, colour, speed_y, speed_x):
        self.square = square.copy()
        self.colour = colour
        self.OGCol = colour
        self.speed_y = speed_y
        self.speed_x = speed_x
    def drawSquare(self):
        pygame.draw.rect(screen, self.colour, self.square, 0, border_radius= 20)
    def drawCircle(self):
        pygame.draw.ellipse(screen, self.colour, self.square,)
    def moveSquare(self, Left, Right, Up, Down):
        key = pygame.key.get_pressed()
        if key[Left]:
            self.square.x -= 15
        if key[Right]:
            self.square.x += 15
        if key[Up]:
            self.square.y -= 15
        if key[Down]:
            self.square.y += 15
        if self.square.right <= 0:
            self.square.right = 0 + 10
        if self.square.left >= screenWidth:
            self.square.left = screenWidth -10
        if self.square.top >= screenHeight:
            self.square.top = screenHeight - 10
        if self.square.bottom <= ScoreField:
            self.square.bottom = ScoreField + 10
    def collideCircle(self, B: pygame.Rect):
        self.square.centerx += self.speed_x
        self.square.centery += self.speed_y
        if self.square.colliderect(B):
            self.speed_x = 0.08 * (self.square.centerx - B.centerx)
            self.speed_y = 0.08 * (self.square.centery - B.centery)
    def shootCircle(self, B: pygame.Rect, left, right):
        key = pygame.key.get_pressed()
        if key[left]:
            self.square.center = (B.left - 20 , B.centery)
            self.speed_x = -10
            self.speed_y = 0
        if key[right]:
            self.square.center = (B.right + 20, B.centery)
            self.speed_x = 10
            self.speed_y = 0
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
    def tennisCircle(self, net: pygame.Rect):
        global bluelatch, redlatch
        if self.square.left <= 0:
            bluelatch = True
        if self.square.right >= screenWidth:
            redlatch = True
        if self.square.top <= ScoreField or self.square.bottom >= screenHeight:
            self.speed_y *= -1
        if bluelatch or redlatch:
            self.square.center = screenWidth/2, screenHeight-300
            self.speed_x = 0
            self.speed_y = 0



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
Player1 = character(RectA, red, 0, 0)
Player2 = character(RectA, blue, 0, 0)
LineHor = character(RectB, white, 0, 0)
LineVer = character(RectD, white, 0, 0,)
Roof = character(RectE, Grey, 0, 0)
Ball = character(RectC, green, 0, 0)
Cheese = character(RectC, yellow, 0, 0)

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
def clearSet():
    for i in range(len(gameSet)):
            gameSet[i] = False
    Player2.square.center = (screenWidth-30, screenHeight-30)
    Player1.square.center = (30, ScoreField+30)


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
        Ball.square.center = (screenWidth/2, screenHeight -300)
        Ball.speed_y = 0
        Ball.speed_x = 0
    #Game mode select
    if key[pygame.K_0]:
        clearSet()
    if key[pygame.K_1]:
        for i in range(len(gameSet)):
            gameSet[i] = False
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
        LineVer.drawSquare()
        Ball.drawCircle()
        Ball.collideCircle(Player1.square)
        Ball.collideCircle(Player2.square)
        Ball.shootCircle(Player1.square, pygame.K_q, pygame.K_e)
        Ball.shootCircle(Player2.square, pygame.K_RSHIFT, pygame.K_KP_1)
        Ball.tennisCircle(LineVer.square)

    if gameSet[2]:
        Player2.CatandMouse(Player1.square, Cheese.square)
        Cheese.drawCircle()

    if gameSet[3]:
        Player2.CatandMouse(Ball.square, Cheese.square)
        Ball.drawCircle()
        Ball.collideCircle(Player1.square)
        Ball.collideCircle(Player2.square)
        Ball.shootCircle(Player1.square, pygame.K_q, pygame.K_e)
        Cheese.drawCircle()
        Cheese.square.center = (200, 200)

    if gameSet[4]:
        screen.blit(test, (0, 100))

    Player1.drawSquare()
    Player1.moveSquare(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
    Player2.drawSquare()
    Player2.moveSquare(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN,)
    Roof.drawSquare()
    RedNumber.drawNumber()
    BluNumber.drawNumber()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit
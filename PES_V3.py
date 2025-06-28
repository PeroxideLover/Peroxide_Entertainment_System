import pygame # DO NOT FORGET YOUR BLOODY PARENTHESIS
#Screen setup
pygame.init()
clock = pygame.time.Clock()
screenWidth = 1000
screenHeight = 500
screen = pygame.display.set_mode ((screenWidth, screenHeight))
leftField = 100
rightField = 900
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
        if self.square.right <= leftField:
            self.square.right = leftField + 10
        if self.square.left >= rightField:
            self.square.left = rightField -10
        if self.square.bottom >= screenHeight:
            self.square.bottom = screenHeight
        if self.square.top <= 0:
            self.square.top = 0
    def extinquish(self, B: pygame.Rect):
        black = (0,0,0)
        if self.square.colliderect(B):
            self.colour = black
        else: self.colour = self.OGCol
class Circle:
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
            self.speed_x = 0.03 * (self.circle.centerx - B.centerx)
            self.speed_y = 0.03 * (self.circle.centery - B.centery)
    def tennisCircle(self):
        global redScore, blueScore, bluelatch, redlatch
        if self.circle.left <= leftField:
            bluelatch = True
        if self.circle.right >= rightField:
            redlatch = True
        if self.circle.top <= 0 or self.circle.bottom >= screenHeight:
            self.speed_y *= -1
        if bluelatch or redlatch:
            self.circle.center = (screenWidth/2, screenHeight/2)
            self.speed_x = 0
            self.speed_y = 0
    def summonCircle(self, B: pygame.Rect, action):
        key = pygame.key.get_pressed()
        self.circle.y += self.speed_y
        self.circle.x += self.speed_x
        if key[action]:
            self.speed_x = 0.01*(B.centerx-self.circle.centerx)
            self.speed_y = 0.01*(B.centery-self.circle.centery)

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

# Squares
RectA = pygame.Rect((leftField, screenHeight-20, 60, 60))
RectB = pygame.Rect((leftField, (screenHeight/2-5), 600, 10))
RectC = pygame.Rect((screenWidth/2-15, screenHeight/2-15, 30, 30))
RectD = pygame.Rect((screenWidth/2-0.5, 0, 1, screenHeight))
RectE = pygame.Rect((0, 0, leftField, screenHeight))

# characters
Player1 = character(RectA, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, red)
Player2 = character(RectA, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, blue)
LineHor = character(RectB, 0, 0, 0, 0, white)
LineVer = character(RectD, 0, 0, 0, 0, white)
RightWall = character(RectE, 0, 0, 0, 0, white)
LeftWall = character(RectE, 0, 0, 0, 0, white)

# circles
Ball = Circle(RectC, 0, 0, yellow)

# Score
redScore = 0
blueScore = 0
redlatch = False
bluelatch = False
RedNumber = number(str(redScore), red, 30, 200)
BluNumber = number(str(blueScore), blue, screenWidth-70, 200)

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

    # Mechanics
    screen.fill((0,200,0))
    LineVer.drawSquare()
    
    Player1.drawSquare()
    Player1.moveSquare()
    Player1.extinquish(Player2.square)

    Player2.drawSquare()
    Player2.moveSquare()

    Ball.drawCircle()
    Ball.collideCircle(Player1.square)
    Ball.collideCircle(Player2.square)
    Ball.summonCircle(Player1.square, pygame.K_LSHIFT)
    Ball.summonCircle(Player2.square, pygame.K_RSHIFT)
    Ball.tennisCircle()

    RightWall.drawSquare()
    LeftWall.drawSquare()
    LeftWall.square.x = rightField
    RedNumber.drawNumber()
    BluNumber.drawNumber()
    #Game mode select
    gameMode = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit
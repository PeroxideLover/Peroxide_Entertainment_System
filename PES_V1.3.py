import pygame

def ballCollision(Ba: pygame.Rect, increment_X, increment_Y):
    #Physics
    pygame.draw.rect(screen, (0, 255, 0), Ba)
    if Ba.colliderect(playerOne):
        
        increment_Y = deflect * -(playerOne.centery-Ba.centery)
        increment_X = deflect * -(playerOne.centerx-Ba.centerx)
            
    Ba.x += increment_X
    Ba.y += increment_Y
    
    if Ba.top <= 0:
        Ba.top = 0
        increment_Y*= -1
    if Ba.bottom >= screenHeight:
        Ba.bottom = screenHeight
        increment_Y *= -1


pygame.init()
clock = pygame.time.Clock()

screenWidth =  800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Peroxide Entertainment System')

movementSpeed = 5
player1Speed_X = 0
player1Speed_Y = 0
player2Speed_X = 0
player2Speed_Y = 0
deflect = 0.1

playerOne = pygame.Rect((50,(screenHeight/2-30),60,60))
playerTwo = pygame.Rect((690,(screenHeight/2-30),60,60))
ball = pygame.Rect(((screenWidth/2-20), (screenHeight/2-20), 40, 40))
line = pygame.Rect(((screenWidth/2-15),0,30,screenHeight))
volleyBall = pygame.Rect(((screenWidth/2-20), -40, 40, 40))
test = (400, 300, 40, 40)
players = [playerOne, playerTwo]

run = True

while run:
    
    #Physics
    playerOne.x += player1Speed_X
    playerOne.y += player1Speed_Y 
    playerTwo.x += player2Speed_X
    playerTwo.y += player2Speed_Y

    

    if playerOne.bottom <= 5:
        playerOne.bottom = 5
    if playerOne.top >= screenHeight-5:
        playerOne.top = screenHeight-5
    if playerOne.right <= 5:
        playerOne.right = 5
    if playerOne.left >= screenWidth-5:
        playerOne.left = screenWidth-5

    if playerTwo.bottom <= 5:
        playerTwo.bottom = 5
    if playerTwo.top >= screenHeight-5:
        playerTwo.top = screenHeight-5
    if playerTwo.right <= 5:
        playerTwo.right = 5
    if playerTwo.left >= screenWidth-5:
        playerTwo.left = screenWidth-5
    

    #Visuals
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 255, 255), line)
    pygame.draw.rect(screen, (255, 0, 0), playerOne)
    pygame.draw.rect(screen, (0, 0, 255), playerTwo)
    pygame.draw.rect(screen, (255, 255, 0), volleyBall)
    ballCollision(ball, 0, 0)
    ballCollision(volleyBall, 0, 0)

    #User Interface
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            #Red
            if event.key == pygame.K_d:
                player1Speed_X += movementSpeed
            if event.key == pygame.K_a:
                player1Speed_X -= movementSpeed
            if event.key == pygame.K_s:
                player1Speed_Y += movementSpeed
            if event.key == pygame.K_w:
                player1Speed_Y -= movementSpeed
            #Blue
            if event.key == pygame.K_RIGHT:
                player2Speed_X += movementSpeed
            if event.key == pygame.K_LEFT:
                player2Speed_X -= movementSpeed
            if event.key == pygame.K_DOWN:
                player2Speed_Y += movementSpeed
            if event.key == pygame.K_UP:
                player2Speed_Y -= movementSpeed
            #Line
            if event.key == pygame.K_1:
                line.bottom = screenHeight/3
            if event.key == pygame.K_2:
                line.bottom = screenHeight
            if event.key == pygame.K_3:
                line.top = screenHeight*(2/3)
            
            
        if event.type == pygame.KEYUP:
            #Red
            if event.key == pygame.K_d:
                player1Speed_X -= movementSpeed
            if event.key == pygame.K_a:
                player1Speed_X += movementSpeed
            if event.key == pygame.K_s:
                player1Speed_Y -= movementSpeed
            if event.key == pygame.K_w:
                player1Speed_Y += movementSpeed
            #Blue
            if event.key == pygame.K_RIGHT:
                player2Speed_X -= movementSpeed
            if event.key == pygame.K_LEFT:
                player2Speed_X += movementSpeed
            if event.key == pygame.K_DOWN:
                player2Speed_Y -= movementSpeed
            if event.key == pygame.K_UP:
                player2Speed_Y += movementSpeed

    pygame.display.flip()
    clock.tick(60)

pygame.quit
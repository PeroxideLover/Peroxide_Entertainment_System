import pygame

def ballAnimation():
    #Physics
    global ballSpeed_X, ballSpeed_Y
    ball.x += ballSpeed_X
    ball.y += ballSpeed_Y
    if ball.top <= 0:
        ball.top = 0
        ballSpeed_Y *= -1
    if ball.bottom >= screenHeight:
        ball.bottom = screenHeight
        ballSpeed_Y *= -1
        
    
    if ball.colliderect(playerOne):
        ballSpeed_Y = deflect * -(playerOne.centery-ball.centery)
        ballSpeed_X = deflect * -(playerOne.centerx-ball.centerx)

    if ball.colliderect(playerTwo):
        ballSpeed_Y = deflect * -(playerTwo.centery-ball.centery)
        ballSpeed_X = deflect * -(playerTwo.centerx-ball.centerx)

pygame.init()
clock = pygame.time.Clock()

screenWidth =  800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Peroxide Entertainment System')

movementSpeed = 5
ballSpeed_X = 0
ballSpeed_Y = 0
player1Speed_X = 0
player1Speed_Y = 0
player2Speed_X = 0
player2Speed_Y = 0
deflect = 0.1
volleySpeed_X = 0
volleySpeed_Y = 0

playerOne = pygame.Rect((50,(screenHeight/2-30) ,60,60))
playerTwo = pygame.Rect((690,(screenHeight/2-30),60,60))
ball = pygame.Rect(((screenWidth/2-20), (screenHeight/2-20), 40, 40))
line = pygame.Rect(((screenWidth/2-15),0,30,screenHeight))
volleyBall = pygame.Rect(((screenWidth/2-20), -40, 40, 40))
run = True

while run:
    
    ballAnimation()
    #Physics
    playerOne.x += player1Speed_X
    playerOne.y += player1Speed_Y 
    playerTwo.x += player2Speed_X
    playerTwo.y += player2Speed_Y

    ball_X = playerOne.right
    ball_Y = playerOne.centery

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
    pygame.draw.rect(screen, (0, 255, 0), ball)

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
            #ServeA
            if event.key == pygame.K_c:
                ball.centerx = (playerOne)
                ball.centery = (playerOne.right)
            #ServeB
            if event.key == pygame.K_v:
                ball.centerx
                ball.centery = (playerOne.bottom)
            
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
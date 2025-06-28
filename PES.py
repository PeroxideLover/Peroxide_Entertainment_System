import pygame

def ballAnimation():
    #Physics
    global ballSpeed_X, ballSpeed_Y
    ball.x += ballSpeed_X
    ball.y += ballSpeed_Y
    if ball.top < 0 or ball.bottom > screenHeight:
        ballSpeed_Y *= -1
    
    if ball.colliderect(playerOne):
        ballSpeed_X *= -1
        if ball.top > playerOne.top and ball.bottom < playerOne.bottom:
                ballSpeed_Y = 0
        elif ball.top < playerOne.top and ball.bottom < playerOne.bottom:
                ballSpeed_Y = -1
        elif ball.top > playerOne.top and ball.bottom > playerOne.bottom:
                ballSpeed_Y = +1

    if ball.colliderect(playerTwo):
        ballSpeed_X *= -1
        if ball.top > playerTwo.top and ball.bottom < playerTwo.bottom:
            ballSpeed_Y = 0
        elif ball.top < playerTwo.top and ball.bottom < playerTwo.bottom:
            ballSpeed_Y = -1
        elif ball.top > playerTwo.top and ball.bottom > playerTwo.bottom:
            ballSpeed_Y = +1

def ballRestart():
    global ballSpeed_X, ballSpeed_Y
    ball.center = (playerOne.centerx + 50, playerOne.centery)
    ballSpeed_X = 2
    ballSpeed_Y *= 0
pygame.init()
clock = pygame.time.Clock()

screenWidth =  800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Peroxide Entertainment System')

movementSpeed = 6
ballSpeed_X = 0
ballSpeed_Y = 0
player1Speed_X = 0
player1Speed_Y = 0
player2Speed_X = 0
player2Speed_Y = 0

playerOne = pygame.Rect((50,(screenHeight/2-35) ,25,70))
playerTwo = pygame.Rect((752,(screenHeight/2-35),25,70))
ball = pygame.Rect(((screenWidth/8-10), (screenHeight/2-17.5), 35, 35))
line = pygame.Rect(((screenWidth/2-15),0,30,screenHeight))
run = True
while run:
    
    ballAnimation()
    #Physics
    playerOne.x += player1Speed_X
    playerOne.y += player1Speed_Y 
    playerTwo.x += player2Speed_X
    playerTwo.y += player2Speed_Y

    if playerOne.top <= 0:
        playerOne.top =0
    if playerOne.bottom >= screenHeight:
        playerOne.bottom = screenHeight
    if playerOne.left <= 0:
        playerOne.left =0
    if playerOne.right >= screenWidth:
        playerOne.right = screenWidth



    if playerTwo.top <= 0:
        playerTwo.top =0
    if playerTwo.bottom >= screenHeight:
        playerTwo.bottom = screenHeight
    if playerTwo.left <= 0:
        playerTwo.left =0
    if playerTwo.right >= screenWidth:
        playerTwo.right = screenWidth
    

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
            #Restart
            if event.key == pygame.K_SPACE:
                ballRestart()
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
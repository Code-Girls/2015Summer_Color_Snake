# 1 - import library
import pygame                                                 
from pygame.locals import *
import random

# 2 - initialize the game
pygame.init()  
pygame.mixer.init()                                                
width, height = 400, 650                                                                       
screen = pygame.display.set_mode((width, height))
score = 0
velx = 20
running = 1
snake = [[100,370], [100,390], [100,410], [100,430], [100,450]]         #put the snake bodies in the class "snake"
snakecol = [[0], [1], [2], [3], [4]]                                    #each snake color matches each snale position
applepos = [110, 110]
num = 0
lastnum = 0
score = 0
keys = [False, False, False, False]

# 3 - load resources
#load images
background = pygame.image.load("resources/images/background.png")
gameover = pygame.image.load("resources/images/gameover.png")
#load snake body
snake1 = pygame.image.load("resources/images/snake1.png")
snake2 = pygame.image.load("resources/images/snake2.png")
snake3 = pygame.image.load("resources/images/snake3.png")
snake4 = pygame.image.load("resources/images/snake4.png")
snake5 = pygame.image.load("resources/images/snake5.png")
snake6 = pygame.image.load("resources/images/snake6.png")
snake7 = pygame.image.load("resources/images/snake7.png")
snake8 = pygame.image.load("resources/images/snake8.png")
#load apples of different colors
red = pygame.image.load("resources/images/red.png")
orange = pygame.image.load("resources/images/orange.png")
yellow = pygame.image.load("resources/images/yellow.png")
green = pygame.image.load("resources/images/green.png")
blue = pygame.image.load("resources/images/blue.png")
lightBlue = pygame.image.load("resources/images/lightblue.png")
pink = pygame.image.load("resources/images/pink.png")
purple = pygame.image.load("resources/images/purple.png")
#load audio
eat = pygame.mixer.Sound("resources/audio/eat.mp3") 
eat.set_volume(0.5)
pygame.mixer.music.load("resources/audio/background.mp3")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(1)

# position of apple
apples = [red, orange, yellow, green, lightBlue, blue, pink, purple]
appleimg = apples[0]


# 4 - keep looping through
while running:
    # 5 - draw the screen elements
    #background
    screen.blit(background, (0,0)) 
    screen.blit(appleimg, applepos)
    # 6 - loop through the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

    if keys[0]:
        if snake[0][1] -velx <0:
            running = 0
        else:
            for i in range(len(snake)-1, 0, -1):                #count backwards, because the snake wil become longer and longer
                snake[i] = snake[i-1]
            snake[0] = [snake[0][0], snake[0][1]-velx]          #update the snake position
                                
    elif keys[1]:
        if snake[0][0] -velx <0:
            running = 0
        else:
            for i in range(len(snake)-1, 0, -1):
                snake[i] = snake[i-1]
            snake[0] = [snake[0][0]-velx, snake[0][1]]
                                    
    elif keys[2]:
        if snake[0][1] +velx >650:
            running = 0
        else:
            for i in range(len(snake)-1, 0, -1):
                snake[i] = snake[i-1]
            snake[0] = [snake[0][0], snake[0][1]+velx]
                                                
    elif keys[3]:
        if snake[0][0] +velx >400:
            running = 0
        else:
            for i in range(len(snake)-1, 0, -1):
                snake[i] = snake[i-1]
            snake[0] = [snake[0][0]+velx, snake[0][1]]
                                    
    #rect the apple
    applePositionRect = pygame.Rect(red.get_rect())
    applePositionRect.left = applepos[0]
    applePositionRect.top = applepos[1]

    #rect the snake
    snakePositionRect = pygame.Rect(snake1.get_rect())
    snakePositionRect.left = snake[0][0]
    snakePositionRect.top = snake[0][1]

    #check for collisions, when the snake eats an apple, a cube with correspoing color will be connected to the snake tail    
    if snakePositionRect.colliderect(applePositionRect):
        eat.play()
        score += 1
        snake.append([applepos[0], applepos[1]])                    #add the position of the apple to the snake tail
        applepos = [random.randint(0, 381),random.randint(0, 631)]
        lastnum = num
        num = random.randint(0,7)
        appleimg = apples[num]
        screen.blit(appleimg, applepos)                             #a new apple will appear randomly
        snakecol.append([lastnum])                                  #add the apple color to the snake tail
    
    #draw the image of corresponding color to the corresponding snake position
    index = 0
    for s in snake:
        if snakecol[index] == [0]:
            screen.blit(snake1, (s[0],s[1]))
        elif snakecol[index] == [1]:
            screen.blit(snake2, (s[0],s[1]))
        elif snakecol[index] == [2]:
            screen.blit(snake3, (s[0],s[1]))
        elif snakecol[index] == [3]:
            screen.blit(snake4, (s[0],s[1]))
        elif snakecol[index] == [4]:
            screen.blit(snake5, (s[0],s[1]))
        elif snakecol[index] == [5]:
            screen.blit(snake6, (s[0],s[1]))
        elif snakecol[index] == [6]:
            screen.blit(snake7, (s[0],s[1]))
        elif snakecol[index] == [7]:
            screen.blit(snake8, (s[0],s[1]))
        index += 1

    #if the snake touches itself, game over
    index1 = 0
    for body in snake:
        if snake[0][0] == body[0] and snake[0][1] == body[1] and index1 == 1:
            running = 0
        else:
            index1 = 1 

    # score displays while playing
    pygame.font.init()
    font = pygame.font.Font(None, 30)
    scoretext = font.render("Score: " + str(score). zfill(2), True, (255,255,255))
    textRect = scoretext.get_rect()
    textRect.topright = [100,15]
    screen.blit(scoretext, textRect)
    #update the screen
    pygame.display.flip()

pygame.mixer.music.stop()
# 7 - game over display   
if running == 0:
    pygame.mixer.music.load("resources/audio/gameover.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)
    pygame.font.init()
    font = pygame.font.Font(None, 50)
    text = font.render("Score: " + str(score), True, (255,0,0)) 
    textRect = text.get_rect() 
    textRect.centerx = screen.get_rect().centerx  
    textRect.centery = screen.get_rect().centery +15
    screen.blit(gameover, (0,0))
    screen.blit(text, textRect)
    pygame.display.flip()

# 8 - check if the event is the X button
while 1:
    for event in pygame.event.get():                           
        if event.type == pygame.QUIT:
           pygame.quit()
           exit(0)

    

       

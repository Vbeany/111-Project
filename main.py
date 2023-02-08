#import and initializes Pygame
import pygame
from paddle import Paddle

pygame.init()



#define colors to be used for the graphics of the game
light_yellow = (243, 229, 99)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#initialize tallies for the number of lives and the score
score = 0
lives = 5

#creates a window for the game to be displayed on and a title
size = (800, 800)
####################################################
background = pygame.image.load('bg.png')
####################################################

screen = pygame.display.set_mode(size)
pygame.display.set_caption("CSC 111 Final Project: Breakout Game")

####################################################
# I searched up how to add the background -Venus 
icon = pygame.image.load('bg.png')
pygame.display.set_icon(icon)
####################################################

 


sprites_list = pygame.sprite.Group()
 


#this will be used later to stop the game
keep_playing = True

#initialize clock which will keep track of how fast the screen refreshes
clock = pygame.time.Clock()



#gives the computer a position to place the paddle and then adds the new object to sprite list
paddle = Paddle(light_yellow, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560
sprites_list.add(paddle)

#so we can keep adding sprites to the list so they can be drawn in the main loop




#********************************* CREATE THE MAIN LOOP **********************************#

#this tells the computer that if the user clicks on quit, the game is over
while keep_playing:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)  
    
    sprites_list.update()

    screen.fill("blue")

    #################################
    screen.blit(background,(0,0))
    #################################
    
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650, 10))
    #draws all the sprites to the screen
    #putting it in the loop because I want it to be dynamic
    sprites_list.draw(screen)
    
    
   

    pygame.display.flip()

    clock.tick(60)
#quits the game when user clicks their mouse
pygame.quit()



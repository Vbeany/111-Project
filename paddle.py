import pygame
BLACK = (0,0,0)

#creates paddle class
class Paddle(pygame.sprite.Sprite):

  def __init__(self, color, width, height):
    super().__init__()

    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)

    #draw paddle on screen
    pygame.draw.rect(self.image, color, [0, 0, width, height])

    
    self.rect = self.image.get_rect()

#************** Now let's make the paddle able to move **************#

def moveLeft(self, pixels):
        self.rect.x -= pixels
        #don't let the paddle go off the screen
        if self.rect.x < 0:
          self.rect.x = 0

def moveRight(self, pixels):
        self.rect.x += pixels
        #don't let the paddle go off the screen
        if self.rect.x > 800:
          self.rect.x = 800
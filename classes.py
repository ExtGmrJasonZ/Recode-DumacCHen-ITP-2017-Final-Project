from pygame import *    #import the * from pygame
from pygame.sprite import * #import the * from pygame.sprite

class Jet(Sprite):      #Class jet inheriting the sprite
    """initialize the jet"""

    def __init__(self, screen): #Constructor for the jet inside the screen
        Sprite.__init__(self)
        """initialize the Jet"""
        self.image = image.load("battlejet.png")    # load the jet image
        self.image = pygame.transform.scale(self.image, (90, 50))   # set the size of the jet inside the creenn
        self.rect = self.image.get_rect() # get rectangle for the image
        self.rect.x = 10    # rectangle base = 10
        self.rect.y = 50    # rectangle height = 50
        self.screen = screen    # initiate scree
        self.move_speed = 10     # moving speed for the jet
        """bullet"""
        self.firerates = 10      # fire rates for the bullets

    def moveleft(self):     # define move left
        self.rect.x -= self.move_speed      #set the jet to move to the left
        display.flip()      #display

    def moveright(self):      # define move right
        self.rect.x += self.move_speed      # set the jet to move to the right
        display.flip()      #display

    def moveup(self):       # define move up
        self.rect.y -= self.move_speed      # set the jet to move up
        display.flip()      #display

    def movedown(self):     # define move down
        self.rect.y += self.move_speed      # set the jet to move down
        display.flip()      #display


class Star_bg:      #class for star background
    #resourse of the backgound setting
    def __init__(self,background):      # define the constructor for the background
        self.background=image.load(background)  # loading the image
        self.background=pygame.transform.scale(self.background,(1000,1000)) # setting the size of the image
        self.background_size=self.background.get_size() # get the size
        self.background_rect=self.background.get_rect() # get the rectangle
        self.width,self.height=self.background_size # the width and height will follow the size of the image
    def draw(self,screen,x,y): #define draw
        screen.blit(self.background,(x,y))  #call the background image so it will appear in the game

class Bullet(Sprite):   # class bullet inheriting the sprite
    def __init__(self,screen, startx, starty):  #Constructor for the bullet
        Sprite. __init__(self)  # super class Sprite
        self.startx = startx    # initiate start x
        self.starty = starty    # initiate start y

        self.speedx = 20        # set the speed of the bullet is 20

        self.image = pygame.image.load("bullets.png")   # loading the bullet image
        self.image = pygame.transform.scale(self.image,(40,40)) # setting the size of the bullet
        self.rect=self.image.get_rect() # get rectangle for the image
        self.rect.left = startx # get the rectleft = start x
        self.rect.top = starty  # get the recttop = start y
        self.rect.center = (startx,starty)  # set the rect center so it will be in the center
        self.screen = screen    # initiate screen
    def movement(self):
        #self.screen.blit(self.image,[self.startx,self.starty])
        self.rect.left += self.speedx       # to add the movement speed for the bullets

class Asteroid(Sprite):         # class asteroid inheriting sprite
    """initialize the Asteroid"""
    def __init__(self, screen, width, height, speedx, startx, starty):  #Constructor for the asteroid
        Sprite.__init__(self)   # super class Sprite
        self.startx = startx    # initiate startx
        self.starty = starty    # initiate start y

        self.speedx = speedx    # initiate speed x

        self.image = pygame.image.load("meteor.png")    # load the meteor image
        self.image = pygame.transform.scale(self.image, (width, height))    # set the size of the image
        self.rect = self.image.get_rect()   # get rectangle for the image
        self.rect.left = startx # set the rectleft = startx
        self.rect.top = starty  # set the recttop = start y
        self.screen = screen    # initiate screen

    def movement(self): # initiate movement
        """method to move the Asteoid"""
        self.rect.left -= self.speedx   # set the movement of the asteroid as it is going left


class Button(Sprite):   # class Button inheriting sprite
    """initialize the button"""
    def __init__(self,image):       # Constructor and put the image
        Sprite. __init__(self)      # super class for sprite
        self.button=pygame.image.load(image)    # load the button image
        self.button=pygame.transform.scale(self.button,(300,150))   # set the size of all the buttons (Start, Return, QUit

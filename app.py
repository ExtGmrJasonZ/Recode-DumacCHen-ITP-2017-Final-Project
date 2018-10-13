from pygame import *     #from pygame we import *
import menu             #we imput menu
import random           #we input random to modify random

from classes import *   #we import the classes file to this file with *




def run_game():          # function for running the game
    """game play interface"""
    screen = pygame.display.set_mode((1000, 1000))    # the code for running the game
    display.set_caption("Jet mission")      # setting the title for the game


    scores = 0              # set the original score to 0
    theClock = pygame.time.Clock()  # create an object to track time
    bg_image = Star_bg("star.gif")      # To the star picture to be the background in the game

    #coordinate of moving background
    x = 0                           # coordinate start from x = 0
    y = 0                           # coordinate start from y = 0
    x1 = bg_image.width
    y1 = 0

    pygame.init()           # Initialize the pygame modules


    #creating a jet
    jet1 = Jet(screen)      #Creating the object jet1 from the class Jet
    Jet_sprites = Group(jet1)   #creating the group

    #create asteroid object group
    asteroid_group = Group()

    #create bullets object Group
    bullets = Group()



    Fps = 200        # for setting the fps of the game
    asteroid_timer = pygame.time.get_ticks()    # get the time for the asteroid_timer
    while True:         # while the condition is true (Looping)
        theClock.tick(Fps)  # set ups how often the while loop should update each self
        Fps += 0.01#game phase goes faster after every frame

        """background move"""

        x -= 5
        x1 -= 5
        bg_image.draw(screen,x,y)
        bg_image.draw(screen,x1, y1)
        if x < -bg_image.width:
            x = 0
        if x1 < 0:                      # this will make spawn the asteroids from the right
            x1 = bg_image.width

        # create score board
        font=pygame.font.SysFont("Times New Romans",36)     # create an object for input the score in 36 fontsize
        score_board=font.render("score:"+str(scores),True,(255,255,255))    # Object for the score to update itself in white color
        # update refered to the word's method
        screen.blit(score_board,(10,550))



        Jet_sprites.draw(screen)        # put the jest inside the screen game

        bullets.draw(screen)            # put the bullets inside the screen game

        asteroid_group.draw(screen)     # put the group of asteroids in the screen game
        display.update()#update jet and screen view

        event.get()
        """moving the jet according to key pressed"""

        key = pygame.key.get_pressed()  # Make an object for inputing the hotkey we press when we play the game
        if key[K_LEFT] and jet1.rect.x>0: # if you press the left key and the jet is not in the most left screen
            jet1.moveleft() # then you can press left

        if key[K_RIGHT] and jet1.rect.x<=700:   # If you press right key before it reaches the most right screen
            jet1.moveright()  # then you can press right

        if key[K_DOWN] and jet1.rect.y<=500:    # if you press down key before it  reaches the most bottom of the screen
            jet1.movedown() # then you can press down

        if key[K_UP] and jet1.rect.y>0:     #if you press up before it reaches the upper screen
            jet1.moveup()   # then you can press up

        if key[K_SPACE] and len(bullets) <= jet1.firerates+(scores/4000):   # if you press space and the length of bullets fired will not be greater than the fire rate of the jet and score + 4000
            bullet = Bullet(screen, jet1.rect.x+50, jet1.rect.y+42) # object bullet and set the bullet spawn place
            bullets.add(bullet)     # add the bullet spawn place to the bullets
            pygame.mixer.music.load("LaserBlast.wav")   #add sound evertime you shoot the bullet
            pygame.mixer.music.play()   # play the sound effect

        if key[K_ESCAPE]:   # if I press the escape key
            menu.menu_screen(Button,run_game)   # it will go the main menu screen and call the button class and run_game function so you can play the game again.

        if key[K_p]:    # if I press the p key
            menu.pause_menu(Button,run_game)    #iy will pause the game


        """generate asteroid randomly"""    #if the asteroid timer is bigger or equal to 200
        if pygame.time.get_ticks() - asteroid_timer >= 200:
            asteroid = Asteroid(screen, 50, 50, random.randint(1,4)*6, 800, (random.randint(1,28) * 20)) # make object asteroid and set the spawn place which is random by using the mothod random.randint
            asteroid_group.add(asteroid)    #add asteroids to the group
            asteroid_timer = pygame.time.get_ticks()    # get the time in the asteroid timer

        """update the movement of asteroid"""
        for asteroid in asteroid_group: # for looping in the condition the asteroid is in the asteroid group
            asteroid.movement() # movement
            if asteroid.rect.right <= 0:    # if the asteroid goes beyond the left screen
                asteroid_group.remove(asteroid) #remove after screen
            if groupcollide(Jet_sprites,asteroid_group,dokilla=True,dokillb=True):#collition check
                menu.lose_menu(Button,run_game,scores)  #if the asteroid touches the jet, the game will go to the lose menu and it will call the Buton class, run_game function so you can either restart or quit the game

        """update bullet movement on screen"""
        for bullet in bullets:  # for looping for bullet from bullet class
            bullet.movement()   # getting the movement for bullet
            if bullet.rect.left > 800:  # if the bullet goes beyond the right screen, the bullet will be removed
                bullets.remove(bullet)
            if groupcollide(bullets,asteroid_group,dokilla=True,dokillb=True):      # checking if the bullet hit the asteroids
                scores += 100       # the score will be up by 100

menu.menu_screen(Button,run_game)   # going to the menu screen which we call the Button class and the run_game function to run the game



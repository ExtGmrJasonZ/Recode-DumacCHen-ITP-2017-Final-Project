from pygame import *        # import * from pygame
import sys                  # import sys
import pygame               # import pygame

def menu_screen(Button,run_game):   # define menu screen inheriting the button class and run_game function
    """make the screen for menu"""
    display.set_caption("Jet Mission")  # set the caption Jet mission
    screen = pygame.display.set_mode((800, 600))    #set the resolution width and height
    #object button for quit and start
    start_button = Button("New Piskel.png") # load the image and make it as the start button
    quit_button = Button("quit button.png") # load the image and make it as the quit butto
    #image for the menu's backgound
    bg_image=pygame.image.load("asteroid_wall.jpg") # load the image as the background image
    bg_image=pygame.transform.scale(bg_image, (800, 600))   # set the size for the background


    pygame.init()   # initiate pygame

    while True:     # while the condition is true
        rect_start= draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))  #rectstart which sets it to black and also set the size
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))  #rectquit which sets it to black and also set the size
        screen.blit(bg_image,(0,0)) #call the background image 0, 0

        screen.blit(start_button.button,(250,200))  #call the start button image and set the sze
        screen.blit(quit_button.button,(250,300))   # call the quit button image and set the size

        ev=event.wait() # pause the program for an amount of time as ev variable

        if ev.type == MOUSEBUTTONDOWN:  # Make loop for clicking mouse button
            if rect_start.collidepoint(mouse.get_pos()):    # if click on the start button
                run_game()  # run the game
            if rect_quit.collidepoint(mouse.get_pos()): # if click on the quit button
                sys.exit()  # exit the game

        if ev.type == QUIT:
            sys.exit()  # exit the game

        display.update()    # display the update after the button you choose

def pause_menu(Button,run_game):    # define pause menu from button class and run _game function
    """pause_menu"""
    #make the screen display
    display.set_caption("Jet Mission")  #set caption
    screen = pygame.display.set_mode((800, 600))    # set the size

    # object button for quit and start
    start_button = Button("quit button.png")    # loading the image
    return_button = Button("pause button.png")  # loading the image

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg")   # load the image
    bg_image = pygame.transform.scale(bg_image, (800, 600)) # set the size of the image


    pygame.init()       # initiate pygame
    paused=True #pause flag
    while paused: # while looping for the condition the game is paused
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))     # draw the start button black colored
        rect_return = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))    # draw the return button black colored
        screen.blit(bg_image, (0, 0))       #call the background image 0, 0

        screen.blit(start_button.button, (250, 200))    # call tthe start button to the screen 250, 300
        screen.blit(return_button.button, (250, 300))   # call the start button to the screen 250, 300

        ev = event.wait()   # pause the program as ev variable

        if ev.type == MOUSEBUTTONDOWN:     # if you click the mouse button
            if rect_start.collidepoint(mouse.get_pos()):    # quit button
                menu_screen(Button,run_game)    # will go back to the menu screen and call the button class and run game function
            if rect_return.collidepoint(mouse.get_pos()):   # return button
                paused = False #flag become  False  # continue game

        if ev.type == QUIT: #if quit the game
            sys.exit()  #exit the game

        display.update()    # update the display

def lose_menu(Button,run_game,score):       # define the lose menu from the button class and the run game function and score
    """make the screen for menu"""
    display.set_caption("Jet Mission")
    screen = pygame.display.set_mode((800, 600))
    font=pygame.font.SysFont("times new roman",100)
    text=font.render("Replay?",True,(255,255,255))
    score_text=font.render("score:"+str(score),True,(255,255,255))

    # object button for quit and start
    start_button = Button("New Piskel.png")
    quit_button = Button("quit button.png")

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg")
    bg_image = pygame.transform.scale(bg_image, (800, 600))

    pygame.init()

    while True:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bg_image, (0, 0))
        screen.blit(text,(200,10))
        screen.blit(start_button.button, (250, 200))
        screen.blit(quit_button.button, (250, 300))
        screen.blit(score_text,(200,400))

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()

        if ev.type == QUIT:
            sys.exit()

        display.update()

# More or less the same with the class before

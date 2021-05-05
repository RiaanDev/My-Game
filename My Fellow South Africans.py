# In this example.py you will learn how to make a very simple game using the pygame library.
# One of the best ways of learning to program is by writing games.
# Pygame is a collection of modules in one package.
# You will need to install pygame.
# To do so:
# 1) open the command line interface on your computer,
# 2) cd to the directory that this task is located in,
# 3) follow the instructions here: https://www.pygame.org/wiki/GettingStarted
# 4) if you need help using pip, see here: https://projects.raspberrypi.org/en/projects/using-pip-on-windows

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

pygame.display.set_caption("My Fellow South Africans")
# This creates the player and gives it the image found in this folder  
player = pygame.image.load("hero.jpg")  # The player

enemy = pygame.image.load("corona.jpg") # The enemy 
enemy2 = pygame.image.load("corona.jpg")# Another enemy
enemy3 = pygame.image.load("corona.jpg")# Another enemy

prize = pygame.image.load("cure.jpg")   # A prize


#This is the size of the player, prize and enemys 
player = pygame.transform.scale(player, (90, 90))

prize = pygame.transform.scale(prize, (60,100))

enemy = pygame.transform.scale(enemy, (80, 80))
enemy2 = pygame.transform.scale(enemy2, (80, 80))
enemy3 = pygame.transform.scale(enemy3, (80, 80))


# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).
image_height = player.get_height()
image_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()


# Store the positions of the player and prize as variables so that you can change them later. 
playerXPosition = 100
playerYPosition = 50

prizeXPosition = 700
prizeYPosition = 300


# Make the enemys start off screen and at a random y position.
enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)

enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)

# This checks if the up or down, left or right key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
keyLeft = False
keyRight = False
keyUp= False
keyDown = False


# This is the main game loop.
while 1: # This is a looping structure that will loop the indented code until you tell it to stop. 

    screen.fill(0)          # Clears the screen.

    screen.blit(player, (playerXPosition, playerYPosition)) # This draws the player image to the screen at the postion specfied.

    screen.blit(enemy, (enemyXPosition, enemyYPosition))    # This draws the enemys to the screen at the position specfied.
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))

    screen.blit(prize, (prizeXPosition, prizeYPosition))    # This draws the prize to the screen at the position specfied
    
    pygame.display.flip()   # This updates the screen. 


    # This loops through events in the game.
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
           

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    keys = pygame.key.get_pressed()
    if keys [pygame. K_UP]:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1 # This moves the player along with the x or y positions

    if keys [pygame. K_DOWN]:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1 # This moves the player along with the x or y positions


    if keys [pygame. K_LEFT]:
        if playerXPosition > 0 : 
            playerXPosition -= 1

    if keys [pygame. K_RIGHT]:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1
    

    # Check for collision of the enemy with the player.

    # Bounding box for the player:
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemys:
    # in effect making the box stay around the enemys image.
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    # Bounding box for the prize:
    # in effect making the box stay around the prize image.
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    
    # Test collision of the boxes:
    if playerBox.colliderect(enemyBox):
        print("You lose!")# Display losing status to the user
        pygame.quit()# Quite game and exit window
        exit(0)

    if playerBox.colliderect(enemy2Box):
        print("You lose!") 
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
        print("You lose!")
        pygame.quit()
        exit(0)
    
    if playerBox.colliderect(prizeBox):
        print("You Win!")# Display winning status to the user  
        pygame.quit()# Quite game and exit window
        exit(0)


    # If the enemy is off the screen the user wins the game:
    if enemyXPosition < 0 - enemy_width:
        print("You win!")# Display wining status to the user: 
        pygame.quit()# Quite game and exit window: 
        exit(0)

    if enemy2XPosition < 0 - enemy2_width:
        print("You win!") 
        pygame.quit()
        exit(0)

    if enemy3XPosition < 0 - enemy3_width:
        print("You win!")
        pygame.quit()
        exit(0)
    
 
    # Make enemy approach the player.
    enemyXPosition -= 0.15
    enemy2XPosition -= 0.15
    enemy3XPosition -= 0.15
    
  

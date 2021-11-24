# Import pygame and time modules
import pygame
# Initialize pygame
pygame.init() 

screen = pygame.display.set_mode((550, 400))
pygame.display.set_caption("City Runner Game")

# Create image loading function here, name it as "image_load"





# Create a function to display coins here, name it as "coin_display"





 
bgImg = image_load("background.png",800,400)
char = image_load("character.png",40,90)
coin = image_load("coin.png",50,50)
coins = [coin for i in range(6)]

# All variables required to track background, character and coin positions are defined here
bgx = 0
charx = 10
chary = 210
x = 0

# Game loop
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            carryOn = False  
        # Check if right arrow key is pressed and move the character and background

        


        # If character goes beyond 500 coordinate along x-axis and reset position of character and background





    # Display the background, character and coins here



    
    pygame.display.flip()
pygame.quit()
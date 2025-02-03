# pygame import
import pygame
pygame.init()

# Opens pong window
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Pong")

# Ball variables
bx = 350  # x position
by = 250  # y position
bVx = 5   # x velocity
bVy = 5   # y velocity
p2Score = 0  # P2 Score
p1Score = 0  # P1 Score
# Game loop
doExit = False

# Clock updates screen
clock = pygame.time.Clock()

# Variables to hold paddle position
p2x = 350
p2y = 400

# Game loop
while not doExit:
    clock.tick(60)  # FPS
    
    for event in pygame.event.get():  # Checks if user did something
        if event.type == pygame.QUIT:  # Checks if user clicked close
            doExit = True  # Flag that we are done so we exit game loop
            
    # Game logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and p2x > 0:
        p2x -= 5
    if keys[pygame.K_RIGHT] and p2x < 600:  # Prevent paddle from going off screen
        p2x += 5
    
    # Ball Movement
    bx += bVx
    by += bVy
    
    # Reflect ball off the side walls
    if bx < 0 or bx + 20 > 700:  
        bVx *= -1

    # Reflect ball off the top and bottom walls
    if by < 0 or by > 490:  
        bVy *= -1

    # Ball paddle reflection
    if bx + 10 > p2x and by + 10 > p2y and bx < p2x + 100:
        bVy *=-1

    # Render section
    screen.fill((191, 19, 148))  # Wipes screen Pink
    pygame.draw.rect(screen, (255, 255, 255), (p2x, p2y, 100, 20), 1)  # Right paddle
    pygame.draw.circle(screen, (255, 255, 255), (bx, by), 10)  # Ball
    
    # Displays Scores
    font = pygame.font.Font(None, 74)  # Use default font
    text = font.render(str(p2Score), 1, (255, 255, 255))
    screen.blit(text, (300, 10))
     
     
    # Update screen
    pygame.display.flip()
            
# END GAME LOOP
pygame.quit()  # Closes pygame window when done





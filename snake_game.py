import pygame  # Import the pygame library
import time
import random  # Import the random library for generating random positions for the food

# Initialize pygame
pygame.init()

# Define colors using RGB tuples
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255, 165, 0)
purple = (128, 0, 128)
pink = (255, 192, 203)
brown = (165, 42, 42)
gray = (128, 128, 128)
gold = (255, 215, 0)
silver = (192, 192, 192)
maroon = (128, 0, 0)
olive = (128, 128, 0)
light_blue = (173, 216, 230)
dark_blue = (0, 0, 139)

# Set the dimensions of the game window
display_width = 800
display_height = 600

# Create the game display/window
game_display = pygame.display.set_mode((display_width, display_height))
# Set the title of the game window
pygame.display.set_caption('Snake Game')

# Set up the game clock
clock = pygame.time.Clock()
# Define the size of each block (the snake and food)
snake_block = 10
# Set the initial speed of the snake
snake_speed = 15

# Set up the font for displaying text
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    """
    Function to display the current score on the screen.
    """
    value = score_font.render("Your Score: " + str(score), True, black)
    game_display.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    """
    Function to draw the snake on the screen.
    """
    for x in snake_list:
        pygame.draw.rect(game_display, dark_blue, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """
    Function to display a message on the screen.
    """
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [display_width / 6, display_height / 3])

def game_loop():
    """
    Main game loop.
    """
    game_over = False  # Flag to indicate if the game is over
    game_close = False  # Flag to indicate if the player has lost

    # Initial position of the snake
    x1 = display_width / 2
    y1 = display_height / 2

    # Variables to keep track of the snake's movement
    x1_change = 0
    y1_change = 0

    # List to keep track of the snake's body
    snake_list = []
    # Initial length of the snake
    length_of_snake = 1

    # Generate initial position for the food
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            # Display game over message and options to quit or restart
            game_display.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", purple)
            your_score(length_of_snake - 1)
            pygame.display.update()

            # Event loop to handle key presses for quitting or restarting the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event loop to handle key presses for moving the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if the snake hits the boundaries
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(silver)  # Fill the background with silver color
        pygame.draw.rect(game_display, maroon, [foodx, foody, snake_block, snake_block])  # Draw the food
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake runs into itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake and display the score
        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)  # Control the speed of the snake

    pygame.quit()  # Quit pygame
    quit()  # Exit the program

game_loop()  # Start the game

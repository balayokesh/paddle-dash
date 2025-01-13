import pygame
import random

def custom_random_int(start, end):
    if start > end:
        raise ValueError("Start must be less than or equal to End.")
    # Scale the random float to the desired range
    random_float = random.random()  # Random float between 0 and 1
    scaled_value = start + int(random_float * (end - start + 1))
    return scaled_value

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Paddle properties
paddle_width, paddle_height = 100, 20
# paddle_x = (WIDTH - paddle_width) // 2
paddle_x = 200
paddle_y = HEIGHT - 100
paddle_speed = 10

# Ball properties
ball_radius = 15
ball_x = custom_random_int(ball_radius, WIDTH - ball_radius)
ball_y = 0
ball_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Move the ball
    ball_y += ball_speed

    # Check if the ball hits the paddle
    if paddle_y < ball_y + ball_radius < paddle_y + paddle_height and paddle_x < ball_x < paddle_x + paddle_width:
        score += 1
        ball_x = custom_random_int(ball_radius, WIDTH - ball_radius)
        ball_y = 0

    # Reset ball if it falls past the paddle
    if ball_y > HEIGHT:
        ball_x = custom_random_int(ball_radius, WIDTH - ball_radius)
        ball_y = 0

    # Draw the paddle
    pygame.draw.rect(screen, BLUE,
                     (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Draw the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()

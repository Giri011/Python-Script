import pygame
import random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parkour Rush")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY = (135, 206, 235)
DARK_GRAY = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.SysFont("arial", 28)
title_font = pygame.font.SysFont("impact", 50)

# Player settings
player_width, player_height = 40, 60
player_x = 100
player_y = HEIGHT - 150
player_vel_y = 0
jumping = False
gravity = 0.8
jump_power = -14

# Platform settings
platforms = []
platform_width = 120
scroll_speed = 3
gap_range = (150, 250)
height_variation = (100, 250)

# Game variables
score = 0
run = True
clock = pygame.time.Clock()
game_over = False
win_game = False

def draw_text(text, font, color, surface, x, y):
    render = font.render(text, True, color)
    surface.blit(render, (x, y))

# Generate platforms
def generate_platforms():
    global platforms
    platforms = []

    # First platform directly under player
    start_platform = pygame.Rect(0, HEIGHT - 150 + player_height, platform_width, 20)
    platforms.append(start_platform)

    # Generate rest of the platforms
    x = start_platform.x + platform_width + random.randint(*gap_range)
    while x < 2000:
        height = HEIGHT - random.randint(*height_variation)
        platforms.append(pygame.Rect(x, height, platform_width, 20))
        x += platform_width + random.randint(*gap_range)

generate_platforms()

def draw_window():
    win.fill(SKY)

    # Draw platforms
    for plat in platforms:
        pygame.draw.rect(win, DARK_GRAY, plat)

    # Draw player
    pygame.draw.rect(win, RED, (player_x, player_y, player_width, player_height))

    draw_text(f"Score: {score}", font, BLACK, win, 10, 10)
    pygame.display.update()

def reset_game():
    global player_y, player_vel_y, jumping, score, game_over, win_game, platforms
    player_y = HEIGHT - 150
    player_vel_y = 0
    jumping = False
    score = 0
    game_over = False
    win_game = False
    platforms.clear()
    generate_platforms()

# Game loop
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if not game_over and not win_game:
        # Jumping
        if keys[pygame.K_SPACE] and not jumping:
            player_vel_y = jump_power
            jumping = True

        # Gravity
        player_vel_y += gravity
        player_y += player_vel_y

        # Collision with platforms
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        on_ground = False
        for plat in platforms:
            plat.x -= scroll_speed  # Move platform to the left
            if player_rect.colliderect(plat) and player_vel_y >= 0:
                player_y = plat.y - player_height
                player_vel_y = 0
                jumping = False
                on_ground = True

        # Remove off-screen platforms and check win
        if platforms and platforms[0].x + platform_width < 0:
            platforms.pop(0)
            score += 1
            if not platforms:
                win_game = True

        # Fall off
        if player_y > HEIGHT:
            game_over = True

        draw_window()

    else:
        win.fill(SKY)
        if game_over:
            draw_text("GAME OVER", title_font, RED, win, WIDTH // 2 - 150, HEIGHT // 2 - 50)
        elif win_game:
            draw_text("YOU WIN!", title_font, GREEN, win, WIDTH // 2 - 130, HEIGHT // 2 - 50)
        draw_text(f"Final Score: {score}", font, BLACK, win, WIDTH // 2 - 80, HEIGHT // 2 + 20)
        draw_text("Press R to Restart or Q to Quit", font, BLACK, win, WIDTH // 2 - 160, HEIGHT // 2 + 70)
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            reset_game()
        elif keys[pygame.K_q]:
            run = False

pygame.quit()

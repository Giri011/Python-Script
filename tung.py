import pygame
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 600, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Shooter Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont("arial", 28)
title_font = pygame.font.SysFont("impact", 50)

# Game variables
player_size = 50
player_vel = 5
bullet_vel = 7
enemy_size = 40
enemy_vel = 3
spawn_delay = 40

clock = pygame.time.Clock()


def draw_text(text, font, color, surface, x, y):
    render = font.render(text, True, color)
    surface.blit(render, (x, y))


def main_menu():
    in_menu = True
    while in_menu:
        win.fill(WHITE)
        draw_text("2D SHOOTER", title_font, BLACK, win, WIDTH // 2 - 150, HEIGHT // 2 - 100)
        draw_text("Press ENTER to Start", font, BLACK, win, WIDTH // 2 - 120, HEIGHT // 2)
        draw_text("Press Q to Quit", font, BLACK, win, WIDTH // 2 - 100, HEIGHT // 2 + 40)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            in_menu = False
        elif keys[pygame.K_q]:
            pygame.quit()
            exit()


def game_loop():
    # Initialize per-game variables
    player_x = WIDTH // 2
    player_y = HEIGHT - player_size - 10
    health = 5
    score = 0
    bullets = []
    enemies = []
    frame_count = 0
    run = True

    def draw_window():
        win.fill(WHITE)
        pygame.draw.rect(win, GREEN, (player_x, player_y, player_size, player_size))

        for bx, by in bullets:
            pygame.draw.rect(win, BLUE, (bx, by, 5, 10))
        for ex, ey in enemies:
            pygame.draw.rect(win, RED, (ex, ey, enemy_size, enemy_size))

        draw_text(f"Score: {score}", font, BLACK, win, 10, 10)
        draw_text(f"Health: {health}", font, BLACK, win, WIDTH - 150, 10)

        pygame.display.update()

    while run:
        clock.tick(60)
        frame_count += 1

        # Spawn enemies
        if frame_count % spawn_delay == 0:
            ex = random.randint(0, WIDTH - enemy_size)
            enemies.append([ex, 0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_x - player_vel > 0:
            player_x -= player_vel
        if keys[pygame.K_d] and player_x + player_vel < WIDTH - player_size:
            player_x += player_vel
        if keys[pygame.K_w] and player_y - player_vel > 0:
            player_y -= player_vel
        if keys[pygame.K_s] and player_y + player_vel < HEIGHT - player_size:
            player_y += player_vel
        if keys[pygame.K_SPACE]:
            bullets.append([player_x + player_size // 2 - 2, player_y])

        # Update bullets
        bullets = [[x, y - bullet_vel] for x, y in bullets if y > 0]

        # Update enemies
        new_enemies = []
        for ex, ey in enemies:
            ey += enemy_vel
            if ey > HEIGHT:
                health -= 1
            else:
                new_enemies.append([ex, ey])
        enemies = new_enemies

        # Collision
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                bx, by = bullet
                ex, ey = enemy
                if (ex < bx < ex + enemy_size) and (ey < by < ey + enemy_size):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break

        if health <= 0:
            win.fill(WHITE)
            draw_text("GAME OVER", title_font, RED, win, WIDTH // 2 - 130, HEIGHT // 2 - 30)
            draw_text(f"Final Score: {score}", font, BLACK, win, WIDTH // 2 - 100, HEIGHT // 2 + 40)
            pygame.display.update()
            pygame.time.wait(3000)
            run = False
            main_menu()

        draw_window()


# Run the game
main_menu()
game_loop()
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Bullet settings
bullet_width = 5
bullet_height = 10
bullet_speed = 10
bullets = []

# Target settings
target_width = 50
target_height = 50
target_speed = 2
targets = []

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot a bullet
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append(pygame.Rect(bullet_x, bullet_y,
                               bullet_width, bullet_height))

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Spawn targets
    if len(targets) < 5:
        target_x = random.randint(0, WIDTH - target_width)
        target_y = random.randint(-100, -target_height)
        targets.append(pygame.Rect(target_x, target_y,
                       target_width, target_height))

    # Move targets
    for target in targets:
        target.y += target_speed
        if target.y > HEIGHT:
            targets.remove(target)

    # Collision detection
    for bullet in bullets:
        for target in targets:
            if bullet.colliderect(target):
                bullets.remove(bullet)
                targets.remove(target)

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y,
                     player_width, player_height))
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    for target in targets:
        pygame.draw.rect(screen, WHITE, target)
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

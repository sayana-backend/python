import pygame
import time
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True
direction = "RIGHT"
score = 0


def game_over():
    font = pygame.font.SysFont("times new roman", 50)
    game_over_surface = font.render(f"Ваш счёт: {score}", True, RED)
    screen.fill(BLACK)
    screen.blit(game_over_surface, (WIDTH // 6, HEIGHT // 3))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not direction == "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and not direction == "UP":
                direction = "DOWN"
            if event.key == pygame.K_LEFT and not direction == "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and not direction == "LEFT":
                direction = "RIGHT"

    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
    food_spawn = True

    if snake_pos[0] < 0 or snake_pos[0] > WIDTH - 10 or snake_pos[1] < 0 or snake_pos[1] > HEIGHT - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    pygame.display.flip()
    clock.tick(15)

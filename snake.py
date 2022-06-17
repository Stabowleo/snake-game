import random
import pygame
import json
from pygame.locals import *
pygame.init()
pygame.font.init()

green = (0, 255, 0)
red = (255, 0, 0)


class Snake:

    def __init__(self) -> None:
        self.size = 40
        self.speed = 10   
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2
        self.x_change = 0
        self.y_change = 0
        self.head = [self.x, self.y]
        self.snake_list = [self.head]
        self.length = 1
        self.colour = "black"

    def draw_snake(self):

        random_colour = (random.randrange(100, 255), random.randrange(0, 255), random.randrange(0, 255))

        chosen_colour = random_colour if self.colour == "random" else green

        for x in self.snake_list:
            pygame.draw.rect(screen, chosen_colour, [x[0], x[1], self.size, self.size])
            


class Food:

    def __init__(self) -> None:
        self.x = round(random.randrange(0, screen.get_width() - Snake().size) / 40) * 40
        self.y = round(random.randrange(0, screen.get_height() - Snake().size) / 40) * 40

    def draw_food(self):
        pygame.draw.rect(screen, red, [self.x, self.y, 40, 40])

    def move(self):
        self.x = round(random.randrange(0, screen.get_width() - Snake().size) / 40) * 40
        self.y = round(random.randrange(0, screen.get_height() - Snake().size) / 40) * 40


clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Snake Game")
pygame.display.set_icon(pygame.image.load("art/SnakeHead.png"))

score = 0


def load_scores():
    with open("saves/topscores.json") as file:
        data = json.load(file)
        file.close()
    return [i for i in data]


def save_score(score):

    
    scores = load_scores()
    scores.append(score)

    with open("saves/topscores.json", "w") as file:
        json.dump(scores, file, indent=4)
        file.close()


def game_close():
    global score

    save_score(score)
    topscore = max(load_scores())
    scorefont = pygame.font.SysFont("comicsansms", 35)
    text = scorefont.render(f"Score: {score}", True, red)
    highscore = scorefont.render(f"Highscore: {topscore}", True, red)
    text2 = scorefont.render(f"Exit - ESC, Restart - ENTER", True, red)
    gameover = pygame.image.load("art/GameOver.png")
    screen.fill((0, 0, 0))
    screen.blit(gameover, (50, screen.get_height() - 600))
    screen.blit(text, (50, screen.get_height() - 435))
    screen.blit(highscore, (50, screen.get_height() - 370))
    screen.blit(text2, (80, screen.get_height() - 60))
    while True: 
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_RETURN:
                    score = 0
                    main()


def main():
    global score

    snake = Snake()
    food = Food()
    game_over = False
    snake.x = screen.get_width() / 2
    snake.y = screen.get_height() / 2

    while not game_over:


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake.x_change = 0
                    snake.y_change = -snake.size
                elif event.key == pygame.K_a:
                    snake.x_change = -snake.size
                    snake.y_change = 0
                elif event.key == pygame.K_s:
                    snake.x_change = 0
                    snake.y_change = snake.size
                elif event.key == pygame.K_d:
                    snake.x_change = snake.size
                    snake.y_change = 0
                elif event.key == pygame.K_RETURN:
                    snake.colour = "random" if snake.colour == "black" else "black"

        if snake.x >= screen.get_width() or snake.x < 0 or snake.y >= screen.get_height() or snake.y < 0:
            game_close()

        snake.x += snake.x_change
        snake.y += snake.y_change
        screen.fill((0, 0, 0))
        food.draw_food()
        snake.head = [snake.x, snake.y]
        snake.snake_list.append(snake.head)
        
        if len(snake.snake_list) > snake.length:
            del snake.snake_list[0]
        

        for x in snake.snake_list[:-1]:
            if x == snake.head:
                game_close()

        
        snake.draw_snake()
        pygame.display.update()


        if snake.x == food.x and snake.y == food.y:
            food.move()
            snake.length += 1
            score += 1

        clock.tick(snake.speed)


if __name__ == "__main__":
    main()
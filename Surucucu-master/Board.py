# Importing statements
from Food import Food
from random import randint
import pygame
from Cell import *
from Snake import Snake

# Autoria de Alan B. vital & Gustavo Hamburg


class Board:
    def __init__(self):
        # overhaul size of the screen by 16x16 pixels as 1 unit
        self.size = {'columns': 45, 'rows': 30}
        # time in ticks between each snake move
        self.snakepace = 6
        # snake state, alive = True, dead = False
        self.snakeState = True
        # game score
        self.score = 0
        # internal cool down to limit player movement
        self.cd = [9, 9, False]
        # screen size in pixels
        self.psize = {'width': 720, 'height': 480}
        # fps control
        self.clock = pygame.time.Clock()
        # time in ticks for internal control
        self.pace = 0
        # spawning snake and assigning to a variable
        self.snake = Snake(352, 240)
        # spawning food and assigning to a variable
        self.food = Food(randint(1, self.size['columns'] - 1) * 16, randint(1, self.size['rows'] - 1) * 16)
        # board
        self.rows = []
        self.screen = pygame.display.set_mode((self.psize['width'], self.psize['height']))
        # rows
        for i in range(0, self.size['rows']):
            self.row = []
            # columns
            for j in range(0, self.size['columns']):
                if i == 0:
                    if j == 0:
                        self.row.append(LTCell(j * 16, i * 16))
                    elif j == self.size['columns'] - 1:
                        self.row.append(TRCell(j * 16, i * 16))
                    else:
                        self.row.append(TCell(j * 16, i * 16))
                elif i == self.size['rows'] - 1:
                    if j == 0:
                        self.row.append(BLCell(j * 16, i * 16))
                    elif j == self.size['columns'] - 1:
                        self.row.append(RBCell(j * 16, i * 16))
                    else:
                        self.row.append(BCell(j * 16, i * 16))
                elif i > 0 and j == 0:
                    self.row.append(LCell(j * 16, i * 16))
                elif i > 0 and j == self.size['columns'] - 1:
                    self.row.append(RCell(j * 16, i * 16))
                else:
                    self.row.append(Cell(j * 16, i * 16))
            self.rows.append(self.row)

    # increment in pace
    def pace_increment(self):
        self.pace += 1

    # draw background in board's screen variable
    def draw_background(self):
        for i in range(0, self.size['rows']):
            for j in range(0, self.size['columns']):
                self.screen.blit(self.rows[i][j].cell, self.rows[i][j].cellRect)
        pygame.display.flip()

    # spawns food in random place
    def spawn_new_food(self):
        self.food = Food(randint(1, self.size['columns'] - 1) * 16, randint(1, self.size['rows'] - 1) * 16)

    # respawn food
    def kill_food(self, snake: Snake):
        def overlap():
            if self.food.coordinates() == snake.headRect:
                return True
            for body_rect in snake.bodyRect:
                if self.food.coordinates() == body_rect:
                    return True
            if self.food.coordinates() == snake.tailRect:
                return True
            return False
        while True:
            self.spawn_new_food()
            if not overlap():
                break

    # draws food in board's screen
    def draw_food(self):
        self.screen.blit(self.food.sprite, self.food.spriteRect)

    # kills the snake
    def kill_snake(self):
        self.snakeState = False

    # draws snake in class's screen
    def draw_snake(self):
        self.screen.blit(self.snake.headSprite, self.snake.headRect)
        for i in range(0, self.snake.bodyLength):
            self.screen.blit(self.snake.bodySprite[i], self.snake.bodyRect[i])
        self.screen.blit(self.snake.tailSprite, self.snake.tailRect)

    # check if snake is in contact with itself or the wall
    def snake_kill_check(self):
        def snake_wall_check():
            if self.snake.headRect.left < 0 or self.snake.headRect.right > self.psize['width']:
                self.kill_snake()
                return True
            if self.snake.headRect.top < 0 or self.snake.headRect.bottom > self.psize['height']:
                self.kill_snake()
                return True

        def snake_body_check():
            try:
                for i in range(1, self.snake.bodyLength):
                    if self.snake.headRect == self.snake.bodyRect[i]:
                        self.kill_snake()
                        return True
                    if self.snake.headRect == self.snake.tailRect:
                        self.kill_snake()
                        return True
            except IndexError:
                pass
        return True if snake_wall_check() or snake_body_check() else False

'''
Na classe Board tem tudo o que diz respeito ao tabuleiro em sí, como destaques temos os atributos principais que são:
-size[tamanho do tabuleiro]
-score[pontuação]
-snake[cobra alocada no tabuleiro]
-food[comida alocada no tabuleiro]
-clock[controle de fps]
-screen[tela onde sera desenhada o tabuleiro]
e de funções:
-snake_kill_check()[checa o estado da cobra e restarta se necessario]
-draw_snake()[desenha a cobra na tela]
-draw_food()[desenha a comida na tela]
-kill_food()["mata" e recria a comida em um lugar diferente]
'''
if __name__ == '__main__':
    pass

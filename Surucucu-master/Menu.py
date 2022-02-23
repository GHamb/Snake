import pygame
from Board import Board
from sys import exit

# Autoria de Alan B. vital & Gustavo Hamburg


class Menu:
    def __init__(self):
        # screen size
        self.size = (720, 480)
        # menu's creen
        self.screen = pygame.display.set_mode(self.size)
        # image speed
        self.speed = [2, 0]
        # background color
        self.background_color = 0, 0, 0
        # image
        self.menu = pygame.image.load("img/jogo menu.png")
        # image rect
        self.menurect = self.menu.get_rect()
        # font for writing on the screen
        pygame.font.init()
        self.font = pygame.font.SysFont('Times New Roman', 30)

    # snake state
    @staticmethod
    def snake_check(board):
        return True if board.snakeState else False

    # runs the game
    def play(self, board: Board):
        while 1:
            # 30 fps
            board.clock.tick(30)

            # key cool down control
            if board.cd[0] >= board.cd[1]:
                board.cd[2] = False
            if board.cd[2] is True:
                board.cd[0] += 1
            # check for snake eating food
            if board.snake.food_check(board.food):
                # if yes
                if board.pace % board.snakepace == 0:
                    # draws background
                    board.draw_background()
                    # moves snake and create new body part
                    board.snake.move_and_grow()
                    board.kill_food(board.snake)
                    board.score += 1
            else:
                # if no
                if board.pace % board.snakepace == 0:
                    # draws background
                    board.draw_background()
                    # moves snake
                    board.snake.move()
                board.draw_food()

            # quit or key press events
            for event in pygame.event.get():
                # exits the game
                if event.type == pygame.QUIT:
                    exit()
                # accelerates snake if correspondent key press while in the same direction of the snake
                if event.type == pygame.KEYDOWN and (
                        event.key == pygame.K_LEFT and board.snake.direction == 'left' or
                        event.key == pygame.K_RIGHT and board.snake.direction == 'right' or
                        event.key == pygame.K_UP and board.snake.direction == 'up' or
                        event.key == pygame.K_DOWN and board.snake.direction == 'down'):
                    board.snakepace = 2
                else:
                    board.snakepace = 6
                # turns the snake
                if event.type == pygame.KEYDOWN and board.cd[0] == board.cd[1]:
                    if event.key == pygame.K_LEFT and board.snake.direction != 'left' \
                            and board.snake.direction != 'right':
                        board.snake.rotate_head('left')

                        board.snake.direction = 'left'
                        board.cd[0] = 0
                        board.cd[2] = True
                    if event.key == pygame.K_RIGHT and board.snake.direction != 'right' \
                            and board.snake.direction != 'left':
                        board.snake.rotate_head('right')
                        board.snake.direction = 'right'
                        board.cd[0] = 0
                        board.cd[2] = True
                    if event.key == pygame.K_UP and board.snake.direction != 'up' and board.snake.direction != 'down':
                        board.snake.rotate_head('up')
                        board.snake.direction = 'up'
                        board.cd[0] = 0
                        board.cd[2] = True
                    if event.key == pygame.K_DOWN and board.snake.direction != 'down' and board.snake.direction != 'up':
                        board.snake.rotate_head('down')
                        board.snake.direction = 'down'
                        board.cd[0] = 0
                        board.cd[2] = True
            # snake kill check for restart
            if board.snake_kill_check():
                self.initial_menu('restart', board.score)
            # draw snake on screen
            board.draw_snake()
            # pace increment
            board.pace_increment()
            pygame.display.flip()

    def initial_menu(self, mode='initial', score=0):
        # initiate screen
        pygame.display.init()
        # screen caption aka title
        pygame.display.set_caption("Surucucu")
        pygame.init()
        # instantiate Board as b1
        b1 = Board()
        if mode == 'initial':
            # in initial state
            textsurface = self.font.render('Pressione para Jogar', False, (35, 142, 35))
        else:
            # in restart state
            textsurface = self.font.render(f'Pressione para Jogar / ultima pontuação: {score}', False, (35, 142, 35))
            b1.cd[0] = 0
            b1.cd[2] = True
        while 1:
            # 210 fps
            b1.clock.tick(210)
            # cool down control
            if b1.cd[0] >= b1.cd[1]:
                b1.cd[2] = False
            if b1.cd[2] is True:
                b1.cd[0] += 1
            for event in pygame.event.get():
                # exits the game
                if event.type == pygame.QUIT:
                    exit()
                # starts the game
                elif event.type == pygame.KEYDOWN and b1.cd[0] == b1.cd[1]:
                    self.play(b1)

            # image movement
            self.menurect = self.menurect.move(self.speed)
            if self.menurect.left < 0 or self.menurect.right > self.size[0]:
                self.speed[0] = -self.speed[0]

            # image draw
            self.screen.fill(self.background_color)
            self.screen.blit(self.menu, self.menurect)
            if mode == 'initial':
                self.screen.blit(textsurface, (self.size[0]/3, 0))
            else:
                self.screen.blit(textsurface, (self.size[0]/5, 0))

            pygame.display.flip()


'''
na classe Menu temos o menu inicial e o de restarte com a pontuação da ultima rodada, assim como a compilação de todo o
 codigo, des das celulas para o tabuleiro a cobra e a comida, tomando conta das interações entre eles. Como destaques
  temos as funções:
  -initial_menu()[sendo o menu inicial do jogo]
  -play()[onde o jogo acontece]
'''

if __name__ == '__main__':
    pass

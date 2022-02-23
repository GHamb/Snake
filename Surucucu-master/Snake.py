import pygame
from Food import *

# Autoria de Alan B. vital & Gustavo Hamburg


# noinspection PyShadowingNames
class Snake:
    def __init__(self, x, y):
        # attributes

        # min length is 3
        self.length = 3

        # angle for rotation control
        self.angle = 90

        # body length
        self.bodyLength = self.length - 2

        # snake speed in pixels
        self.speed = 16

        # snake direction
        self.direction = 'up'

        # head attributes
        self.headSprite = pygame.image.load('img/snake/head.jpg')
        self.headRect = self.headSprite.get_rect().move(x, y)
        self.headPreviewsRect = self.headRect
        self.rotate = []

        # body attributes
        self.bodySprite = []

        for i in range(0, self.bodyLength):
            self.bodySprite.append(pygame.image.load('img/snake/body.jpg'))
        self.bodyRect = []
        for i in range(0, self.bodyLength):
            self.bodyRect.append(self.bodySprite[i].get_rect().move(x, y + (i*16) + self.speed))
        self.bodyPreviewsRect = self.bodyRect[self.bodyLength - 1].move(-self.speed, self.speed)

        # tail attributes
        self.tailSprite = pygame.image.load('img/snake/tail.jpg')
        self.tailRect = self.tailSprite.get_rect().move(self.bodyPreviewsRect.move(self.speed, 0).left,
                                                        self.bodyPreviewsRect.move(self.speed, 0).top)

    # checks for food
    def food_check(self, food: Food):
        return True if self.headRect == food.coordinates() else False

    # updates in Rect
    def update_previews_head_rect(self):
        self.headPreviewsRect = self.headRect

    def update_previews_body_rect(self):
        self.bodyPreviewsRect = self.bodyRect[self.bodyLength - 1]

    # move head
    def move_head(self, coordinates):
        self.headRect = self.headRect.move(coordinates)

    # move body
    def move_body(self):
        for i in range(self.bodyLength - 1, -1, -1):
            if i == 0:
                self.bodyRect[0] = self.headPreviewsRect
            else:
                self.bodyRect[i] = self.bodyRect[i - 1]

            for rotation in self.rotate:
                if rotation[0] is True and self.bodyRect[i] == rotation[1]:
                    self.bodySprite[i] = pygame.transform.rotate(self.bodySprite[i], rotation[2])

    # move and create new body
    def move_body_and_create(self):
        self.move_body()
        self.create_body()
        try:
            if self.bodyRect[self.bodyLength - 1] == self.rotate[0][1]:
                self.bodySprite[self.bodyLength - 1] = pygame.transform.rotate(
                    self.bodySprite[self.bodyLength - 1], self.rotate[0][2])
        except IndexError:
            pass

    # move tail
    def move_tail(self):
        self.tailRect = self.bodyPreviewsRect
        if self.rotate:
            if self.tailRect == self.rotate[0][1]:
                self.tailSprite = pygame.transform.rotate(self.tailSprite, self.rotate[0][2])
                self.rotate.reverse()
                self.rotate.pop()
                self.rotate.reverse()

    # switch for moving
    def switch_speed(self, x):
        return {
            'left': (-self.speed, 0),
            'right': (self.speed, 0),
            'up': (0, -self.speed),
            'down': (0, self.speed)
        }[x]

    # switch for rotating angle
    @staticmethod
    def switch_angle(x):
        return {
            'left_up': 90,
            'left_down': -90,
            'right_up': -90,
            'right_down': 90,
            'up_left': -90,
            'up_right': 90,
            'down_left': 90,
            'down_right': -90
        }[x]

    # create new body
    def create_body(self):
        self.length += 1
        self.bodyLength += 1
        self.bodySprite.append(pygame.image.load('img/snake/body.jpg'))
        self.bodyRect.append(self.bodySprite[len(self.bodyRect) - 1].get_rect().move(self.bodyPreviewsRect.left,
                                                                                     self.bodyPreviewsRect.top))
        if ((not self.rotate) and (self.direction == 'left' or self.direction == 'right')) and self.bodyLength != 1:
            self.bodySprite[self.bodyLength - 1] = pygame.transform.rotate(self.bodySprite[self.bodyLength - 1], 90)
        try:
            if self.rotate[0][3] == 'left' or self.rotate[0][3] == 'right':
                self.bodySprite[self.bodyLength - 1] = pygame.transform.rotate(self.bodySprite[self.bodyLength - 1], 90)
        except IndexError:
            pass

    # moves everything together
    def move(self):
        self.update_previews_head_rect()
        self.move_head(self.switch_speed(self.direction))
        self.update_previews_body_rect()
        self.move_body()
        self.move_tail()

    # moves and grows another body part
    def move_and_grow(self):
        self.update_previews_head_rect()
        self.move_head(self.switch_speed(self.direction))
        self.update_previews_body_rect()
        self.move_body_and_create()

    # rotate head and add rotation
    def rotate_head(self, direction):
        if direction == 'left':
            # left
            if self.direction == 'up':
                self.angle = self.switch_angle('left_up')
            elif self.direction == 'down':
                self.angle = self.switch_angle('left_down')
            self.headSprite = pygame.transform.rotate(self.headSprite, self.angle)
        elif direction == 'right':
            # right
            if self.direction == 'up':
                self.angle = self.switch_angle('right_up')
            elif self.direction == 'down':
                self.angle = self.switch_angle('right_down')
            self.headSprite = pygame.transform.rotate(self.headSprite, self.angle)

        elif direction == 'up':
            # up
            if self.direction == 'left':
                self.angle = self.switch_angle('up_left')
            elif self.direction == 'right':
                self.angle = self.switch_angle('up_right')
            self.headSprite = pygame.transform.rotate(self.headSprite, self.angle)
        elif direction == 'down':
            # down
            if self.direction == 'left':
                self.angle = self.switch_angle('down_left')
            elif self.direction == 'right':
                self.angle = self.switch_angle('down_right')
            self.headSprite = pygame.transform.rotate(self.headSprite, self.angle)
        self.rotate.append([True, self.headRect, self.angle, self.direction])

    # print snake Rects for debug purposes
    def report(self):
        print('head: ', self.headRect)
        print('previews_head', self.headPreviewsRect)
        print('body: ', self.bodyRect)
        print('previews_body', self.bodyPreviewsRect)
        print('tail: ', self.tailRect)
        print('-----------------')


'''
Na classe Snake tem tudo o que diz respeito a cobra em sí, como destaques temos os atributos principais que são :
-length[tamanho];
-speed[velocidade];
-headSprite,bodySprite,tailSprite[sprites dos componentes da cobra];
-headRect,bodyRect,tailRect[objetos Rect referentes aos sprites];
e de funções:
-food_check()[checa por comida em contato com a cabeça da cobra];
-rotate_head()[muda a direção da cobra]
-move()[move a cobra]
-move_and_grow()[move e cria uma nova parte de corpo para a cobra]
'''

if __name__ == '__main__':
    pass

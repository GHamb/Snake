import pygame

# Autoria de Alan B. vital & Gustavo Hamburg


# food class
class Food:
    def __init__(self, x, y):
        # food sprite
        self.sprite = pygame.image.load('img/food.jpg')
        # food rect
        self.spriteRect = self.sprite.get_rect().move(x, y)

    # get coordinates aka food rect
    def coordinates(self):
        return self.spriteRect
'''
Na classe comida esta os atributos da mesma, assim como as coordenadas de onde ela será agregada como argumentos no momento de instancia da classe
'''
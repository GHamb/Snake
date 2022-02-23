from pygame import image

# Autoria de Alan B. vital & Gustavo Hamburg

# generic cell
class Cell:
    def __init__(self, x, y):
        self.cell = image.load('img/cells/cell.jpg')
        self.cellRect = self.cell.get_rect().move(x, y)

    @property
    def coordinates(self):
        return tuple((self.cellRect.left, self.cellRect.left))


# border left cell
class LCell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cell = image.load('img/cells/left_cell.jpg')


# border right cell
class RCell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cell = image.load('img/cells/right_cell.jpg')


# border top cell
class TCell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cell = image.load('img/cells/top_cell.jpg')


# border bottom cell
class BCell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cell = image.load('img/cells/bottom_cell.jpg')


# corner bottom left cell
class BLCell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cell = image.load('img/cells/corner_bottom_left.jpg')


# corner top left cell
class LTCell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cell = image.load('img/cells/corner_top_left.jpg')


# corner top right cell
class TRCell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cell = image.load('img/cells/corner_top_rigth.jpg')


# corner bottom right cell
class RBCell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cell = image.load('img/cells/corner_rigth_bottom.jpg')


'''
Na classe celula esta cada tipo de celula que compôe o tabuleiro
'''
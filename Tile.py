#!/usr/bin/python3
# -*- coding: utf-8 -*-


def _color(value: int) -> str:
    """
    :param value: valeur d'une tuile
    :return: couleur au format #RRGGBB
    """
    colors = {0: '#848484', 2: '#FFFFFF', 4: '#FFFF6B', 8: '#FF7F00',
              16: '#D6710C', 32: '#B9260A', 64: '#ED0000', 128: '#FFD700',
              256: '#FFD700', 512: '#FFD700', 1024: '#FFD700', 2048: '#FFD700',
              4096: '#FFD700', 8192: '#FFD700', 16384: '#FFD700', 32786: '#FFD700'}
    return colors[value]


class Tile(int):
    """
    Objet représentant la tuile, il hérite de int et possède une couleur
    """
    def __new__(cls, value=0):
        return super(Tile, cls).__new__(cls, value)

    @property
    def color(self) -> str:
        """
        :return: couleur au format #RRGGBB
        """
        return _color(self)

    @property
    def str(self):
        if self != 0:
            return str(self)
        else:
            return ''


if __name__ == '__main__':
    pass

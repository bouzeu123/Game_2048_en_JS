#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import Label
from Tile import Tile
from Score import Score
import random


class Grid(object):
    """
    Objet représentant la grille de jeu: elle est constituée des différentes tuiles
    gère le déplacement des tuiles
    gère les conditions de jeu
    gère le score
    """
    def __init__(self, parent, size=4):
        self.size = size
        self.parent = parent
        self.tiles = self.create_empty()
        self.labels = self.create_labels()
        self.init_tiles()
        self.score = Score()

    def init(self):
        self.tiles = self.create_empty()
        self.init_tiles()
        self.score.window.grid_remove()
        self.score = Score()
        self.update()

    def create_empty(self):
        return [[Tile()]*len(self) for _ in range(len(self))]

    @staticmethod
    def random() -> Tile:
        """
        :return: un tuile dont la valeur est choisie au hasard //
        probabilité => 2: 9/10 ; 4:1/10
        """
        return random.choice([Tile(2)] * 9 + [Tile(4)])

    def init_tiles(self):
        self.add_new_tile()
        self.add_new_tile()
        self.update()

    def add_new_tile(self):
        length = len(self)
        i = random.choice(range(length))
        j = random.choice(range(length))
        while self.tiles[i][j] != 0:
            i = random.choice(range(length))
            j = random.choice(range(length))
        self.tiles[i][j] = Grid.random()

    def create_labels(self):
        length = len(self)
        labels = [[None] * length for _ in range(length)]
        for i in range(length):
            for j in range(length):
                label = Label(self.parent,
                              font=("Helvetica", 16, "bold"),
                              text=self.tiles[i][j].str,
                              background=self.tiles[i][j].color,
                              borderwidth=4,
                              width=3,
                              justify='center')
                label.grid(row=i, column=j, padx=5, pady=5, ipadx=30, ipady=30)
                labels[i][j] = label
        return labels

    def update(self):
        length = len(self)
        for i in range(length):
            for j in range(length):
                tile = self.tiles[i][j]
                label = self.labels[i][j]
                label.config(text=tile.str, background=tile.color)

    def grid_remove(self):
        length = len(self)
        for i in range(length):
            for j in range(length):
                self.labels[i][j].grid_remove()
        self.score.window.grid_remove()

    @property
    def tile_max(self) -> int:
        max_rows = list()
        for row in self.tiles:
            max_rows.append(max(row))
        return max(max_rows)

    def __len__(self):
        return self.size

    @property
    def is_full(self) -> bool:
        length = len(self)
        for i in range(length):
            for j in range(length):
                if self.tiles[i][j] == 0:
                    return False
        return True

    @property
    def is_not_movable(self) -> bool:
        length = len(self)
        for row in self.tiles:
            for i in range(length-1):
                if row[i] == row[i+1]:
                    return False
        trans = self.transposed()
        for row in trans:
            for i in range(length-1):
                if row[i] == row[i+1]:
                    return False
        return True

    def merge(self, row: int):
        """
        :param row: ligne de la matrice à traiter
        Déplace les éléments d'une ligne vers la gauche:
        en supprimant les zeros
        et fusionne (additionne) les 2 premiers éléments identiques recontrés
        """
        store = []
        result = []
        for elt in self.tiles[row]:  # on vire les zéros
            if elt != 0:
                store.append(elt)
        store.extend([Tile()] * (len(self) - len(store)))
        i = 0
        while i < len(store) - 1:
            if store[i] == store[i+1]:
                colapse = store[i] + store[i+1]
                result.append(Tile(colapse))
                self.score.value = self.score.value+colapse
                i += 2
            else:
                result.append(store[i])
                i += 1
        result.append(Tile(store[-1]))  # ajout du dernier élément
        result.extend([Tile()] * (len(self.tiles) - len(result)))
        self.tiles[row] = result

    def move(self):
        """
        Déplace l'ensemble de la matrice vers la gauche
        """
        for i in range(len(self)):
            self.merge(i)
        if not self.is_full:
            self.add_new_tile()

    def mirror(self):
        """
        Réalise un mirroir sur la matrice:
        [ 1 2 3 4 ] devient [ 4 3 2 1]
        la transformation se fait en place
        """
        store = self.create_empty()
        length = len(self)
        for i in range(length):
            for j in range(length):
                store[i][j] = self.tiles[i][length-1-j]
        self.tiles = store

    def transposed(self):
        """
        :return: le transposé de la matrice
        """
        result = self.create_empty()
        length = len(self)
        for i in range(length):
            for j in range(length):
                result[i][j] = self.tiles[j][i]
        return result

    def transpose(self):
        """
        Transpose la matrice en place
        """
        self.tiles = self.transposed()

    def anti_transpose(self):
        """
        Réalise la symétrie selon l'axe oblique inverse:
        | 1  2  3  4 |                   | 16 12  8  4 |
        | 5  6  7  8 |     devient       | 15 11  7  3 |
        | 9 10 11 12 |                   | 14 10  6  2 |
        |13 14 15 16 |                   | 13  9  5  1 |
        la transformation se fait en place
        """
        store = self.create_empty()
        length = len(self)
        for i in range(length):
            for j in range(length):
                store[i][j] = self.tiles[length-1-j][length-1-i]
        self.tiles = store

    def is_not_movable(self) -> bool:
        """
        Est-ce-que la grille peut être déplacée
        """
        length = len(self)
        for row in self.tiles:
            for i in range(length-1):
                if row[i] == row[i+1]:
                    return False
        trans = self.transposed()
        for row in trans:
            for i in range(length-1):
                if row[i] == row[i+1]:
                    return False
        return True

    def __str__(self):
        length = len(self)
        result = "+----" * length + '+' + '\n'
        for row in self.tiles:
            result += '|'
            for elt in row:
                result += "{:^4}".format(elt) + '|'
            result += '\n' + "+----" * length + '+' + '\n'
        return result


if __name__ == '__main__':
    pass

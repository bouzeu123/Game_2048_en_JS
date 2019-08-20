#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Grid import Grid
from tkinter import Tk, Menu, messagebox


class Game(object):
    """
    Gère l'éxécuton de la partie en cours
    et détermine su celle-ci s'est terminée par une victoire ou non
    """
    def __init__(self):
        self.window = self.init_window()
        self.game_board = Grid(self.window)
        self.init_keys()

    def init_window(self):
        root = Tk()
        root.iconbitmap('favicon.ico')
        root.title('')
        menubar = Menu(root)
        root.config(menu=menubar)
        menu = Menu(menubar, tearoff=0)
        menu.add_radiobutton(label="4X4", command=lambda: self.resize(4))
        menu.add_radiobutton(label="5X5", command=lambda: self.resize(5))
        menu.add_radiobutton(label="6X6", command=lambda: self.resize(6))
        menu.add_command(label="Quitter", command=root.destroy)
        menubar.add_cascade(label="Réglages", menu=menu)
        return root

    def init_keys(self):
        self.window.bind_all('<Key-Down>', self.move_down)
        self.window.bind_all('<Key-Left>', self.move_left)
        self.window.bind_all('<Key-Right>', self.move_right)
        self.window.bind_all('<Key-Up>', self.move_up)
        self.window.mainloop()

    def init(self):
        self.game_board.init()

    def resize(self, new_size):
        response = messagebox.askyesno("Resize",
                                       "Redimensionner la grille  de : {0}X{0} vers {1}X{1} ? "
                                       .format(self.game_board.size, new_size))
        if response:
            self.game_board.grid_remove()
            self.game_board = Grid(self.window, new_size)
            self.game_board.score.window.grid(columnspan=new_size)
            self.init()

    def move(self):
        """
        Le game board sera déplacé que si la partie est encore jouable (non terminée)
        sinon le meilleur score eventuel est sauvegardé
        """
        if self.is_game_over():
            if self.is_win():
                replay = messagebox.askyesno("Bravo", "Vous avez gagné ! Rejouer ?")
            else:
                replay = messagebox.askyesno("Perdu", "Oh lala c'est perdu ! Rejouer ?")
            if replay:
                self.init()
        else:
            self.game_board.move()

    def move_up(self, event):
        self.game_board.transpose()
        self.move()
        self.game_board.transpose()
        self.game_board.update()

    def move_left(self, event):
        self.move()
        self.game_board.update()

    def move_right(self, event):
        self.game_board.mirror()
        self.move()
        self.game_board.mirror()
        self.game_board.update()

    def move_down(self, event):
        self.game_board.anti_transpose()
        self.move()
        self.game_board.anti_transpose()
        self.game_board.update()

    def is_game_over(self) -> bool:
        return self.game_board.is_not_movable() and self.game_board.is_full

    def is_win(self) -> bool:
        return self.game_board.tile_max >= 2048


if __name__ == '__main__':
    Game()


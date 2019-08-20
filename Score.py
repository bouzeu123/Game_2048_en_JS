#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import LabelFrame, Label


class Score:
    def __init__(self):
        self._value = 0
        self.high = Score.init_high()
        self.value_label = Label()
        self.high_label = Label()
        self.window = self.init_window()

    @staticmethod
    def init_high() -> int:
        try:
            with open("highcore.txt", "r+") as highcore_file:
                high = highcore_file.read()
        except FileNotFoundError:
            highcore_file = open("highcore.txt", "w")
            high = '0'
            highcore_file.write(high)
        return int(high)

    def init_window(self):
        root = Label()
        left = LabelFrame(root, text="Score")
        left.grid(row=0, column=0)
        right = LabelFrame(root, text="High")
        right.grid(row=0, column=1)
        self.value_label = Label(left, text=str(self._value), font=("Helvetica", 16, "bold"))
        self.value_label.grid(padx=5, pady=5, ipadx=5, ipady=5)
        self.high_label = Label(right, text=str(self.high), font=("Helvetica", 16, "bold"))
        self.high_label.grid(padx=5, pady=5, ipadx=5, ipady=5)
        root.grid(columnspan=4)
        return root

    def update(self):
        self.value_label.configure(text=str(self._value))
        self.high_label.configure(text=str(self.high))

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value != self._value:
            self._value = new_value
            if self._value > self.high:
                self.high = self._value
                self.save()
            self.update()

    def save(self):
        with open("highcore.txt", "r+") as highcore_file:
            highcore_file.seek(0)
            highcore_file.write(str(self.high))
            highcore_file.truncate()

    @property
    def str(self):
        if self != 0:
            return str(self)
        else:
            return ''


if __name__ == '__main__':
    score = Score()
    score.window.mainloop()

from Tkinter import *
import ttk
import os
import sys
import re
import string
import threading
import Queue

__author__ = 'Travis'

class piece:

    def __init__(self, frame,  row, column, red, black):

        self.y = row
        self.x = column
        self.red = red
        self.black = black
        self.type = ""

        button = Button(frame)
        button["command"] = self.click
        button["height"] = 2
        button["width"] = 8

        if row > 5:
            if row % 2 == 0:
                if column % 2 == 1:
                    # button["image"] = red
                    button["text"] = "red"
                    self.type = "red"
            else:
                if column % 2 == 0:
                    # button["image"] = black
                    button["text"] = "red"
                    self.type = "red"
        if row < 4:
            if row % 2 == 0:
                if column % 2 == 1:
                    # button["image"] = red
                    button["text"] = "black"
                    self.type = "black"
            else:
                if column % 2 == 0:
                    # button["image"] = black
                    button["text"] = "black"
                    self.type = "black"

        if row % 2 == 0:
            if column % 2 == 1:
                button["bg"] = '#FFFFCC'
            else:
                button["bg"] = '#8A5C00'
        else:
            if column % 2 == 1:
                button["bg"] = '#8A5C00'
            else:
                button["bg"] = '#FFFFCC'

        button.grid(row=row, column=column, sticky='ewns')
        self.button = button

    def click(self):
        # self.master.destroy()
        self.button["state"] = 'disabled'

    def changeType(self, newType):

        self.button["text"] = newType


class application:

    def __init__(self, master, lock, AiQueue, GuiQueue):

        # Creating uir objects
        self.master = master
        self.frame = Frame()
        self.frame.grid()
        self.board = []
        self.red = PhotoImage(file='red.gif')
        self.black = PhotoImage(file='black.gif')
        self.createWidgets()
        self.lock = lock
        self.AiQueue = AiQueue
        self.GuiQueue = GuiQueue
        self.updateScreen()


        # self.master.mainloop()


    def createWidgets(self):

        for i in range(0, 10):
            row = []
            for j in range(0, 10):
                row.append(piece(self.frame, i, j, self.red, self.black))

            self.board.append(row)


    def updateScreen(self):

        while 1:
            self.frame.update()
            try:
                tempBoard = self.AiQueue.get()

            except:
                pass

            i = 0
            j = 0

            for row in tempBoard:

                for column in row:

                    self.board[i][j].changeType(column)
                    j += 1
                i += 1


        print 'hello'
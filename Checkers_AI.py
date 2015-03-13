__author__ = 'Travis'


import os
import re
import sys
import threading
import Queue


class ArtificialIntelligence:

    def __init__(self, lock, AiQueue, GuiQueue):

        self.lock = lock
        self.AiQueue = AiQueue
        self.GuiQueue = GuiQueue

    def Start(self):

        while 1:

            # check queue for button presses
            try:
                press = self.GuiQueue.get()

            except:
                press = "cancel"
                pass

            while 1 and press != "cancel":
                try:
                    press2 = self.GuiQueue.get()
                    break

                except:
                    pass
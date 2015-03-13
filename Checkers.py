__author__ = 'Travis'

import Tkinter as tk
import Checkers_uir
import Checkers_AI
import ttk
import threading
import Queue


class GuiThread(threading.Thread):
    def __init__(self, threadID, name, lock, AiQueue, GuiQueue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.lock = lock
        self.AiQueue = AiQueue
        self.GuiQueue = GuiQueue

    def run(self):
        gui = tk.Tk()
        app = Checkers_uir.application(gui, self.lock, self.AiQueue, self.GuiQueue)
        app.master.mainloop()


class AiThread(threading.Thread):
    def __init__(self, threadID, name, lock, AiQueue, GuiQueue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.lock = lock
        self.AiQueue = AiQueue
        self.GuiQueue = GuiQueue

    def run(self):

        AI = Checkers_AI.ArtificialIntelligence(self.lock, self.AiQueue, self.GuiQueue)
        AI.Start()
        print 'hello im a ai'


if __name__ == '__main__':

    # Start application threads
    queueLock = threading.Lock()
    AiQueue = Queue.Queue()
    GuiQueue = Queue.Queue()
    threadGui = GuiThread(0, "MainGui", queueLock, AiQueue, GuiQueue)
    threadAi = AiThread(1, "AI", queueLock, AiQueue, GuiQueue)
    threadGui.start()
    threadAi.start()
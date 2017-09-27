from tkinter import *
import string
import time
import random 
import threading

class MatchingGame():

  def __init__(self):
    self.isopen = False
    self.opened = None
    self.root = Tk()
    self.player = True
    self.changeturn = False
    self.getscreen()

  def getscreen(self):
    c = r = 0
    for al in self.getrandom(10):
      label = Label(self.root, text = al, width = 4, height = 2)
      self.addbutton(r, c)
      label.grid(row = r, column = c)
      c+=1
      if c >= 4:
        r+=1
        c=0
    self.player1 = Label(self.root, text = "Player1:", width = 6, height = 2)
    self.player1.grid(row = r, column = 0)
    self.player1_score = Label(self.root, text = "0", width = 4, height = 2)
    self.player1_score.grid(row = r, column = 1)
    self.player2 = Label(self.root, text = "Player2:", width = 6, height = 2)
    self.player2.grid(row = r, column = 2)
    self.player2_score = Label(self.root, text = "0", width = 4, height = 2)
    self.player2_score.grid(row = r, column = 3)

  def addbutton(self, row, column):
    cmd = lambda row = row, column = column : self.onclick(row, column)
    button = Button(self.root, width = 1, command = cmd)
    button.grid(row = row, column = column)

  def playerturn(self):
    threading.Thread(target = self._playerturn).start()

  def _playerturn(self):
    while True:
      if self.changeturn:
        self.player = not self.player
        if self.player:
          self.player1["bg"] = "yellow"
          self.player2["bg"] = "white"
        else:
          self.player1["bg"] = "white"
          self.player2["bg"] = "yellow"
        self.changeturn = False

  def onclick(self, row, column):
    print(self.isopen)
    for wg in self.root.grid_slaves(row, column):
      if wg.__class__ == Label().__class__: 
        opening = wg
      else:
        button = wg
    print(button)
    button.grid_remove()
    if self.isopen:
      if self.opened["text"] != opening["text"]:
        self.refresh(self.opened.grid_info()["row"], self.opened.grid_info()["column"], opening.grid_info()["row"], opening.grid_info()["column"])
      else:
        if self.player:
          self.player1_score["text"] = str(int(self.player1_score["text"])+1)
        else:
          self.player2_score["text"] = str(int(self.player2_score["text"])+1)
      self.changeturn = True
      self.isopen = False
    else:
      self.opened = opening
      self.isopen = True
    del button

  def refresh(self, row1, column1 ,row2 ,column2):
    target = lambda row1 = row1, column1 = column1, row2 = row2, column2 = column2 : self._refresh(row1, column1 ,row2 ,column2)
    threading.Thread(target=target).start()

  def _refresh(self, row1, column1 ,row2 ,column2):
    time.sleep(0.5) 
    self.addbutton(row1, column1)
    self.addbutton(row2, column2)

  def getrandom(self, n):
    random_ascii = ((random.sample([ c for c in string.ascii_lowercase], n))*2)
    random.shuffle(random_ascii)
    return random_ascii

  def startgame(self):
    self.playerturn()
    self.root.mainloop()




game = MatchingGame()
game.startgame()
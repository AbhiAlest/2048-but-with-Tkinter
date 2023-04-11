import tkinter as tk
import c
import random as r


class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Tkinter 2048")
        self.mgrid = tk.Frame(
            self, bg=c.gc, bd=3, width=400, height=400)
        self.mgrid.grid(pady=(80, 0))
        self.mGUI()
        self.start()
      
        self.master.bind("<Left>", self.l)
        self.master.bind("<Right>", self.r)
        self.master.bind("<Up>", self.u)
        self.master.bind("<Down>", self.d)
      
        self.mainloop()
    def mGUI(self):
        self.tiles = []
        for i in range(4):
            ro = []
            for j in range(4):
                cframe = tk.Frame(
                    self.mgrid,
                    bg=c.etc,
                    width=100,
                    height=100)
                cframe.grid(row=i, column=j, padx=5, pady=5)
                cnumber = tk.Label(self.mgrid, bg=c.etc)
                cnumber.grid(row=i, column=j)
                cdata = {"frame": cframe, "number": cnumber}
                ro.append(cdata)
            self.tiles.append(ro)
          
        sframe = tk.Frame(self)
        sframe.place(relx=0.5, y=40, anchor="center")
        tk.Label(
            sframe,
            text="Score",
            font=c.slf).grid(
            row=0)
        self.score_label = tk.Label(sframe, text="0", font=c.sf)
        self.score_label.grid(row=1)

    def start(self):
        self.m = [[0] * 4 for _ in range(4)]
        row = r.randint(0, 3)
        col = r.randint(0, 3)
        self.m[row][col] = 2
        self.tiles[row][col]["frame"].configure(bg=c.tc[2])
        self.tiles[row][col]["number"].configure(
            bg=c.tc[2],
            fg=c.tnc[2],
            font=c.tnf[2],
            text="2")
        while self.m[row][col] != 0:
            row = r.randint(0, 3)
            col = r.randint(0, 3)
        self.m[row][col] = 2
        self.tiles[row][col]["frame"].configure(bg=c.tc[2])
        self.tiles[row][col]["number"].configure(
            bg=c.tc[2],
            fg=c.tnc[2],
            font=c.tnf[2],
            text="2")
        self.score = 0

    def stacker(self):
        nm = [[0] * 4 for r in range(4)]
        for i in range(4):
            fiposition = 0
            for j in range(4):
                if self.m[i][j] != 0:
                    nm[i][fiposition] = self.m[i][j]
                    fiposition = 1+fiposition
        self.m = nm

    def combiner(self):
        for i in range(4):
            for j in range(3):
                if self.m[i][j] != 0 and self.m[i][j] == self.m[i][j + 1]:
                    self.m[i][j] = 2*self.m[i][j]
                    self.m[i][j + 1] = 0
                    self.score = self.m[i][j]+self.score
                  
    def reverser(self):
        nm = []
        for i in range(4):
            nm.append([])
            for j in range(4):
                nm[i].append(self.m[i][-j+3])
        self.m = nm

    def changer(self):
        nm = [[0] * 4 for r in range(4)]
        for i in range(4):
            for j in range(4):
                nm[i][j] = self.m[j][i]
        self.m = nm

    def adder(self):
        row = r.randint(0, 3)
        col = r.randint(0, 3)
        while(self.m[row][col] != 0):
            row = r.randint(0, 3)
            col = r.randint(0, 3)
        self.m[row][col] = r.choice([2, 4])

    def GUIupdater(self):
        for i in range(4):
            for j in range(4):
                cvalue = self.m[i][j]
                if cvalue == 0:
                    self.tiles[i][j]["frame"].configure(bg=c.etc)
                    self.tiles[i][j]["number"].configure(
                        bg=c.etc, text="")
                else:
                    self.tiles[i][j]["frame"].configure(
                        bg=c.tc[cvalue])
                    self.tiles[i][j]["number"].configure(
                        bg=c.tc[cvalue],
                        fg=c.tnc[cvalue],
                        font=c.tnf[cvalue],
                        text=str(cvalue))
        self.score_label.configure(text=self.score)
        self.update_idletasks()

    def l(self, eve):
        self.stacker()
        self.combiner()
        self.stacker()
        self.adder()
        self.GUIupdater()
        self.gover()

    def r(self, eve):
        self.reverser()
        self.stacker()
        self.combiner()
        self.stacker()
        self.reverser()
        self.adder()
        self.GUIupdater()
        self.gover()

    def u(self, eve):
        self.changer()
        self.stacker()
        self.combiner()
        self.stacker()
        self.changer()
        self.adder()
        self.GUIupdater()
        self.gover()

    def d(self, event):
        self.changer()
        self.reverser()
        self.stacker()
        self.combiner()
        self.stacker()
        self.reverser()
        self.changer()
        self.adder()
        self.GUIupdater()
        self.gover()

    def hmove(self):
        for i in range(4):
            for j in range(3):
                if self.m[i][j] == self.m[i][j + 1]:
                    return True
        return False

    def vmove(self):
        for i in range(3):
            for j in range(4):
                if self.m[i][j] == self.m[i + 1][j]:
                    return True
        return False

    def gover(self):
        if any(2048 in row for row in self.m): #winner
            goverf = tk.Frame(self.mgrid, borderwidth=2)
            goverf.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                goverf,
                text="Winner!",
                bg=c.wb,
                fg=c.gofc,
                font=c.gof).pack()
        elif not any(0 in row for row in self.m) and not self.hmove() and not self.vmove():
            goverf = tk.Frame(self.mgrid, borderwidth=2)
            goverf.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                goverf,
                text="You lost!",
                bg=c.lbg,
                fg=c.gofc,
                font=c.gof).pack()

Game()

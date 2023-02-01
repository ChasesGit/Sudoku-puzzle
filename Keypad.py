from tkinter import *
from TileClass import Tile


class KeyPadTile:
    def __init__(self, master=None, value=0, width=4, height=1, board=None) -> None:
        self.value = value
        self.board = board
        self.lstOfTiles = []
        self.button = Button(master,
                             height=height,
                             width=width,
                             command=self.click,
                             font=("Impact", 20)
                             )
        self.update()

    def update(self) -> None:
        self.button['text'] = str(self.value)

    def click(self) -> None:
        if Tile.SELECTED_BUTTON is not None and Tile.SELECTED_BUTTON.getState():
            Tile.SELECTED_BUTTON.setValue(self.value)

        if self.value == 10:
            new = self.board.boardGen()
            counter = 0
            for j in range(3):
                for i in range(3):
                    for k in range(3):
                        for l in range(3):
                            self.lstOfTiles.append(self.board.blockObjs[j][i].tileObjs[k][l])
            for block in range(9):
                for row in new[block]:
                    for num in row:
                        self.lstOfTiles[counter].setValue(num)
                        self.lstOfTiles[counter].isActive = self.lstOfTiles[counter].setState()
                        self.lstOfTiles[counter].setColor("white")
                        counter += 1

        if self.value == 11:
            solve = self.board.allBoard
            counter = 0
            for j in range(3):
                for i in range(3):
                    for k in range(3):
                        for l in range(3):
                            self.lstOfTiles.append(self.board.blockObjs[j][i].tileObjs[k][l])
            for block in range(9):
                for row in solve[block]:
                    for num in row:
                        self.lstOfTiles[counter].setValue(num)
                        self.lstOfTiles[counter].isActive = self.lstOfTiles[counter].setState()
                        self.lstOfTiles[counter].setColor()
                        counter += 1

    def getButton(self):
        return self.button

    def setState(self) -> bool:
        if self.value == 0:
            self.button['state'] = ACTIVE
            return True
        else:
            self.button['state'] = DISABLED
            return False


class KeyPad:
    def __init__(self, master=None, board=None) -> None:
        self.numBlocks = []
        self.board = board
        self._createPad(master)

    def _createPad(self, master):
        counter = 1
        for column in range(9):
            self.numBlocks.append(KeyPadTile(master, counter))
            self.numBlocks[column].getButton().grid(row=1, column=column, padx=2, pady=1)
            counter += 1
        clearButton = KeyPadTile(master, width=45)
        clearButton.getButton().grid(row=2, columnspan=10, pady=1, padx=1)
        clearButton.getButton()['text'] = 'Clear Tile'
        newGame = KeyPadTile(master, width=45, value=10, board=self.board)
        newGame.getButton().grid(row=3, columnspan=10, pady=1, padx=1)
        newGame.getButton()['text'] = 'New Game'
        solveGame = KeyPadTile(master, width=45, value=11, board=self.board)
        solveGame.getButton().grid(row=4, columnspan=11, pady=1, padx=1)
        solveGame.getButton()['text'] = 'Solve Board'

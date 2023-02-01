from random import sample, uniform
from tkinter import *
import BlockClass as b
import Functions as func
import math as m


class Board:
    def __init__(self, master=None) -> None:
        self.allBoard = None
        self.blockObjs = [[], [], []]
        self.board = self.boardGen()
        self._createBoard(master, self.board)

    def _createBoard(self, master, board):
        board_index = 0
        for row in range(int(m.sqrt(len(board)))):
            for col in range(int(m.sqrt(len(board)))):
                fr = Frame(master, bg='darkblue')
                self.blockObjs[row].append(
                    b.Block(fr, board[board_index]))
                fr.grid(row=row, column=col, padx=2, pady=2)
                board_index += 1

    # removes values for user input spaces
    def _removeValues(self, board):
        for i, block in enumerate(board):
            for j, row in enumerate(block):
                for k, value in enumerate(row):
                    threashold = uniform(0, 1)
                    # print(f'Value {value} is at cords Block {i}, Row {j}, Index {k} with a threashold of {
                    # threshold}')
                    if threashold < 0.75:
                        board[i][j][k] = 0

    def checkBoard(self) -> bool:
        for row in self.blockObjs:
            for block in row:
                if not block.checkBlock():
                    return False

        for row in range(len(self.blockObjs)):
            for col in range(len(self.blockObjs[row])):
                if not self.checkRow(row, col):
                    return False
                if not self.checkColumn(row, col):
                    return False
        return True

    def checkRow(self, block_index, block_row) -> bool:
        x = set()
        for block in self.blockObjs[block_index]:
            x.update(block.getRow(block_row))
        return func.checkSet(x)

    def checkColumn(self, block_index, block_col) -> bool:
        x = set()
        for board_row in range(3):
            x.update(self.blockObjs[board_row]
                     [block_index].getColumn(block_col))
        return func.checkSet(x)

    # pattern for a baseline valid solution
    def pattern(self, r, c, base, side):
        return (base * (r % base) + r // base + c) % side

    # randomize rows, columns and numbers (of valid base pattern)
    def shuffle(self, s) -> list:
        return sample(s, len(s))

    def getBoard(self) -> list:
        return self.blockObjs

    def boardGen(self):
        base = 3
        side = base * base
        rBase = range(base)
        rows = [g * base + r for g in self.shuffle(rBase) for r in self.shuffle(rBase)]
        cols = [g * base + c for g in self.shuffle(rBase) for c in self.shuffle(rBase)]
        nums = self.shuffle(range(1, base * base + 1))
        board = [[nums[self.pattern(r, c, base, side)] for c in cols] for r in rows]
        fixedBoard = self._fixDataStructure(board, base)
        # I have monkey brain so I needed to store this somewhere, so I can hide values l8r
        self.allBoard = self._fixDataStructure(board, base)
        self._removeValues(fixedBoard)
        return fixedBoard

    def _fixDataStructure(self, board, base) -> list:
        new_ = []
        segmented_ = []
        completed_ = []

        for i in range(0, 9):
            for j in range(0, 9):
                new_.append(board[i][j])
                if len(new_) == 3:
                    segmented_.append(new_)
                    new_ = []
        i = 0
        while i < len(segmented_) - (base * 2):
            new_.append(segmented_[i])
            new_.append(segmented_[i + base])
            new_.append(segmented_[i + base * 2])
            completed_.append(new_)
            i += 1
            new_ = []
            if i % 3 == 0:
                i += 6
        return completed_

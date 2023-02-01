import TileClass as T


class Block:

    def __init__(self, master, tileValues) -> None:
        self.tileObjs = [[], [], []]
        self._createBlock(master, tileValues)
        self.set = self.updateSet()

    def _createBlock(self, master, values):
        for row_index, row in enumerate(values):
            for col_index in range(len(row)):
                self.tileObjs[row_index].append(
                    T.Tile(master, values[row_index][col_index], self))
                self.tileObjs[row_index][col_index].getButton().grid(
                    row=row_index, column=col_index, padx=1, pady=1)

    def updateSet(self) -> set:
        x = set()
        for row in range(len(self.tileObjs)):
            x.update(self.getRow(row))
        self.set = x
        return x

    def getRow(self, row_index) -> list:
        return [value.getValue() for value in self.tileObjs[row_index]]

    def getColumn(self, col_index) -> list:
        return [self.tileObjs[row_index][col_index].getValue() for row_index in range(len(self.tileObjs))]

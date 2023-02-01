import BoardClass
import BlockClass
import TileClass


def checkSet(numSet) -> bool:
    if len(numSet) == 9 and 0 not in numSet:
        return True
    else:
        return False


def checkBoard(board) -> bool:
    for row in board:
        for block in row:
            if not block.checkBlock():
                return False

    for row in range(len(board)):
        for col in range(len(board[row])):
            if not checkRow(row, col):
                return False
            if not checkColumn(row, col):
                return False
    return True


def checkRow(block_index, block_row) -> bool:
    x = set()
    for block in self.blockObjs[block_index]:
        x.update(block.getRow(block_row))
    return checkSet(x)


def checkColumn(block_index, block_col) -> bool:
    x = set()
    for board_row in range(3):
        x.update(self.blockObjs[board_row]
                 [block_index].getColumn(block_col))
    return checkSet(x)


def checkBlock(block) -> bool:
    return checkSet(block.set)

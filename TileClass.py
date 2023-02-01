from tkinter import *


class Tile:
    SELECTED_BUTTON = None

    def __init__(self, master, value, block) -> None:
        self.value = value
        self.parent = block
        self.button = Button(master,
                             height=1,
                             width=4,
                             command=self.click,
                             font=('Impact', 20)
                             )
        self.isActive = self.setState()
        self.setColor()
        self.update()

    def setColor(self, color=None):
        if self.isActive:
            self.button['bg'] = color
            self.button['activeforeground'] = 'blue'
        else:
            self.button['bg'] = '#90c8ff'

    # Need to be able retrieve button object to use layout managers
    def getButton(self) -> Button:
        return self.button

    # updates the label on buttons as well as can lock/unlock buttons
    def update(self) -> None:
        if self.value == 0 or self.value >= 10:
            self.button['text'] = ''
        else:
            self.button['text'] = str(self.value)

    # what happens when button is clicked
    def click(self) -> None:
        self.update()
        # print('Block Set: ', self.parent.updateSet())
        Tile.SELECTED_BUTTON = self

    def getValue(self) -> int:
        return self.value

    def setValue(self, value: int):
        self.value = value
        self.update()

    def getState(self) -> bool:
        return self.isActive

    def setState(self) -> bool:
        if self.value == 0:
            self.button['state'] = ACTIVE
            return True
        else:
            self.button['state'] = DISABLED
            return False

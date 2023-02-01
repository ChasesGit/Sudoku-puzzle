from tkinter import *
import BoardClass as bc
import Keypad as kp


def main():
    root = Tk()

    width = 625
    height = 900
    root.title('Sudoku Puzzle Game')
    root.geometry(f'{width}x{height}')
    root.configure(bg='light blue')
    root.resizable(False, False)

    board_frame = Frame(root, background='darkblue')
    board_frame.pack(pady=15)
    board = bc.Board(board_frame)

    keypad_frame = Frame(root, background='darkblue')
    keypad_frame.pack(pady=20)
    keypad = kp.KeyPad(keypad_frame, board=board)

    # Frame Loop content must be above this line
    root.mainloop()


if __name__ == '__main__':
    main()

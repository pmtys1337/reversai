import tkinter as tk
import board.board as bo

#root = tk.Tk()
#screen = tk.Canvas(root, width=500, height=500,
#                        background="#222", highlightthickness=0)
#screen.pack()

board = bo.Board()
board.show_board()
board.move()
board.show_board()
board.move()
board.show_board()

#root.wm_title("ReversAI")
#root.mainloop()

class Board:
    def __init__(self):
        # Initializing an empty board
        self.__board = self._clean_board()

    # private methods
    def _clean_board(self):
        new_board = []
        for x_coord in range(8):
            new_board.append([])
            for y_coord in range(8):
                new_board[x_coord].append(None)
        #Initializing the center values
        new_board[3][3]="w"
        new_board[3][4]="b"
        new_board[4][3]="b"
        new_board[4][4]="w"

        return new_board

    def _load_board(self, path):
        new_board = self._clean_board()
        with open(path) as in_file:
            x_coord = 0
            for line in in_file:
                assert(x_coord < 8)
                for y_coord in range(8):
                    new_board[x_coord][y_coord] = line[y_coord]
                x_coord += 1

        return new_board

    # public methods
    def show_board(self, screen=None, outline=False):
        # It can be showed on consloe
        if not screen:
            for x_coord in range(8):
                for y_coord in range(8):
                    act_field = self.__board[x_coord][y_coord]
                    if act_field:
                        print(act_field+" ", end="")
                    else:
                        print("- ", end="")
                print("\n")
        else:
            try:
                # If we want an outline on the board then draw one
                if outline:
                    screen.create_rectangle(50,50,450,450,outline="#111")
                # Drawing the intermediate lines
                for i in range(7):
                    lineShift = 50+50*(i+1)
                    # Horizontal line
                    screen.create_line(50,lineShift,450,lineShift,fill="#111")
                    # Vertical line
                    screen.create_line(lineShift,50,lineShift,450,fill="#111")
                screen.update()
            except:
                print("Dude..WTF")

    # Save actual state of board to a given PATH
    def save_game(self, path="out.txt"):
        with open(path, "w") as out_file:
            for i in range(8):
                for j in range(8):
                    act_field = self.__board[i][j]
                    if act_field:
                        out_file.write(act_field)
                    else:
                        out_file.write("-")
                out_file.write("\n")

    # Load a game from a given path
    def load_game(self, path):
        try:
            self.__board = self._load_board()
        except:
            print("WHAT now..")

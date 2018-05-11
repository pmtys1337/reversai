class Board:
    def __init__(self):
        # Initializing an empty board
        self.__board = self.__clean_board()
        # Initializing the first player (white)
        self.__player = 0

    # private methods
    def __clean_board(self):
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

    def __get_dcboard(self):
        deepc_board = []
        for x_coord in range(8):
            line = []
            for y_coord in range(8):
                line.append(self.__board[x_coord][y_coord])
            deepc_board.append(line)

        return deepc_board

    def __load_board(self, path):
        new_board = self.__clean_board()
        with open(path) as in_file:
            x_coord = 0
            for line in in_file:
                assert(x_coord < 8)
                for y_coord in range(8):
                    act_field = line[y_coord]
                    new_board[x_coord][y_coord] = \
                        act_field if act_field != "-" else None
                x_coord += 1

        return new_board

    def __is_valid_move(self, move_x, move_y):
        # TODO: add rules of reversi
        if self.__board[move_x][move_y] != None:
            return False

        return True

    def __make_a_move(self, move_x, move_y):
        if self.__is_valid_move(move_x, move_y):
            colour = "w" if self.__player == 0 else "b"
            # we have to use "deep" copy
            new_board = self.__get_dcboard()
            # the move
            # TODO: add rules of reversi
            new_board[move_x][move_y] = colour

            return new_board
        # TODO: invalid move case
        return None

#   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---

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
                    line_shift = 50+50*(i+1)
                    # Horizontal line
                    screen.create_line(50,line_shift,450,line_shift,fill="#111")
                    # Vertical line
                    screen.create_line(line_shift,50,line_shift,450,fill="#111")
                screen.update()
            except:
                print("Dude..WTF")

    # Save actual state of board to a given PATH
    def save_game(self, path="out.txt"):
        with open(path, "w") as out_file:
            for x_coord in range(8):
                for y_coord in range(8):
                    act_field = self.__board[x_coord][y_coord]
                    if act_field:
                        out_file.write(act_field)
                    else:
                        out_file.write("-")
                out_file.write("\n")

    # Load a game from a given path
    def load_game(self, path):
        try:
            self.__board = self.__load_board()
        except:
            print("WHAT now..")

class Board:
    # INIT

    def __init__(self, screen = None, hint = True):
        self.__board = self.__clean_board() # Initializing an empty board
        self.__player = 0 # Initializing the first player (white)
        self.__valid_moves = self.__get_valid_moves() # Have to know
        self.__screen = screen # Can play with graph and console too
        self.__hint = hint # Show valid moves for player
        self.__alphabet_coords = {
            "A": 0, "B": 1, "C": 2, "D": 3,
            "E": 4, "F": 5, "G": 6, "H": 7
        } # Alphabet coords for console

    # PRIVATE METHODS

    def __clean_board(self):
        new_board = []
        for row_idx in range(8):
            new_board.append([])
            for col_idx in range(8):
                new_board[row_idx].append(None)
        #Initializing the center values
        new_board[3][3]="w"
        new_board[3][4]="b"
        new_board[4][3]="b"
        new_board[4][4]="w"

        return new_board

    def __get_dcboard(self):
        deepc_board = []
        for row_idx in range(8):
            line = []
            for col_idx in range(8):
                line.append(self.__board[row_idx][col_idx])
            deepc_board.append(line)

        return deepc_board

    def __load_board(self, path):
        new_board = self.__clean_board()
        with open(path) as in_file:
            row_idx = 0
            for line in in_file:
                assert(row_idx < 8)
                for col_idx in range(8):
                    act_field = line[col_idx]
                    new_board[row_idx][col_idx] = \
                        act_field if act_field != "-" else None
                row_idx += 1

        return new_board

    def __get_valid_moves(self):
        valid_moves = []
        colour = "w" if self.__player == 0 else "b"
        for row_idx in range(8):
            for col_idx in range(8):
                if not self.__board[row_idx][col_idx]:
                    neighbours = []
                    for ri in range(max(0,row_idx-1),min(row_idx+2,8)):
                        for ci in range(max(0,col_idx-1),min(col_idx+2,8)):
                            if self.__board[ri][ci]:
                                neighbours.append((ri,ci))

                    for neighbour in neighbours:
                        neigh_row = neighbour[0]
                        neigh_col = neighbour[1]
                        if self.__board[neigh_row][neigh_col] == colour:
                            continue
                        else:
                            delta_row = neigh_row - row_idx
                            delta_col = neigh_col - col_idx
                            tmp_row = neigh_row
                            tmp_col = neigh_col
                            while 0 <= tmp_row <= 7 and 0 <= tmp_col <= 7:
                                if self.__board[tmp_row][tmp_col] == None:
                                    break
                                if self.__board[tmp_row][tmp_col] == colour:
                                    valid_moves.append((row_idx,col_idx))
                                    break
                                tmp_row += delta_row
                                tmp_col += delta_col

        return valid_moves

    def __is_valid_move(self, move_x, move_y):
        return (move_x, move_y) in self.__valid_moves

    def __make_a_move(self, move_row, move_col):
        if self.__is_valid_move(move_row, move_col):
            colour = "w" if self.__player == 0 else "b"
            new_board = self.__get_dcboard() # we have to use "deep" copy
            new_board[move_row][move_col] = colour # move
            neighbours =[]
            for row_idx in range(max(0,move_row-1),min(move_row+2,8)):
                for col_idx in range(max(0,move_col-1),min(move_col+2,8)):
                    if new_board[row_idx][col_idx] != None:
                        neighbours.append((row_idx,col_idx))
            switch_discs = [] # collect tiles for switch
            for neighbour in neighbours:
                neigh_row = neighbour[0]
                neigh_col = neighbour[1]
                if new_board[neigh_row][neigh_col] != colour:
                    line = []
                    delta_row = neigh_row - move_row
                    delta_col = neigh_col - move_col
                    tmp_row = neigh_row
                    tmp_col = neigh_col
                    while 0 <= tmp_row <= 7 and 0 <= tmp_col <= 7:
                        line.append((tmp_row,tmp_col))
                        if new_board[tmp_row][tmp_col] == None:
                            break
                        if new_board[tmp_row][tmp_col] == colour:
                            for disc in line:
                                switch_discs.append(disc)
                            break
                        tmp_row += delta_row
                        tmp_col += delta_col
            for disc in switch_discs:
                new_board[disc[0]][disc[1]] = colour
            return new_board
        # TODO: invalid move case
        return None

#   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---

    # PUBLIC METHODS

    def show_board(self, outline=False):
        # It can be showed on consloe
        if not self.__screen:
            print("   ",*sorted(self.__alphabet_coords.keys()))
            for row_idx in range(8):
                print(row_idx+1,"| ", end="")
                for col_idx in range(8):
                    act_field = self.__board[row_idx][col_idx]
                    if act_field:
                        print(act_field+" ", end="")
                    else:
                        ch = " "
                        if self.__is_valid_move(row_idx,col_idx) \
                           and self.__hint: ch = "-"
                        print(ch+" ", end="")
                print("|",row_idx+1)
            print("   ",*sorted(self.__alphabet_coords.keys()))
        else:
            try:
                # TODO: Make draw depend screen resolution
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

    def move(self):
        row_idx = col_idx = -1

        if not self.__screen: # Console
            # TODO: Use regexp for input
            field = input("Take one valid field please: ")
            row_idx = int(field[1])-1
            col_idx = self.__alphabet_coords[field[0]]
        else: # Screen
            # TODO: Handle click event
            pass

        assert(-1 < row_idx < 8 and -1 < col_idx < 8)
        self.__board = self.__make_a_move(row_idx, col_idx)
        self.__player = 1 - self.__player
        self.__valid_moves = self.__get_valid_moves()

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

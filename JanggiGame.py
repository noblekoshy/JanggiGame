# Author: Noble Koshy
# Date: 3/10/21
# Description: class named JanggiGame for playing an abstract board game called Janggi

import copy

class JanggiGame:
    """class named JanggiGame for playing an abstract board game called Janggi"""
    def __init__(self):
        """initialize data members"""
        self._game_state = "UNFINISHED"
        self._player_turn = "b" # blue starts
        self._players = ["b", "r"]
        self._player_in_check = " " # is either b or r when player in check
        # Initialize all pieces on board with starting locations.
        rCh1 = Chariot(self, "rCh1", [0, 0])
        rEl1 = Elephant(self, "rEl1", [0, 1])
        rHo1 = Horse(self, "rHo1", [0, 2])
        rGu1 = Guard(self, "rGu1", [0, 3])
        rGu2 = Guard(self, "rGu2", [0, 5])
        rEl2 = Elephant(self, "rEl2", [0, 6])
        rHo2 = Horse(self, "rHo2", [0, 7])
        rCh2 = Chariot(self, "rCh2", [0, 8])
        rGen = General(self, "rGen", [1, 4])
        rCa1 = Cannon(self, "rCa1", [2, 1])
        rCa2 = Cannon(self, "rCa2", [2, 7])
        rSo1 = Solider(self, "rSo1", [3,0])
        rSo2 = Solider(self, "rSo2", [3,2])
        rSo3 = Solider(self, "rSo3", [3,4])
        rSo4 = Solider(self, "rSo4", [3,6])
        rSo5 = Solider(self, "rSo5", [3,8])
        bCh1 = Chariot(self, "bCh1", [9, 0])
        bEl1 = Elephant(self, "bEl1", [9, 1])
        bHo1 = Horse(self, "bHo1", [9, 2])
        bGu1 = Guard(self, "bGu1", [9, 3])
        bGu2 = Guard(self, "bGu2", [9, 5])
        bEl2 = Elephant(self, "bEl2", [9, 6])
        bHo2 = Horse(self, "bHo2", [9, 7])
        bCh2 = Chariot(self, "bCh2", [9, 8])
        bGen = General(self, "bGen", [8, 4])
        bCa1 = Cannon(self, "bCa1", [7, 1])
        bCa2 = Cannon(self, "bCa2", [7, 7])
        bSo1 = Solider(self, "bSo1", [6, 0])
        bSo2 = Solider(self, "bSo2", [6, 2])
        bSo3 = Solider(self, "bSo3", [6, 4])
        bSo4 = Solider(self, "bSo4", [6, 6])
        bSo5 = Solider(self, "bSo5", [6, 8])

        # 2D list used to represent the board. None elements represent blank squares.
        self._board = [[rCh1, rEl1, rHo1, rGu1, None, rGu2, rEl2, rHo2, rCh2],
                       [None, None, None, None, rGen, None, None, None, None],
                       [None, rCa1, None, None, None, None, None, rCa2, None],
                       [rSo1, None, rSo2, None, rSo3, None, rSo4, None, rSo5],
                       [None, None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None, None],
                       [bSo1, None, bSo2, None, bSo3, None, bSo4, None, bSo5],
                       [None, bCa1, None, None, None, None, None, bCa2, None],
                       [None, None, None, None, bGen, None, None, None, None],
                       [bCh1, bEl1, bHo1, bGu1, None, bGu2, bEl2, bHo2, bCh2],
                       ]

        # lopp through board and get possible moves from starting location for all the pieces
        for row in self._board:
            for square in row:
                if square is not None:
                    square.set_possible_moves(square.get_row(), square.get_col())

    def get_board(self):
        """get board"""
        return self._board

    def set_board(self, board):
        """set board (input is a board list)"""
        self._board = board

    def find_piece_from_name(self, name):
        """find a piece on the board. IE find bGen. Return location (row,col)"""
        for row in self._board:
            for square in row:
                if square is not None and square.get_name() == name:
                    return square.get_location()
        print("piece not found")

    def get_square(self, row, column):
        """get the item in a square from the board"""
        return self._board[row][column]

    def set_square(self, row, column, item):
        """set the item in a square from the board"""
        self._board[row][column] = item

    def algebraic_to_board_notation(self, algebraic_notation):
        """convert algebraic notation to board list notation"""
        # convert letter from algebraic notation to column number (list index, starts at 0)
        column = ord(algebraic_notation[0]) - 97
        # convert number from algebraic notation to row number (list index, starts at 0)
        row = int(algebraic_notation[1:]) - 1
        board_index = [row, column]
        return board_index

    def print_board(self):
        """print board in readable format"""
        for i in self._board:
            for j in i:
                if j:
                    print(j.get_name(), end="|")
                else:
                    print("    ", end="|")
            print()

    def get_game_state(self):
        """returns one of these values, depending on the game state: 'UNFINISHED' or 'RED_WON' or 'BLUE_WON'."""
        return self._game_state

    def set_game_state(self, winner):
        """set game state to winner"""
        if winner == "r":
            self._game_state = "RED_WON"
        elif winner == "b":
            self._game_state = "BLUE_WON"

    def get_player_turn(self):
        """returns player currently on their turn."""
        return self._player_turn

    def get_player_waiting(self):
        """return player not on their turn"""
        # Use list comprehension to find other player. Return slice of single element list.
        return [i for i in self._players if i != self._player_turn][0]

    def change_turn(self):
        """change turn to the other player"""
        # Use list comprehension to find other player. Return slice of single element list.
        self._player_turn = self.get_player_waiting()

    def is_in_check(self, player):
        """
        takes as a parameter either 'red' or 'blue' and returns True if that player is in check,
        but returns False otherwise.
        """
        if self._player_in_check in player:
            return True
        else:
            return False

    def make_move(self, from_location, to_location):
        """takes two parameters - strings that represent the square to move from and the square to move to"""
        # return false is it is an invalid move
        # assume from and to locations are on the board
        # save a deep copy of the current board
        board_before_move = copy.deepcopy(self._board)
        player = self.get_player_turn()
        opponent = self.get_player_waiting()

        # if the game has already been won
        if self._game_state != "UNFINISHED":
            return False
        # If a player might decides to pass their turn when their general is in check, return false
        if self._player_in_check == self._player_turn and from_location == to_location:
            print("cant pass your turn. you are in check")
            return False
        # if your from and to are the same and you are not in check, then you pass your the turn
        if from_location == to_location:
            self.change_turn()
            print("pass turn")
            return True
        # convert algebraic notation to board notation [row, col]
        from_board = self.algebraic_to_board_notation(from_location)
        from_row = from_board[0]
        from_col = from_board[1]
        to_board = self.algebraic_to_board_notation(to_location)
        to_row = to_board[0]
        to_col = to_board[1]
        # get object at that board location
        from_object = self.get_square(from_row, from_col)
        to_object = self.get_square(to_row, to_col)
        # if the from square is empty
        if from_object is None:
            return False
        # If the square being moved from does not contain a piece belonging to the player whose turn it is,
        if from_object.get_color() != player:
            print(f"Not your turn. Tried {from_object.get_name()} from:{from_location} to: {to_location}")
            return False
        # if the to square contains your own piece
        if to_object is not None and to_object.get_color() == player:
            print(f"Cant capture own piece.Tried {from_object.get_name()} from:{from_location} to: {to_location}")
            return False
        # if the indicated move is not legal for the piece's movement range
        if not from_object.valid_move(from_row, from_col, to_row, to_col):
            print(f"Out of movement range.Tried {from_object.get_name()} from:{from_location} to: {to_location}")
            return False

        # Move (copy) piece to end location
        print(f"Moving {from_object.get_name()} from:{from_location} to: {to_location}")
        # update location data and possible moves in piece object
        from_object.set_location(to_row, to_col)
        from_object.set_possible_moves(to_row, to_col)

        # update board square
        self.set_square(to_row, to_col, from_object)
        # Remove piece from start location
        self.set_square(from_row, from_col, None)

        # check and check mate procedures:
        #  The player's move should not put/leave their general in check
        player_possible_moves = []
        opponent_possible_moves = []
        opponent_pieces = []
        # get location of the generals
        opponent_gen_loc = self.find_piece_from_name(opponent + "Gen")
        player_gen_loc = self.find_piece_from_name(player + "Gen")
        # go through board. See possible moves for the current player and opponent
        for row in self._board:
            for square in row:
                if square is not None:
                    square.set_possible_moves(square.get_row(), square.get_col())
                    if square.get_color() == opponent:
                        opponent_possible_moves.extend(square.get_possible_moves())
                        opponent_pieces.append(square)
                    elif square.get_color() == player:
                        player_possible_moves.extend(square.get_possible_moves())
        if player_gen_loc in opponent_possible_moves:
            print(f"{player} cant make this move, it put/leaves their gen in check")
            # UNDO BOARD MOVE
            # restore board to what it was before the move
            self.set_board(board_before_move)
            return False
        elif player_gen_loc not in opponent_possible_moves and player == self._player_in_check:
            print(f"{player}: was taken out of check")
            self._player_in_check = " "

        # check if the opponent is in check now
        if opponent_gen_loc in player_possible_moves:
            print(f"{opponent} is in check")
            self._player_in_check = opponent
            # check if opponent can move out of check. If they cannot then it is checkmate
            # go through possible moves for each of the opponent pieces
            test_moves = []
            for piece in opponent_pieces:
                piece.set_possible_moves(piece.get_row(), piece.get_col())
                piece_possible_moves = piece.get_possible_moves()
                piece_row = piece.get_row()
                piece_col = piece.get_col()
                for move in piece_possible_moves:
                    test_moves.append(self.test_move(piece, piece_row, piece_col, move[0], move[1]))
            if True not in test_moves:
                # player cant get out of check, thus checkmate
                print("checkmate")
                self.set_game_state(player)

        self.change_turn()
        return True

    def test_move(self, piece, from_row, from_col, to_row, to_col):
        """test a move to see if opponent can get out of check"""
        # save a deep copy of the current board
        board_before_test_move = copy.deepcopy(self._board)
        opponent = self.get_player_waiting()
        # if to location is off the board, return false
        if to_row < 0 or to_row > 9:
            return False
        if to_col < 0 or to_col > 8:
            return False
        # get object at that board location
        from_object = self.get_square(from_row, from_col)
        to_object = self.get_square(to_row, to_col)
        if from_object is None:
            print(f'{from_row}, {from_col} square is empty')
            return False
        # if the to square contains your own (this case the opponent's) piece. cant capture your own piece
        if to_object is not None and to_object.get_color() == opponent:
            return False
        # update location data and possible moves in piece object
        from_object.set_location(to_row, to_col)
        from_object.set_possible_moves(to_row, to_col)
        # update board square
        self.set_square(to_row, to_col, from_object)
        # Remove piece from start location
        self.set_square(from_row, from_col, None)

        player_possible_moves = []
        # go through board. See possible moves for the current player
        for row in self._board:
            for square in row:
                if square is not None:
                    square.set_possible_moves(square.get_row(), square.get_col())
                    if square.get_color() == self._player_turn:
                        player_possible_moves.extend(square.get_possible_moves())
        opponent_gen_loc = self.find_piece_from_name(opponent + "Gen")
        if opponent_gen_loc not in player_possible_moves:
            # player can get out of check
            print(f'{piece.get_name()} to {to_row},{to_col} gets you out of check')
            self.set_board(board_before_test_move)
            return True

        # revert board back
        self.set_board(board_before_test_move)
        return False


class Piece:
    """abstract class to represent a piece on the board"""
    def __init__(self, janggi_game, name, location):
        """initialize data members"""
        self._name = name # example rCh1
        self._color = name[0]
        self._piece_type = name[1:3]
        self._location = location # use list index format [row,col]
        self._row = location[0]
        self._col = location[1]
        self._possible_moves = []
        # pass janggi class as data member for the piece class
        # so piece can access the board from janggi class
        self._janggi_game = janggi_game

    def get_name(self):
        """get name"""
        return self._name

    def get_color(self):
        """get color"""
        return self._color

    def get_piece_type(self):
        """get piece type"""
        return self._piece_type

    def get_location(self):
        """get location"""
        return self._location

    def get_row(self):
        """get row"""
        return self._row

    def get_col(self):
        """get col"""
        return self._col

    def set_location(self, row, col):
        """set location"""
        self._location = [row, col]
        self._row = row
        self._col = col

    def get_possible_moves(self):
        """get possible moves"""
        return self._possible_moves

    def set_possible_moves(self, from_row, from_col):
        """set possible moves at the given location"""
        # we define in the child classes
        pass


class Solider(Piece):
    """Child of Piece class. Represent Solider piece"""
    def __init__(self, janggi_game, name, location):
        Piece.__init__(self, janggi_game, name, location)

    def set_possible_moves(self, from_row, from_col):
        """generate possible moves at given location"""
        # red piece can only move down or side to side
        # blue piece can only move up or side to side
        # can move diagonal forward in fortress
        # clear old possible moves
        self._possible_moves.clear()
        up_row = from_row - 1
        down_row = from_row + 1
        left_col = from_col - 1
        right_col = from_col + 1
        if self._color == "r":
            # can move down (+1) or side to side (-1,+1)
            if from_row < 9:
                self._possible_moves.append([down_row, from_col])
            if from_col > 0:
                self._possible_moves.append([from_row, left_col])
            if from_col < 8:
                self._possible_moves.append([from_row, right_col])
            # if in enemy fort can move diagonal
            if [from_row, from_col] == [7, 3]:
                self._possible_moves.append([8, 4])
            if [from_row, from_col] == [8, 4]:
                self._possible_moves.append([9, 3])
                self._possible_moves.append([9, 5])
            if [from_row, from_col] == [7, 5]:
                self._possible_moves.append([8, 4])

        if self._color == 'b':
            # can move up (row-1) or side to side (col-1,col+1)
            if from_row > 0:
                self._possible_moves.append([up_row, from_col])
            if from_col > 0:
                self._possible_moves.append([from_row, left_col])
            if from_col < 8:
                self._possible_moves.append([from_row, right_col])
            # if in enemy fort can move diagonal
            if [from_row, from_col] == [2, 3]:
                self._possible_moves.append([1, 4])
            if [from_row, from_col] == [1, 4]:
                self._possible_moves.append([0, 3])
                self._possible_moves.append([0, 5])
            if [from_row, from_col] == [2, 5]:
                self._possible_moves.append([1, 4])

    def valid_move(self, from_row, from_col, to_row, to_col):
        """return true if valid move"""
        # clear possible moves
        self._possible_moves.clear()
        # red piece can only move down or side to side
        # blue piece can only move up or side to side
        # can move diagonal forward in fortress
        # cannot capture same color pieces
        if self._color == "r":
            # can move down (+1) or side to side (-1,+1)
            self._possible_moves = [[from_row + 1, from_col],
                                    [from_row, from_col - 1],
                                    [from_row, from_col + 1]
                                    ]
            # if in enemy fort can move diagonal
            if [from_row, from_col] == [7, 3]:
                self._possible_moves.append([8, 4])
            if [from_row, from_col] == [8, 4]:
                self._possible_moves.append([9, 3])
                self._possible_moves.append([9, 5])
            if [from_row, from_col] == [7, 5]:
                self._possible_moves.append([8, 4])

        if self._color == 'b':
            # can move up (row-1) or side to side (col-1,col+1)
            self._possible_moves = [[from_row - 1, from_col],
                                   [from_row, from_col - 1],
                                   [from_row, from_col + 1]
                                   ]
            # if in enemy fort can move diagonal
            if [from_row, from_col] == [2,3]:
                self._possible_moves.append([1,4])
            if [from_row, from_col] == [1,4]:
                self._possible_moves.append([0,3])
                self._possible_moves.append([0,5])
            if [from_row, from_col] == [2,5]:
                self._possible_moves.append([1,4])

        if [to_row, to_col] in self._possible_moves:
            return True
        else:
            return False


class Chariot(Piece):
    """Child of piece class. Represent Chariot piece"""
    def __init__(self, janggi_game, name, location):
        Piece.__init__(self, janggi_game, name, location)

    def set_possible_moves(self, from_row, from_col):
        """generate possible moves at given location"""
        # clear old possible moves
        self._possible_moves.clear()
        # can move up/down and side to side
        # check up
        up_row = from_row - 1
        # keep going til you hit a piece
        while up_row >= 0 and self._janggi_game.get_square(up_row, from_col) is None:
            self._possible_moves.append([up_row, from_col])
            up_row -= 1
        # if the next square up is on the board, test if it is your opponent's piece
        if up_row >= 0:
            if self._janggi_game.get_square(up_row, from_col).get_color() != self.get_color():
                # this is enemy piece. you can capture it
                self._possible_moves.append([up_row, from_col])
        # check down
        down_row = from_row + 1
        # keep going til you hit a piece
        while down_row <= 9 and self._janggi_game.get_square(down_row, from_col) is None:
            self._possible_moves.append([down_row, from_col])
            down_row += 1
        # if the next square down is on the board, test if it is your opponent's piece
        if down_row <= 9:
            if self._janggi_game.get_square(down_row, from_col).get_color() != self.get_color():
                # this is enemy piece. you can capture it
                self._possible_moves.append([down_row, from_col])

        # check left side
        left_col = from_col - 1
        # keep going til you hit a piece
        while left_col >= 0 and self._janggi_game.get_square(from_row, left_col) is None:
            self._possible_moves.append([from_row, left_col])
            left_col -= 1
        # if the next square left is on the board, test if it is your opponent's piece
        if left_col >= 0:
            if self._janggi_game.get_square(from_row, left_col).get_color() != self.get_color():
                # this is enemy piece. you can capture it
                self._possible_moves.append([from_row, left_col])

        # check right side
        right_col = from_col + 1
        # keep going til you hit a piece
        while right_col <= 8 and self._janggi_game.get_square(from_row, right_col) is None:
            self._possible_moves.append([from_row, right_col])
            right_col += 1
        # if the next square right is on the board, test if it is your opponent's piece
        if right_col <= 8:
            if self._janggi_game.get_square(from_row, right_col).get_color() != self.get_color():
                # this is enemy piece. you can capture it
                self._possible_moves.append([from_row, right_col])

        # add palace conditions
        # consider condition if a piece is in the way of double diagonal movement
        if [from_row, from_col] == [0, 3]:
            self._possible_moves.append([1, 4])
            if self._janggi_game.get_square(1, 4) is None:
                self._possible_moves.append([2, 5])
        if [from_row, from_col] == [0, 5]:
            self._possible_moves.append([1, 4])
            if self._janggi_game.get_square(1, 4) is None:
                self._possible_moves.append([2, 3])
        if [from_row, from_col] == [1, 4]:
            self._possible_moves.extend([[0, 3], [0, 5], [2, 3], [2, 5]])
        if [from_row, from_col] == [2, 3]:
            self._possible_moves.append([1, 4])
            if self._janggi_game.get_square(1, 4) is None:
                self._possible_moves.append([0, 5])
        if [from_row, from_col] == [2, 5]:
            self._possible_moves.append([1, 4])
            if self._janggi_game.get_square(1, 4) is None:
                self._possible_moves.append([0, 3])
        if [from_row, from_col] == [7, 3]:
            self._possible_moves.append([8, 4])
            if self._janggi_game.get_square(8, 4) is None:
                self._possible_moves.append([9, 5])
        if [from_row, from_col] == [7, 5]:
            self._possible_moves.append([8, 4])
            if self._janggi_game.get_square(8, 4) is None:
                self._possible_moves.append([9, 3])
        if [from_row, from_col] == [8, 4]:
            self._possible_moves.extend([[7, 3], [7, 5], [9, 3], [9, 5]])
        if [from_row, from_col] == [9, 3]:
            self._possible_moves.append([8, 4])
            if self._janggi_game.get_square(8, 4) is None:
                self._possible_moves.append([7, 5])
        if [from_row, from_col] == [9, 5]:
            self._possible_moves.append([8, 4])
            if self._janggi_game.get_square(8, 4) is None:
                self._possible_moves.append([7, 3])

    def valid_move(self, from_row, from_col, to_row, to_col):
        """return true if valid move for the piece"""
        # clear old possible moves
        self._possible_moves.clear()
        # can move up/down and side to side
        # check up
        up_row = from_row - 1
        # keep going til you hit a piece
        while up_row >= 0 and self._janggi_game.get_square(up_row, from_col) is None:
            self._possible_moves.append([up_row, from_col])
            up_row -= 1
        # if the next square up is on the board, test if it is your opponent's piece
        if up_row >= 0:
            if self._janggi_game.get_square(up_row, from_col).get_color() != self.get_color():
                # this is enemy piece. you can capture it
                self._possible_moves.append([up_row, from_col])
        # check down
        down_row = from_row + 1
        # keep going til you hit a piece
        while down_row <= 9 and self._janggi_game.get_square(down_row, from_col) is None:
            self._possible_moves.append([down_row, from_col])
            down_row += 1
        # if the next square down is on the board, test if it is your opponent's piece
        if down_row <= 9:
            if self._janggi_game.get_square(down_row, from_col).get_color() != self.get_color():
                # this is enemy piece. you can capture it
                self._possible_moves.append([down_row, from_col])

        # check left side
        left_col = from_col - 1
        # keep going til you hit a piece
        while left_col >= 0 and self._janggi_game.get_square(from_row, left_col) is None:
            self._possible_moves.append([from_row, left_col])
            left_col -= 1
        # if the next square left is on the board, test if it is your opponent's piece
        if left_col >= 0:
            if self._janggi_game.get_square(from_row, left_col).get_color() != self.get_color():
                # this is enemy piece. you can capture it
                self._possible_moves.append([from_row, left_col])

        # check right side
        right_col = from_col + 1
        # keep going til you hit a piece
        while right_col <= 8 and self._janggi_game.get_square(from_row, right_col) is None:
            self._possible_moves.append([from_row, right_col])
            right_col += 1
        # if the next square right is on the board, test if it is your opponent's piece
        if right_col <= 8:
            if self._janggi_game.get_square(from_row, right_col).get_color() != self.get_color():
                # this is enemy piece. you can capture it
                self._possible_moves.append([from_row, right_col])

        # add palace conditions
        # consider condition if a piece is in the way of double diagonal movement
        if [from_row, from_col] == [0, 3]:
            self._possible_moves.append([1, 4])
            if self._janggi_game.get_square(1, 4) is None:
                self._possible_moves.append([2, 5])
        if [from_row, from_col] == [0, 5]:
            self._possible_moves.append([1, 4])
            if self._janggi_game.get_square(1, 4) is None:
                self._possible_moves.append([2, 3])
        if [from_row, from_col] == [1, 4]:
            self._possible_moves.extend([[0, 3], [0, 5], [2, 3], [2, 5]])
        if [from_row, from_col] == [2, 3]:
            self._possible_moves.append([1, 4])
            if self._janggi_game.get_square(1, 4) is None:
                self._possible_moves.append([0, 5])
        if [from_row, from_col] == [2, 5]:
            self._possible_moves.append([1, 4])
            if self._janggi_game.get_square(1, 4) is None:
                self._possible_moves.append([0, 3])
        if [from_row, from_col] == [7, 3]:
            self._possible_moves.append([8, 4])
            if self._janggi_game.get_square(8, 4) is None:
                self._possible_moves.append([9, 5])
        if [from_row, from_col] == [7, 5]:
            self._possible_moves.append([8, 4])
            if self._janggi_game.get_square(8, 4) is None:
                self._possible_moves.append([9, 3])
        if [from_row, from_col] == [8, 4]:
            self._possible_moves.extend([[7, 3], [7, 5], [9, 3], [9, 5]])
        if [from_row, from_col] == [9, 3]:
            self._possible_moves.append([8, 4])
            if self._janggi_game.get_square(8, 4) is None:
                self._possible_moves.append([7, 5])
        if [from_row, from_col] == [9, 5]:
            self._possible_moves.append([8, 4])
            if self._janggi_game.get_square(8, 4) is None:
                self._possible_moves.append([7, 3])

        if [to_row, to_col] in self._possible_moves:
            return True
        else:
            return False


class Elephant(Piece):
    """Child of Piece class. Represents Elephant piece."""
    def __init__(self, janggi_game, name, location):
        Piece.__init__(self, janggi_game, name, location)

    def set_possible_moves(self, from_row, from_col):
        """generate all possible moves for the piece at the given location"""
        # clear possible moves
        self._possible_moves.clear()
        # 1 space up, down or sideways then 2 space outward diagonally
        # can be blocked as well

        # Check up motion
        up_row = from_row - 1
        # check if on board (check greater than 2 b/c we still have to move 2 row up later)
        if up_row >= 2 and self._janggi_game.get_square(up_row, from_col) is None:
            # go up another row and check the outer diagonals paths
            up_row -= 1
            # left diagonal
            up_left_col = from_col - 1
            # check if on board (check greater than 1 b/c we still have to move 1 col left later) and diagonal path
            if up_left_col >= 1 and self._janggi_game.get_square(up_row, up_left_col) is None:
                # move diagonal again
                up_left_row = up_row - 1
                up_left_col -= 1
                self._possible_moves.append([up_left_row, up_left_col])

            # right diagonal
            up_right_col = from_col + 1
            # check if col on the board
            if up_right_col <= 7 and self._janggi_game.get_square(up_row, up_right_col) is None:
                up_right_row = up_row - 1
                up_right_col += 1
                self._possible_moves.append([up_right_row, up_right_col])

        # Check down motion
        down_row = from_row + 1
        if down_row <= 7 and self._janggi_game.get_square(down_row, from_col) is None:
            # go down another row and check the outer diagonals path
            down_row += 1
            # left diagonal
            down_left_col = from_col - 1
            # check if col on the board and diagonal path
            if down_left_col >= 1 and self._janggi_game.get_square(down_row, down_left_col) is None:
                # move diagonal again
                down_left_row = down_row + 1
                down_left_col -= 1
                self._possible_moves.append([down_left_row, down_left_col])

            # right diagonal
            down_right_col = from_col + 1
            # check if col on the board and diagonal path
            if down_right_col <= 8 and self._janggi_game.get_square(down_row, down_right_col) is None:
                # move diagonal again
                down_right_row = down_row + 1
                down_right_col += 1
                self._possible_moves.append([down_right_row, down_right_col])

        # Check left motion
        left_col = from_col - 1
        if left_col >= 2 and self._janggi_game.get_square(from_row, left_col) is None:
            # go left another col and check the outer diagonals path
            left_col -= 1
            # up diagonal
            left_up_row = from_row - 1
            # check if row on the board and diagonal path
            if left_up_row >= 1 and self._janggi_game.get_square(left_up_row, left_col) is None:
                # move diagonal again
                left_up_col = left_col - 1
                left_up_row -= 1
                self._possible_moves.append([left_up_row, left_up_col])
            # down diagonal
            left_down_row = from_row + 1
            # check if row on the board and diagonal path
            if left_down_row <= 8 and self._janggi_game.get_square(left_down_row, left_col) is None:
                # move diagonal again
                left_down_col = left_col - 1
                left_down_row += 1
                self._possible_moves.append([left_down_row, left_down_col])

        # Check right motion
        right_col = from_col + 1
        if right_col <= 6 and self._janggi_game.get_square(from_row, right_col) is None:
            # go right another col and check the outer diagonals path
            right_col += 1
            # up diagonal
            right_up_row = from_row - 1
            # check if row on the board and diagonal path
            if right_up_row >= 1 and self._janggi_game.get_square(right_up_row, right_col) is None:
                # move diagonal again
                right_up_col = right_col + 1
                right_up_row -= 1
                self._possible_moves.append([right_up_row, right_up_col])
            # down diagonal
            right_down_row = from_row + 1
            # check if row on the board and diagonal path
            if right_down_row <= 8 and self._janggi_game.get_square(right_down_row, right_col):
                # move diagonal again
                right_down_col = right_col + 1
                right_down_row += 1
                self._possible_moves.append([right_down_row, right_down_col])

    def valid_move(self, from_row, from_col, to_row, to_col):
        """return true if valid move for the piece"""
        # clear possible moves
        self._possible_moves.clear()
        # 1 space up, down or sideways then 2 space outward diagonally
        # can be blocked as well

        # Check up motion
        up_row = from_row - 1
        # check if on board (check greater than 2 b/c we still have to move 2 row up later)
        if up_row >= 2 and self._janggi_game.get_square(up_row, from_col) is None:
            # go up another row and check the outer diagonals paths
            up_row -= 1
            # left diagonal
            up_left_col = from_col - 1
            # check if on board (check greater than 1 b/c we still have to move 1 col left later) and diagonal path
            if up_left_col >= 1 and self._janggi_game.get_square(up_row, up_left_col) is None:
                # move diagonal again
                up_left_row = up_row - 1
                up_left_col -= 1
                self._possible_moves.append([up_left_row, up_left_col])

            # right diagonal
            up_right_col = from_col + 1
            # check if col on the board
            if up_right_col <= 7 and self._janggi_game.get_square(up_row, up_right_col) is None:
                up_right_row = up_row - 1
                up_right_col += 1
                self._possible_moves.append([up_right_row, up_right_col])

        # Check down motion
        down_row = from_row + 1
        if down_row <= 7 and self._janggi_game.get_square(down_row, from_col) is None:
            # go down another row and check the outer diagonals path
            down_row += 1
            # left diagonal
            down_left_col = from_col - 1
            # check if col on the board and diagonal path
            if down_left_col >= 1 and self._janggi_game.get_square(down_row, down_left_col) is None:
                # move diagonal again
                down_left_row = down_row + 1
                down_left_col -= 1
                self._possible_moves.append([down_left_row, down_left_col])

            # right diagonal
            down_right_col = from_col + 1
            # check if col on the board and diagonal path
            if down_right_col <= 8 and self._janggi_game.get_square(down_row, down_right_col) is None:
                # move diagonal again
                down_right_row = down_row + 1
                down_right_col += 1
                self._possible_moves.append([down_right_row, down_right_col])

        # Check left motion
        left_col = from_col - 1
        if left_col >= 2 and self._janggi_game.get_square(from_row, left_col) is None:
            # go left another col and check the outer diagonals path
            left_col -= 1
            # up diagonal
            left_up_row = from_row - 1
            # check if row on the board and diagonal path
            if left_up_row >= 1 and self._janggi_game.get_square(left_up_row, left_col) is None:
                # move diagonal again
                left_up_col = left_col - 1
                left_up_row -= 1
                self._possible_moves.append([left_up_row, left_up_col])
            # down diagonal
            left_down_row = from_row + 1
            # check if row on the board and diagonal path
            if left_down_row <= 8 and self._janggi_game.get_square(left_down_row, left_col) is None:
                # move diagonal again
                left_down_col = left_col - 1
                left_down_row += 1
                self._possible_moves.append([left_down_row, left_down_col])

        # Check right motion
        right_col = from_col + 1
        if right_col <= 6 and self._janggi_game.get_square(from_row, right_col) is None:
            # go right another col and check the outer diagonals path
            right_col += 1
            # up diagonal
            right_up_row = from_row - 1
            # check if row on the board and diagonal path
            if right_up_row >= 1 and self._janggi_game.get_square(right_up_row, right_col) is None:
                # move diagonal again
                right_up_col = right_col + 1
                right_up_row -= 1
                self._possible_moves.append([right_up_row, right_up_col])
            # down diagonal
            right_down_row = from_row + 1
            # check if row on the board and diagonal path
            if right_down_row <= 8 and self._janggi_game.get_square(right_down_row, right_col):
                # move diagonal again
                right_down_col = right_col + 1
                right_down_row += 1
                self._possible_moves.append([right_down_row, right_down_col])

        if [to_row, to_col] in self._possible_moves:
            return True
        else:
            return False


class Horse(Piece):
    """Child of Piece class. Represents Horse piece"""
    def __init__(self, janggi_game, name, location):
        Piece.__init__(self, janggi_game, name, location)

    def set_possible_moves(self, from_row, from_col):
        """generate all possible moves for the piece at the given location"""
        # clear possible moves
        self._possible_moves.clear()
        # 1 space up, down or sideways then 1 space outward diagonally
        # can be blocked if cant move up/down or sideways

        # Check up motion
        up_row = from_row - 1
        # check if on board (check greater than 1 b/c we still have to move 1 row up later)
        if up_row >= 1 and self._janggi_game.get_square(up_row, from_col) is None:
            # go up another row and check the outer diagonals
            up_row -= 1
            # left diagonal
            up_left_col = from_col - 1
            # check if col on the board
            if up_left_col >= 0:
                self._possible_moves.append([up_row, up_left_col])
            # right diagonal
            up_right_col = from_col + 1
            # check if col on the board
            if up_right_col <= 8:
                self._possible_moves.append([up_row, up_right_col])

        # Check down motion
        down_row = from_row + 1
        if down_row <= 8 and self._janggi_game.get_square(down_row, from_col) is None:
            # go down another row and check the outer diagonals
            down_row += 1
            # left diagonal
            down_left_col = from_col - 1
            # check if col on the board
            if down_left_col >= 0:
                self._possible_moves.append([down_row, down_left_col])
            # right diagonal
            down_right_col = from_col + 1
            # check if col on the board
            if down_right_col <= 8:
                self._possible_moves.append([down_row, down_right_col])

        # Check left motion
        left_col = from_col - 1
        if left_col >= 1 and self._janggi_game.get_square(from_row, left_col) is None:
            # go left another col and check the outer diagonals
            left_col -= 1
            # up diagonal
            left_up_row = from_row - 1
            # check if row on the board
            if left_up_row >= 0:
                self._possible_moves.append([left_up_row, left_col])
            # down diagonal
            left_down_row = from_row + 1
            # check if row on the board
            if left_down_row <= 9:
                self._possible_moves.append([left_down_row, left_col])

        # Check right motion
        right_col = from_col + 1
        if right_col <= 7 and self._janggi_game.get_square(from_row, right_col) is None:
            # go right another col and check the outer diagonals
            right_col += 1
            # up diagonal
            right_up_row = from_row - 1
            # check if row on the board
            if right_up_row >= 0:
                self._possible_moves.append([right_up_row, right_col])
            # down diagonal
            right_down_row = from_row + 1
            # check if row on the board
            if right_down_row <= 9:
                self._possible_moves.append([right_down_row, right_col])

    def valid_move(self, from_row, from_col, to_row, to_col):
        """return true if valid move"""
        # clear possible moves
        self._possible_moves.clear()
        # 1 space up, down or sideways then 1 space outward diagonally
        # can be blocked if cant move up/down or sideways

        # Check up motion
        up_row = from_row - 1
        # check if on board (check greater than 1 b/c we still have to move 1 row up later)
        if up_row >= 1 and self._janggi_game.get_square(up_row, from_col) is None:
            # go up another row and check the outer diagonals
            up_row -= 1
            # left diagonal
            up_left_col = from_col - 1
            # check if col on the board
            if up_left_col >= 0:
                self._possible_moves.append([up_row, up_left_col])
            # right diagonal
            up_right_col = from_col + 1
            # check if col on the board
            if up_right_col <= 8:
                self._possible_moves.append([up_row, up_right_col])

        # Check down motion
        down_row = from_row + 1
        if down_row <= 8 and self._janggi_game.get_square(down_row, from_col) is None:
            # go down another row and check the outer diagonals
            down_row += 1
            # left diagonal
            down_left_col = from_col - 1
            # check if col on the board
            if down_left_col >= 0:
                self._possible_moves.append([down_row, down_left_col])
            # right diagonal
            down_right_col = from_col + 1
            # check if col on the board
            if down_right_col <= 8:
                self._possible_moves.append([down_row, down_right_col])

        # Check left motion
        left_col = from_col - 1
        if left_col >= 1 and self._janggi_game.get_square(from_row, left_col) is None:
            # go left another col and check the outer diagonals
            left_col -= 1
            # up diagonal
            left_up_row = from_row - 1
            # check if row on the board
            if left_up_row >= 0:
                self._possible_moves.append([left_up_row, left_col])
            # down diagonal
            left_down_row = from_row + 1
            # check if row on the board
            if left_down_row <= 9:
                self._possible_moves.append([left_down_row, left_col])

        # Check right motion
        right_col = from_col + 1
        if right_col <= 7 and self._janggi_game.get_square(from_row, right_col) is None:
            # go right another col and check the outer diagonals
            right_col += 1
            # up diagonal
            right_up_row = from_row - 1
            # check if row on the board
            if right_up_row >= 0:
                self._possible_moves.append([right_up_row, right_col])
            # down diagonal
            right_down_row = from_row + 1
            # check if row on the board
            if right_down_row <= 9:
                self._possible_moves.append([right_down_row, right_col])

        if [to_row, to_col] in self._possible_moves:
            return True
        else:
            return False


class Guard(Piece):
    """Child of piece class. Represents a Guard piece."""
    def __init__(self, janggi_game, name, location):
        Piece.__init__(self, janggi_game, name, location)

    def set_possible_moves(self, from_row, from_col):
        """generate all possible moves for the piece at the given location"""
        # clear possible moves
        self._possible_moves.clear()
        # guards can only move in the palace
        if self._color == "r":
            # can move in the red palace
            if [from_row, from_col] == [0, 3]:
                self._possible_moves.extend([[0, 4], [1, 3], [1, 4]])
            if [from_row, from_col] == [0, 4]:
                self._possible_moves.extend([[0, 3], [0, 5], [1, 4]])
            if [from_row, from_col] == [0, 5]:
                self._possible_moves.extend([[0, 4], [1, 4], [1, 5]])
            if [from_row, from_col] == [1, 3]:
                self._possible_moves.extend([[0, 3], [1, 4], [2, 3]])
            if [from_row, from_col] == [1, 4]:
                self._possible_moves.extend([[0, 3], [0, 4], [0, 5], [1, 3], [1, 5], [2, 3], [2, 4], [2, 5]])
            if [from_row, from_col] == [1, 5]:
                self._possible_moves.extend([[0, 5], [1, 4], [2, 5]])
            if [from_row, from_col] == [2, 3]:
                self._possible_moves.extend([[1, 3], [1, 4], [2, 4]])
            if [from_row, from_col] == [2, 4]:
                self._possible_moves.extend([[1, 4], [2, 3], [2, 5]])
            if [from_row, from_col] == [2, 5]:
                self._possible_moves.extend([[1, 4], [1, 5], [2, 4]])
        if self._color == 'b':
            # can move in the blue palace
            if [from_row, from_col] == [7, 3]:
                self._possible_moves.extend([[7, 4], [8, 3], [8, 4]])
            if [from_row, from_col] == [7, 4]:
                self._possible_moves.extend([[7, 3], [7, 5], [8, 4]])
            if [from_row, from_col] == [7, 5]:
                self._possible_moves.extend([[7, 4], [8, 4], [8, 5]])
            if [from_row, from_col] == [8, 3]:
                self._possible_moves.extend([[7, 3], [8, 4], [9, 3]])
            if [from_row, from_col] == [8, 4]:
                self._possible_moves.extend([[7, 3], [7, 4], [7, 5], [8, 3], [8, 5], [9, 3], [9, 4], [9, 5]])
            if [from_row, from_col] == [8, 5]:
                self._possible_moves.extend([[7, 5], [8, 4], [9, 5]])
            if [from_row, from_col] == [9, 3]:
                self._possible_moves.extend([[8, 3], [8, 4], [9, 4]])
            if [from_row, from_col] == [9, 4]:
                self._possible_moves.extend([[8, 4], [9, 3], [9, 5]])
            if [from_row, from_col] == [9, 5]:
                self._possible_moves.extend([[8, 4], [8, 5], [9, 4]])

    def valid_move(self, from_row, from_col, to_row, to_col):
        """return true if valid move"""
        # clear possible moves
        self._possible_moves.clear()
        # guards can only move in the palace
        if self._color == "r":
            # can move in the red palace
            if [from_row, from_col] == [0, 3]:
                self._possible_moves.extend([[0, 4], [1, 3], [1, 4]])
            if [from_row, from_col] == [0, 4]:
                self._possible_moves.extend([[0, 3], [0, 5], [1, 4]])
            if [from_row, from_col] == [0, 5]:
                self._possible_moves.extend([[0, 4], [1, 4], [1, 5]])
            if [from_row, from_col] == [1, 3]:
                self._possible_moves.extend([[0, 3], [1, 4], [2, 3]])
            if [from_row, from_col] == [1, 4]:
                self._possible_moves.extend([[0, 3], [0, 4], [0, 5], [1, 3], [1, 5], [2, 3], [2, 4], [2, 5]])
            if [from_row, from_col] == [1, 5]:
                self._possible_moves.extend([[0, 5], [1, 4], [2, 5]])
            if [from_row, from_col] == [2, 3]:
                self._possible_moves.extend([[1, 3], [1, 4], [2, 4]])
            if [from_row, from_col] == [2, 4]:
                self._possible_moves.extend([[1, 4], [2, 3], [2, 5]])
            if [from_row, from_col] == [2, 5]:
                self._possible_moves.extend([[1, 4], [1, 5], [2, 4]])
        if self._color == 'b':
            # can move in the blue palace
            if [from_row, from_col] == [7, 3]:
                self._possible_moves.extend([[7, 4], [8, 3], [8, 4]])
            if [from_row, from_col] == [7, 4]:
                self._possible_moves.extend([[7, 3], [7, 5], [8, 4]])
            if [from_row, from_col] == [7, 5]:
                self._possible_moves.extend([[7, 4], [8, 4], [8, 5]])
            if [from_row, from_col] == [8, 3]:
                self._possible_moves.extend([[7, 3], [8, 4], [9, 3]])
            if [from_row, from_col] == [8, 4]:
                self._possible_moves.extend([[7, 3], [7, 4], [7, 5], [8, 3], [8, 5], [9, 3], [9, 4], [9, 5]])
            if [from_row, from_col] == [8, 5]:
                self._possible_moves.extend([[7, 5], [8, 4], [9, 5]])
            if [from_row, from_col] == [9, 3]:
                self._possible_moves.extend([[8, 3], [8, 4], [9, 4]])
            if [from_row, from_col] == [9, 4]:
                self._possible_moves.extend([[8, 4], [9, 3], [9, 5]])
            if [from_row, from_col] == [9, 5]:
                self._possible_moves.extend([[8, 4], [8, 5], [9, 4]])

        if [to_row, to_col] in self._possible_moves:
            return True
        else:
            return False


class General(Piece):
    """Child of piece class. Represents the general piece."""
    def __init__(self, janggi_game, name, location):
        Piece.__init__(self, janggi_game, name, location)

    def set_possible_moves(self, from_row, from_col):
        """generate all possible moves for the piece at the given location"""
        # clear possible moves
        self._possible_moves.clear()
        # guards can only move in the palace
        if self._color == "r":
            # can move in the red palace
            if [from_row, from_col] == [0, 3]:
                self._possible_moves.extend([[0, 4], [1, 3], [1, 4]])
            if [from_row, from_col] == [0, 4]:
                self._possible_moves.extend([[0, 3], [0, 5], [1, 4]])
            if [from_row, from_col] == [0, 5]:
                self._possible_moves.extend([[0, 4], [1, 4], [1, 5]])
            if [from_row, from_col] == [1, 3]:
                self._possible_moves.extend([[0, 3], [1, 4], [2, 3]])
            if [from_row, from_col] == [1, 4]:
                self._possible_moves.extend([[0, 3], [0, 4], [0, 5], [1, 3], [1, 5], [2, 3], [2, 4], [2, 5]])
            if [from_row, from_col] == [1, 5]:
                self._possible_moves.extend([[0, 5], [1, 4], [2, 5]])
            if [from_row, from_col] == [2, 3]:
                self._possible_moves.extend([[1, 3], [1, 4], [2, 4]])
            if [from_row, from_col] == [2, 4]:
                self._possible_moves.extend([[1, 4], [2, 3], [2, 5]])
            if [from_row, from_col] == [2, 5]:
                self._possible_moves.extend([[1, 4], [1, 5], [2, 4]])
        if self._color == 'b':
            # can move in the blue palace
            if [from_row, from_col] == [7, 3]:
                self._possible_moves.extend([[7, 4], [8, 3], [8, 4]])
            if [from_row, from_col] == [7, 4]:
                self._possible_moves.extend([[7, 3], [7, 5], [8, 4]])
            if [from_row, from_col] == [7, 5]:
                self._possible_moves.extend([[7, 4], [8, 4], [8, 5]])
            if [from_row, from_col] == [8, 3]:
                self._possible_moves.extend([[7, 3], [8, 4], [9, 3]])
            if [from_row, from_col] == [8, 4]:
                self._possible_moves.extend([[7, 3], [7, 4], [7, 5], [8, 3], [8, 5], [9, 3], [9, 4], [9, 5]])
            if [from_row, from_col] == [8, 5]:
                self._possible_moves.extend([[7, 5], [8, 4], [9, 5]])
            if [from_row, from_col] == [9, 3]:
                self._possible_moves.extend([[8, 3], [8, 4], [9, 4]])
            if [from_row, from_col] == [9, 4]:
                self._possible_moves.extend([[8, 4], [9, 3], [9, 5]])
            if [from_row, from_col] == [9, 5]:
                self._possible_moves.extend([[8, 4], [8, 5], [9, 4]])

    def valid_move(self, from_row, from_col, to_row, to_col):
        """return true if valid move"""
        # clear possible moves
        self._possible_moves.clear()
        # guards can only move in the palace
        if self._color == "r":
            # can move in the red palace
            if [from_row, from_col] == [0, 3]:
                self._possible_moves.extend([[0, 4], [1, 3], [1, 4]])
            if [from_row, from_col] == [0, 4]:
                self._possible_moves.extend([[0, 3], [0, 5], [1, 4]])
            if [from_row, from_col] == [0, 5]:
                self._possible_moves.extend([[0, 4], [1, 4], [1, 5]])
            if [from_row, from_col] == [1, 3]:
                self._possible_moves.extend([[0, 3], [1, 4], [2, 3]])
            if [from_row, from_col] == [1, 4]:
                self._possible_moves.extend([[0, 3], [0, 4], [0, 5], [1, 3], [1, 5], [2, 3], [2, 4], [2, 5]])
            if [from_row, from_col] == [1, 5]:
                self._possible_moves.extend([[0, 5], [1, 4], [2, 5]])
            if [from_row, from_col] == [2, 3]:
                self._possible_moves.extend([[1, 3], [1, 4], [2, 4]])
            if [from_row, from_col] == [2, 4]:
                self._possible_moves.extend([[1, 4], [2, 3], [2, 5]])
            if [from_row, from_col] == [2, 5]:
                self._possible_moves.extend([[1, 4], [1, 5], [2, 4]])
        if self._color == 'b':
            # can move in the blue palace
            if [from_row, from_col] == [7, 3]:
                self._possible_moves.extend([[7, 4], [8, 3], [8, 4]])
            if [from_row, from_col] == [7, 4]:
                self._possible_moves.extend([[7, 3], [7, 5], [8, 4]])
            if [from_row, from_col] == [7, 5]:
                self._possible_moves.extend([[7, 4], [8, 4], [8, 5]])
            if [from_row, from_col] == [8, 3]:
                self._possible_moves.extend([[7, 3], [8, 4], [9, 3]])
            if [from_row, from_col] == [8, 4]:
                self._possible_moves.extend([[7, 3], [7, 4], [7, 5], [8, 3], [8, 5], [9, 3], [9, 4], [9, 5]])
            if [from_row, from_col] == [8, 5]:
                self._possible_moves.extend([[7, 5], [8, 4], [9, 5]])
            if [from_row, from_col] == [9, 3]:
                self._possible_moves.extend([[8, 3], [8, 4], [9, 4]])
            if [from_row, from_col] == [9, 4]:
                self._possible_moves.extend([[8, 4], [9, 3], [9, 5]])
            if [from_row, from_col] == [9, 5]:
                self._possible_moves.extend([[8, 4], [8, 5], [9, 4]])

        if [to_row, to_col] in self._possible_moves:
            return True
        else:
            return False


class Cannon(Piece):
    """Child of Cannon piece. Represents a cannon piece"""
    def __init__(self, janggi_game, name, location):
        Piece.__init__(self, janggi_game, name, location)

    def set_possible_moves(self, from_row, from_col):
        """generate all possible moves for the piece at the given location."""
        # cannon moves in horizontally or vertically. it must jump over a piece
        # cannot jump over other cannons
        # cannot capture other cannons
        # can move diagonally in the palace. must have a piece in between. Thus can only go from the corner

        # clear possible moves
        self._possible_moves.clear()

        # up movement WORKS!
        # keep going til you run into a piece or the edge of board
        up_row = from_row - 1
        while up_row >= 0 and self._janggi_game.get_square(up_row, from_col) is None:
            up_row -= 1
        # need row to be at least 1 from the top edge as we need to jump over a piece
        if up_row >= 1:
            # if piece we are jumping over is not a cannon
            if self._janggi_game.get_square(up_row, from_col).get_piece_type() != "Ca":
                # again keep going til you run into piece or edge of board
                up_row = up_row - 1
                while up_row >= 0 and self._janggi_game.get_square(up_row, from_col) is None:
                    self._possible_moves.append([up_row, from_col])
                    up_row -= 1
                # if row is on the board, check if piece to be capture is not a cannon
                if up_row >= 0:
                    if self._janggi_game.get_square(up_row, from_col).get_piece_type() != "Ca":
                        self._possible_moves.append([up_row, from_col])

        # down movement WORKS!
        # keep going til you run into a piece or the edge of board
        down_row = from_row + 1
        while down_row <= 9 and self._janggi_game.get_square(down_row, from_col) is None:
            down_row += 1
        # need row to be at least 1 from the edge as we need to jump over a piece
        if down_row <= 8:
            # if piece we are jumping over is not a cannon
            if self._janggi_game.get_square(down_row, from_col).get_piece_type() != "Ca":
                # again keep going til you run into piece or edge of board
                down_row = down_row + 1
                while down_row <= 9 and self._janggi_game.get_square(down_row, from_col) is None:
                    self._possible_moves.append([down_row, from_col])
                    down_row += 1
                # if row is on the board, check if piece to be capture is not a cannon
                if down_row <= 9:
                    if self._janggi_game.get_square(down_row, from_col).get_piece_type() != "Ca":
                        self._possible_moves.append([down_row, from_col])

        # left movement
        # keep going til you run into a piece or the edge of board
        left_col = from_col - 1
        while left_col >= 0 and self._janggi_game.get_square(from_row, left_col) is None:
            left_col -= 1
        # need row to be at least 1 from the edge as we need to jump over a piece
        if left_col >= 1:
            # if piece we are jumping over is not a cannon
            if self._janggi_game.get_square(from_row, left_col).get_piece_type() != "Ca":
                # again keep going til you run into piece or edge of board
                left_col = left_col - 1
                while left_col >= 0 and self._janggi_game.get_square(from_row, left_col) is None:
                    self._possible_moves.append([from_row, left_col])
                    left_col -= 1
                # if row is on the board, check if piece to be capture is not a cannon
                if left_col >= 0:
                    if self._janggi_game.get_square(from_row, left_col).get_piece_type() != "Ca":
                        self._possible_moves.append([from_row, left_col])

        # right movement
        # keep going til you run into a piece or the edge of board
        right_col = from_col + 1
        while right_col <= 8 and self._janggi_game.get_square(from_row, right_col) is None:
            right_col += 1
        # need row to be at least 1 from the edge as we need to jump over a piece
        if right_col <= 7:
            # if piece we are jumping over is not a cannon
            if self._janggi_game.get_square(from_row, right_col).get_piece_type() != "Ca":
                # again keep going til you run into piece or edge of board
                right_col = right_col + 1
                while right_col <= 8 and self._janggi_game.get_square(from_row, right_col) is None:
                    self._possible_moves.append([from_row, right_col])
                    right_col += 1
                # if row is on the board, check if piece to be capture is not a cannon
                if right_col <= 8:
                    if self._janggi_game.get_square(from_row, right_col).get_piece_type() != "Ca":
                        self._possible_moves.append([from_row, right_col])

        # palace movement: can only occur from the corners and piece needs to be in the middle
        # Same rules apply: cant jump over cannons, cant capture cannons
        # red palace
        if [from_row, from_col] == [0, 3]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(1, 4) is not None and self._janggi_game.get_square(1, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(2, 5) is not None and self._janggi_game.get_square(2, 5).get_piece_type() != "Ca":
                    self._possible_moves.append([2, 5])
                # if the corner is empty
                elif self._janggi_game.get_square(2, 5) is None:
                    self._possible_moves.append([2, 5])
        if [from_row, from_col] == [0, 5]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(1, 4) is not None and self._janggi_game.get_square(1, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(2, 3) is not None and self._janggi_game.get_square(2, 3).get_piece_type() != "Ca":
                    self._possible_moves.append([2, 3])
                # if the corner is empty
                elif self._janggi_game.get_square(2, 3) is None:
                    self._possible_moves.append([2, 3])
        if [from_row, from_col] == [2, 3]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(1, 4) is not None and self._janggi_game.get_square(1, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(0, 5) is not None and self._janggi_game.get_square(0, 5).get_piece_type() != "Ca":
                    self._possible_moves.append([0, 5])
                # if the corner is empty
                elif self._janggi_game.get_square(0, 5) is None:
                    self._possible_moves.append([0, 5])
        if [from_row, from_col] == [2, 5]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(1, 4) is not None and self._janggi_game.get_square(1, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(0, 3) is not None and self._janggi_game.get_square(0, 3).get_piece_type() != "Ca":
                    self._possible_moves.append([0, 3])
                # if the corner is empty
                elif self._janggi_game.get_square(0, 3) is None:
                    self._possible_moves.append([0, 3])
        # blue palace
        if [from_row, from_col] == [7, 3]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(8, 4) is not None and self._janggi_game.get_square(8, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(9, 5) is not None and self._janggi_game.get_square(9, 5).get_piece_type() != "Ca":
                    self._possible_moves.append([9, 5])
                # if the corner is empty
                elif self._janggi_game.get_square(9, 5) is None:
                    self._possible_moves.append([9, 5])
        if [from_row, from_col] == [7, 5]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(8, 4) is not None and self._janggi_game.get_square(8, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(9, 3) is not None and self._janggi_game.get_square(9, 3).get_piece_type() != "Ca":
                    self._possible_moves.append([9, 3])
                # if the corner is empty
                elif self._janggi_game.get_square(9, 3) is None:
                    self._possible_moves.append([9, 3])
        if [from_row, from_col] == [9, 3]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(8, 4) is not None and self._janggi_game.get_square(8, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(7, 5) is not None and self._janggi_game.get_square(7, 5).get_piece_type() != "Ca":
                    self._possible_moves.append([7, 5])
                # if the corner is empty
                elif self._janggi_game.get_square(7, 5) is None:
                    self._possible_moves.append([7, 5])
        if [from_row, from_col] == [9, 5]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(8, 4) is not None and self._janggi_game.get_square(8, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(7, 3) is not None and self._janggi_game.get_square(7, 3).get_piece_type() != "Ca":
                    self._possible_moves.append([7, 3])
                # if the corner is empty
                elif self._janggi_game.get_square(7, 3) is None:
                    self._possible_moves.append([7, 3])

    def valid_move(self, from_row, from_col, to_row, to_col):
        """return true if valid move"""
        # cannon moves in horizontally or vertically. it must jump over a piece
        # cannot jump over other cannons
        # cannot capture other cannons
        # can move diagonally in the palace. must have a piece in between. Thus can only go from the corner

        # clear possible moves
        self._possible_moves.clear()

        # up movement WORKS!
        # keep going til you run into a piece or the edge of board
        up_row = from_row - 1
        while up_row >= 0 and self._janggi_game.get_square(up_row, from_col) is None:
            up_row -= 1
        # need row to be at least 1 from the top edge as we need to jump over a piece
        if up_row >= 1:
            # if piece we are jumping over is not a cannon
            if self._janggi_game.get_square(up_row, from_col).get_piece_type() != "Ca":
                # again keep going til you run into piece or edge of board
                up_row = up_row - 1
                while up_row >= 0 and self._janggi_game.get_square(up_row, from_col) is None:
                    self._possible_moves.append([up_row, from_col])
                    up_row -= 1
                # if row is on the board, check if piece to be capture is not a cannon
                if up_row >= 0:
                    if self._janggi_game.get_square(up_row, from_col).get_piece_type() != "Ca":
                        self._possible_moves.append([up_row, from_col])

        # down movement WORKS!
        # keep going til you run into a piece or the edge of board
        down_row = from_row + 1
        while down_row <= 9 and self._janggi_game.get_square(down_row, from_col) is None:
            down_row += 1
        # need row to be at least 1 from the edge as we need to jump over a piece
        if down_row <= 8:
            # if piece we are jumping over is not a cannon
            if self._janggi_game.get_square(down_row, from_col).get_piece_type() != "Ca":
                # again keep going til you run into piece or edge of board
                down_row = down_row + 1
                while down_row <= 9 and self._janggi_game.get_square(down_row, from_col) is None:
                    self._possible_moves.append([down_row, from_col])
                    down_row += 1
                # if row is on the board, check if piece to be capture is not a cannon
                if down_row <= 9:
                    if self._janggi_game.get_square(down_row, from_col).get_piece_type() != "Ca":
                        self._possible_moves.append([down_row, from_col])

        # left movement
        # keep going til you run into a piece or the edge of board
        left_col = from_col - 1
        while left_col >= 0 and self._janggi_game.get_square(from_row, left_col) is None:
            left_col -= 1
        # need row to be at least 1 from the edge as we need to jump over a piece
        if left_col >= 1:
            # if piece we are jumping over is not a cannon
            if self._janggi_game.get_square(from_row, left_col).get_piece_type() != "Ca":
                # again keep going til you run into piece or edge of board
                left_col = left_col - 1
                while left_col >= 0 and self._janggi_game.get_square(from_row, left_col) is None:
                    self._possible_moves.append([from_row, left_col])
                    left_col -= 1
                # if row is on the board, check if piece to be capture is not a cannon
                if left_col >= 0:
                    if self._janggi_game.get_square(from_row, left_col).get_piece_type() != "Ca":
                        self._possible_moves.append([from_row, left_col])

        # right movement
        # keep going til you run into a piece or the edge of board
        right_col = from_col + 1
        while right_col <= 8 and self._janggi_game.get_square(from_row, right_col) is None:
            right_col += 1
        # need row to be at least 1 from the edge as we need to jump over a piece
        if right_col <= 7:
            # if piece we are jumping over is not a cannon
            if self._janggi_game.get_square(from_row, right_col).get_piece_type() != "Ca":
                # again keep going til you run into piece or edge of board
                right_col = right_col + 1
                while right_col <= 8 and self._janggi_game.get_square(from_row, right_col) is None:
                    self._possible_moves.append([from_row, right_col])
                    right_col += 1
                # if row is on the board, check if piece to be capture is not a cannon
                if right_col <= 8:
                    if self._janggi_game.get_square(from_row, right_col).get_piece_type() != "Ca":
                        self._possible_moves.append([from_row, right_col])

        # palace movement: can only occur from the corners and piece needs to be in the middle
        # Same rules apply: cant jump over cannons, cant capture cannons
        # red palace
        if [from_row, from_col] == [0, 3]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(1, 4) is not None and self._janggi_game.get_square(1, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(2, 5) is not None and self._janggi_game.get_square(2, 5).get_piece_type() != "Ca":
                    self._possible_moves.append([2, 5])
                # if the corner is empty
                elif self._janggi_game.get_square(2, 5) is None:
                    self._possible_moves.append([2, 5])
        if [from_row, from_col] == [0, 5]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(1, 4) is not None and self._janggi_game.get_square(1, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(2, 3) is not None and self._janggi_game.get_square(2, 3).get_piece_type() != "Ca":
                    self._possible_moves.append([2, 3])
                # if the corner is empty
                elif self._janggi_game.get_square(2, 3) is None:
                    self._possible_moves.append([2, 3])
        if [from_row, from_col] == [2, 3]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(1, 4) is not None and self._janggi_game.get_square(1, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(0, 5) is not None and self._janggi_game.get_square(0, 5).get_piece_type() != "Ca":
                    self._possible_moves.append([0, 5])
                # if the corner is empty
                elif self._janggi_game.get_square(0, 5) is None:
                    self._possible_moves.append([0, 5])
        if [from_row, from_col] == [2, 5]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(1, 4) is not None and self._janggi_game.get_square(1, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(0, 3) is not None and self._janggi_game.get_square(0, 3).get_piece_type() != "Ca":
                    self._possible_moves.append([0, 3])
                # if the corner is empty
                elif self._janggi_game.get_square(0, 3) is None:
                    self._possible_moves.append([0, 3])
        # blue palace
        if [from_row, from_col] == [7, 3]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(8, 4) is not None and self._janggi_game.get_square(8, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(9, 5) is not None and self._janggi_game.get_square(9, 5).get_piece_type() != "Ca":
                    self._possible_moves.append([9, 5])
                # if the corner is empty
                elif self._janggi_game.get_square(9, 5) is None:
                    self._possible_moves.append([9, 5])
        if [from_row, from_col] == [7, 5]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(8, 4) is not None and self._janggi_game.get_square(8, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(9, 3) is not None and self._janggi_game.get_square(9, 3).get_piece_type() != "Ca":
                    self._possible_moves.append([9, 3])
                # if the corner is empty
                elif self._janggi_game.get_square(9, 3) is None:
                    self._possible_moves.append([9, 3])
        if [from_row, from_col] == [9, 3]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(8, 4) is not None and self._janggi_game.get_square(8, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(7, 5) is not None and self._janggi_game.get_square(7, 5).get_piece_type() != "Ca":
                    self._possible_moves.append([7, 5])
                # if the corner is empty
                elif self._janggi_game.get_square(7, 5) is None:
                    self._possible_moves.append([7, 5])
        if [from_row, from_col] == [9, 5]:
            # if middle of palace is not empty and does not have a cannon
            if self._janggi_game.get_square(8, 4) is not None and self._janggi_game.get_square(8, 4).get_piece_type() != "Ca":
                # if corner is not empty and does not have a cannon
                if self._janggi_game.get_square(7, 3) is not None and self._janggi_game.get_square(7, 3).get_piece_type() != "Ca":
                    self._possible_moves.append([7, 3])
                # if the corner is empty
                elif self._janggi_game.get_square(7, 3) is None:
                    self._possible_moves.append([7, 3])

        if [to_row, to_col] in self._possible_moves:
            return True
        else:
            return False


def main():
    game = JanggiGame()
    game.make_move('e7', 'e6')
    game.make_move('e2', 'e2')
    game.make_move('e6', 'e5')
    game.make_move('e2', 'e2')
    game.make_move('e5', 'e4')
    game.make_move('e2', 'e2')
    game.make_move('e4', 'd4')
    game.make_move('e2', 'e2')
    game.make_move('d4', 'c4')
    game.make_move('e2', 'e2')
    game.make_move('a10', 'a9')
    game.make_move('e2', 'e2')
    game.make_move('a9', 'd9')
    game.make_move('e2', 'e2')
    game.make_move('d9', 'd8')
    game.make_move('e2', 'e2')
    game.make_move('d8', 'd7')
    game.make_move('e2', 'e2')
    game.make_move('d7', 'd6')
    game.make_move('i1', 'i2')
    game.make_move('e9', 'e9')
    game.make_move('i2', 'g2')
    game.make_move('e9', 'e9')
    game.make_move('i4', 'h4')
    game.make_move('e9', 'e9')
    game.make_move('h3', 'h5')
    game.make_move('i10', 'i9')
    game.make_move('e2', 'e2')
    game.make_move('i9', 'g9')
    game.make_move('e2', 'e2')
    game.make_move('g9', 'g8')
    game.make_move('e2', 'e2')
    game.make_move('h8', 'f8')
    game.make_move('f1', 'e1')
    game.make_move('g7', 'f7')
    game.make_move('e2', 'e2')
    game.make_move('i7', 'i6')
    game.make_move('e2', 'e2')
    game.make_move('g10', 'i7')
    game.make_move('e2', 'e2')
    game.make_move('i7', 'f5')
    game.make_move('e2', 'e2')
    game.make_move('f5', 'd8')
    game.make_move('e2', 'e2')
    game.make_move('d8', 'b5')
    game.make_move('e2', 'e2')
    game.make_move('c4', 'd4')
    game.make_move('e2', 'e2')
    game.make_move('d4', 'e4')
    game.make_move('e2', 'e2')
    # checkmate
    game.make_move('e4', 'e3')
    print(game.get_game_state())
    game.print_board()


if __name__ == "__main__":
    main()




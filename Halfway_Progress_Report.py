# Author: Noble Koshy
# Date: 2/24/21
# Description: Halfway Progress Report


class JanggiGame:
    """
    class named JanggiGame for playing an abstract board game called Janggi.
    This is the main class. It uses composition as the JanggiGame has pieces. The pieces are stored in the board list
    """
    def __init__(self):
        """initialize Jangi class data members"""
        # game state (string), players (2 element list: blue, red), current player's turn (string)
        # blue_check (boolean), red_check (boolean)
        # board: stored as a 2D list. 9x9 list representing the board.
        # Create instances of all pieces objects.
        # Store pieces objects inside board list at the starting locations.
        pass

    def algebraic_notation_to_board_index(self, algebraic_notation):
        """take algebraic notation and return row, column number (list index, starts at 0)"""
        pass

    def get_board(self):
        """return board list"""
        return self._board

    def print_board(self):
        """print board in human readable format"""
        pass

    def get_game_state(self):
        """returns one of these values, depending on the game state: 'UNFINISHED' or 'RED_WON' or 'BLUE_WON'."""
        pass

    def get_current_turn(self):
        """returns the current player's turn."""
        pass

    def get_other_player(self):
        """get player NOT on their turn. Use this to update the current player's turn"""
        # Use list comprehension to find other player. Return slice of single element list.
        pass

    def is_in_check(self, player):
        """
        takes as a parameter either 'red' or 'blue' and returns True if that player is in check,
        but returns False otherwise.
        If check flag for the given color is true, then return true.
        """
        pass

    def make_move(self, from_location, to_location):
        """
        two parameters - strings that represent the square to move from and the square to move
        If the square being moved from does not contain a piece belonging to the player whose turn it is,
        or if the indicated move is not legal, or if the game has already been won, then it should just return False.
        Otherwise it should make the indicated move, remove any captured piece, update the game state if necessary,
        update whose turn it is, and return True.
        """
        pass


class Piece:
    """Abstract class representing a Piece on the board, Interacts with JanggiGame to access board"""
    def __init__(self, name, color, location, janggi_game):
        """initialize Piece class data members"""
        # Name of piece (string), color (string), location on board (two element list: row, col)
        # janggi_game (janggi_game class): this is to allow the piece class to access the game's board data
        # possible_moves (list): will store all the possible moves for a piece at a given location.
        pass

class Chariot(Piece):
    """Class representing Chariot piece. Inherits from Piece class"""
    def __init__(self, name, color, location, janggi_game):
        Piece.__init__(self, name, color, location, janggi_game)

    def get_possible_moves(self):
        """return list of all possible moves for a piece at its current location. Based on rules for this piece
        and the current game board. """
        pass

class Elephant(Piece):
    """Class representing Elephant piece. Inherits from Piece class"""
    def __init__(self, name, color, location, janggi_game):
        Piece.__init__(self, name, color, location, janggi_game)

    def get_possible_moves(self):
        """return list of all possible moves for a piece at its current location. Based on rules for this piece
        and the current game board. """
        pass

class Horse(Piece):
    """Class representing Horse piece. Inherits from Piece class"""
    def __init__(self, name, color, location, janggi_game):
        Piece.__init__(self, name, color, location, janggi_game)

    def get_possible_moves(self):
        """return list of all possible moves for a piece at its current location. Based on rules for this piece
        and the current game board. """
        pass

class Guard(Piece):
    """Class representing Guard piece. Inherits from Piece class"""
    def __init__(self, name, color, location, janggi_game):
        Piece.__init__(self, name, color, location, janggi_game)

    def get_possible_moves(self):
        """return list of all possible moves for a piece at its current location. Based on rules for this piece
        and the current game board. """
        pass

class Cannon(Piece):
    """Class representing Cannon piece. Inherits from Piece class"""
    def __init__(self, name, color, location, janggi_game):
        Piece.__init__(self, name, color, location, janggi_game)

    def get_possible_moves(self):
        """return list of all possible moves for a piece at its current location. Based on rules for this piece
        and the current game board. """
        pass

class Solider(Piece):
    """Class representing Solider piece. Inherits from Piece class"""
    def __init__(self, name, color, location, janggi_game):
        Piece.__init__(self, name, color, location, janggi_game)

    def get_possible_moves(self):
        """return list of all possible moves for a piece at its current location. Based on rules for this piece
        and the current game board. """
        pass

class General(Piece):
    """Class representing General piece. Inherits from Piece class"""
    def __init__(self, name, color, location, janggi_game):
        Piece.__init__(self, name, color, location, janggi_game)

    def get_possible_moves(self):
        """return list of all possible moves for a piece at its current location. Based on rules for this piece
        and the current game board. """
        pass

# "DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"

# Initializing the board
# Board is initialized using a 2-dimensional list. A 9x9 list. Elements represent squares on the board.
# IE row 2, column E of board is represented by board[1][4]
# Blank elements represent blank squares on the board.
# Create objects for all game pieces and store in starting location in board list

# Determining how to represent pieces at a given location on the board
# Represent a piece at a given location with a piece object. An abstract parent piece class is defined.
# From the parent piece class we have child piece variations (Solider, Cannon, etc)
# Piece objects have a data member recording their location. Written in list index format (ie [1,4])
# Piece objects are stored in the board list from the JangiGame class.

# Determining how to validate a given move according to the rules for each piece, turn taking and other game rules.
# Each piece object has a possible moves function. This function returns a list of all possible/legal moves for a piece
# based on its current location. If to_location given to JangiClass make_move is in the possible moves list for the
# selected piece object, then it is a valid move.
# Within JangiGame make_move method, use conditional statements:
# If the color of the piece object selected does not match the color of the current player then return false.
# Also if the location selected is a blank square (board list element), then return false.
# Also if the game state is not finished, then return false.

# Modifying the board state after each move.
# Within the JangiGame make_move method: pop the piece object board list current location to the new location.
# Replacing what was already at that location. The old location will now be blank.
# Also update the location data member for the piece object with the new location info.

# Determining how to track which player's turn it is to play right now.
# JanggiGame class has a data member called current_turn that tracks who's turn it is.
# This starts as "blue" as blue starts. Currrent_turn changes to the other player once make_move completes & is true.

# Determining how to detect the checkmate scenario.
# JanggiGame has data members for check (boolean) and checkmate (boolean). We determine check and checkmate
# Within the make_move method. After a sucessful move occurs and the board is updated,
# run the possible_moves for the piece in its new location.
# Check if any of the possible moves have the same location as the opponent's general piece. If yes, then the
# opponent is in check. Change the check flag for the opponent color to true.
# Now we must check if the opponent is in checkmate. Run the possible moves function for the opponents general.
# If their general has no possible moves (list is empty), then the opponent is in checkmate.
# Change the game state to current player won.

# Determining which player has won and also figuring out when to check that.
# Winner is determined within the make_move method, at the end. After we determine the opponent is in checkmate,
# then we update the game state to current player won.






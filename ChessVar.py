# Author: Hunter Shipman
# GitHub username: HunterShipman
# Date: 11/30/2023
# Description:  A ChessVar class that will allow two players to play a derivative of chess. In this version of chess, a
#               player wins by taking all of one type of chess piece. For example, you can win by taking both knights,
#               every single pawn, or just the queen. Also, the king is not a special piece, it still moves like a king,
#               but it cannot castle and there is no check or checkmate. Also, pawns cannot use en passant or pawn
#               promotion, however they can still move two places forward on their first move and still capture
#               diagonally.

class ChessVar:
    """
    This class will be used to play the (derivative) game of chess.

    It will communicate with the children of the ChessPiece class to determine different aspects of a
    specific chess piece, such as the chess pieces name and if the attempted move is legal or not.

    _piece_dict: represents all the pieces left on the board. Once a specific pieces count has dropped to 0, the
                 opposing player has won
    _game_state: represents if the game is still active or once a player has won, who won the game
    _turn:       represents which players turn it is
    _board:      represents the chess board. It is a list of 8 lists. Each list represents a row of the chess board and
                 each lists index represents a square on that row.
    """
    def __init__(self):
        self._piece_dict = {'K': 1, 'Q': 1, 'R': 2, 'B': 2, 'N': 2, 'P': 8, 'k': 1, 'q': 1, 'r': 2, 'b': 2, 'n': 2,
                            'p': 8}
        self._game_state = "UNFINISHED"
        self._turn = "WHITE"
        self._board = [

            [Rook("BLACK"), Knight("BLACK"), Bishop("BLACK"), Queen("BLACK"), King("BLACK"), Bishop("BLACK"),
             Knight("BLACK"), Rook("BLACK")],

            [Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"), Pawn("BLACK"),
             Pawn("BLACK")],

            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],

            [Pawn("WHITE"), Pawn("WHITE"), Pawn("WHITE"), Pawn("WHITE"), Pawn("WHITE"), Pawn("WHITE"), Pawn("WHITE"),
             Pawn("WHITE")],

            [Rook("WHITE"), Knight("WHITE"), Bishop("WHITE"), Queen("WHITE"), King("WHITE"), Bishop("WHITE"),
             Knight("WHITE"), Rook("WHITE")]

        ]

    def get_game_state(self):
        """
        :return: the chess boards game state (can be "UNFINISHED", "WHITE_WON", or "BLACK_WON"
        """
        return self._game_state

    def get_turn(self):
        """
        :return: which players turn it is ("WHITE" or "BLACK")
        """
        return self._turn

    def get_piece_dict(self):
        """
        :return: the piece_dict dictionary
        """
        return self._piece_dict

    def del_piece(self, square):
        """
        Deletes a piece from the chess boards dictionary of pieces left on the board.
        MyBoard.del_piece('a5') would determine what piece is in square a5 and then decrement its count in the boards
        _piece_dict data member.
        NOTE: does not remove a piece from the board.

        :parameter square: must be satisfied by the square in algebraic notation to delete the chess piece from.
        """
        indices = algebra_indices(square)  # looks like [x, y]
        piece_name = self._board[indices[0]][indices[1]].get_name()
        self._piece_dict[piece_name] = self._piece_dict[piece_name] - 1

    def make_move(self, start, end):
        """
        First checks if a player has won the game. Then checks if there is a piece in the starting square. Then checks
        if the piece in the starting square is the opponents color. Then checks if the move is legal. Then checks if
        there are any obstructions. If any of these occur we return False.

        If we pass all of those tests, then we make the move and return True. If an opposing piece is occupying the end
        square, that piece is captured. When a piece is captured we decrement its count from the boards _piece_dict data
        member and replace it on the board with the capturing piece. If doing so makes the specific pieces count 0, then
        the player whose turn it is will have won and the boards _game_state will be changed to reflect that.

        :parameter start: the square containing the piece we want to move in algebraic notation as a string
        :parameter end: the square we want to move the piece to in algebraic notation as a string
        """
        # check game state
        if self._game_state != "UNFINISHED":
            return False

        # check if there is a piece in the square
        indices_start = algebra_indices(start)  # looks like [x, y]
        start_piece = self._board[indices_start[0]][indices_start[1]]
        if start_piece is None:
            return False

        # check if the piece is the right color
        if start_piece.get_color() != self._turn:
            return False

        # check if move is legal
        if not start_piece.is_move_legal(start, end):
            return False

        # check if any obstructions, excluding end location (except for knight (and king??)) :TODO


        # check final location for a piece.
        indices_end = algebra_indices(end)  # looks like [x, y]
        end_piece = self._board[indices_end[0]][indices_end[1]]
        if end_piece is None:  # if no piece, skip
            pass
        else:
            if end_piece.get_color() == self._turn:  # if end square has a piece of the players own color
                return False
            else:  # if end square is opponents color
                piece_name = end_piece.get_name()
                self._piece_dict[piece_name] -= 1

        # move piece
        self._board[indices_end[0]][indices_end[1]] = start_piece
        self._board[indices_start[0]][indices_start[1]] = None

        # change whose turn it is
        if self._turn == "WHITE":
            self._turn = "BLACK"
        else:
            self._turn = "WHITE"



    def show_board(self):
        """
        Prints out the current state of the board

        Capital letters are black pieces and lowercase letters are white pieces.
        R = Rook, N = Knight, B = Bishop, Q = Queen, K = King, P = Pawn.
        """
        # prints the top "line" of the board
        print('      a   b   c   d   e   f   g   h')
        print('    _________________________________')

        # prints the actual board and it's pieces
        for row in range(8):
            row_list = [8, 7, 6, 5, 4, 3, 2, 1]
            print(f'{row_list[row]}   ', end='')

            for column in range(8):
                print("| ", end='')
                if self._board[row][column] is None:
                    print('  ', end='')
                else:
                    print(self._board[row][column].get_name() + ' ', end='')

            print(f'|   {row_list[row]}')

        # prints the bottom "line" of the board
        print('    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        print('      a   b   c   d   e   f   g   h')


class ChessPiece:
    """
    This class will act as a parent class for each different chess piece. Each child class will have a different "name"
    that is one letter. If the piece's color is Black, said letter will be uppercase. For example the black kings name
    will be "K", and the white kings name will be "k".

    The point of having this parent class is to not have to write each get method for the child classes. Also, because
    each piece has different allowed moves, the is_move_legal method will work differently for each class but will
    always return True or False. This allows us to use polymorphism when checking if a pieces attempted move is legal.
    """
    def __init__(self, color):
        self._name = None  # will be overriden by child
        self._has_moved = False  # Once a piece has moved, changes to True
        self._color = color  # must be "WHITE" or "BLACK"

    def get_has_moved(self):
        """
        :return: True if the piece has moved and False if it hasn't
        """
        return self._has_moved

    def set_has_moved(self):
        """
        Sets the objects has_moved status to true. Currently only being used for rooks.
        """
        self._has_moved = True

    def get_color(self):
        """
        :return: the color data member of the piece
        """
        return self._color

    def get_name(self):
        """
        :return: the name data member of the piece
        """
        return self._name


class King(ChessPiece):
    """
    A King class that is a child of the ChessPiece class. Used to represent the king piece and it's attributes.

    MOVES: can move one square in any direction. like a furnace in minecraft.
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "K" if color == "BLACK" else "k"

    def is_move_legal(self, start, end):
        """
        returns True if the move is legal, returns False if it is not.

        :parameter start: the square the piece starts in, in algebraic notation as a string
        :parameter end: the square we are attempting to move the piece to in algebraic notation as a string
        """
        return True


class Queen(ChessPiece):
    """
    A Queen class that is a child of the ChessPiece class. Used to represent the Queen piece and it's attributes.

    MOVES: straight up and down OR diagonally. as far as she wants
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "Q" if color == "BLACK" else "q"

    def is_move_legal(self, start, end):
        """
        returns True if the move is legal, returns False if it is not.

        :parameter start: the square the piece starts in, in algebraic notation as a string
        :parameter end: the square we are attempting to move the piece to in algebraic notation as a string
        """
        return True


class Rook(ChessPiece):
    """
    A Rook class that is a child of the ChessPiece class. Used to represent a Rook piece and it's attributes.

    MOVES: Straight up and down or left to right. as far as he wants
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "R" if color == "BLACK" else "r"

    def is_move_legal(self, start, end):
        """
        returns True if the move is legal, returns False if it is not.

        :parameter start: the square the piece starts in, in algebraic notation as a string
        :parameter end: the square we are attempting to move the piece to in algebraic notation as a string
        """
        return True


class Bishop(ChessPiece):
    """
    A Bishop class that is a child of the ChessPiece class. Used to represent a Bishop piece and it's attributes.

    MOVES: only diagonally. as far as he wants
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "B" if color == "BLACK" else "b"

    def is_move_legal(self, start, end):
        """
        returns True if the move is legal, returns False if it is not.

        :parameter start: the square the piece starts in, in algebraic notation as a string
        :parameter end: the square we are attempting to move the piece to in algebraic notation as a string
        """
        return True


class Knight(ChessPiece):
    """
    A Knight class that is a child of the ChessPiece class. Used to represent a Knight piece and it's attributes.

    MOVES: "like a capital L". Two squares one direction, one to the side. EX: two down one left.
        NOTE: can "jump" over another piece.
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "N" if color == "BLACK" else "n"

    def is_move_legal(self, start, end):
        """
        returns True if the move is legal, returns False if it is not.

        :parameter start: the square the piece starts in, in algebraic notation as a string
        :parameter end: the square we are attempting to move the piece to in algebraic notation as a string
        """
        return True


class Pawn(ChessPiece):
    """
    A Pawn class that is a child of the ChessPiece class. Used to represent a Pawn piece and it's attributes.

    MOVES: Can move one square forward, never backward.
        NOTE: on first move, can move two or one squares forward.
        NOTE: ONLY captures diagonally. cannot capture if the square in front is occupied
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "P" if color == "BLACK" else "p"

    def is_move_legal(self, start, end):
        """
        returns True if the move is legal, returns False if it is not.

        :parameter start: the square the piece starts in, in algebraic notation as a string
        :parameter end: the square we are attempting to move the piece to in algebraic notation as a string
        """
        return True


def algebra_indices(square):
    """
    Converts the given square into a list of indices to plug into the chess board. Because the representation of the
    board for the players is in algebraic notation and the program represents the board as a list of lists, we must
    convert the algebraic notation into indices for the boards list of lists. One thing to note is algebraic notation
    puts the column first and the row second. This will return a list that has the row first and column second as that
    is how the boards list of lists is used.

    :parameter square: should be a string in algebraic notation.
    :returns: the equivalent representation as a list of integers
    EX: "d6" is returned as [2, 3]
    """
    temp_list = [7, 6, 5, 4, 3, 2, 1, 0]
    new_square = list(square)
    new_square[0] = ord(new_square[0]) - 97  # converts the letter to its unicode value, then makes it our index
    new_square[1] = temp_list[int(new_square[1]) - 1]
    new_square[0], new_square[1] = new_square[1], new_square[0]

    return new_square


game = ChessVar()
game.show_board()
print(game.get_turn())
print('')
print(game.get_piece_dict())
print('')
game.make_move("a1", "a7")
print('')
game.show_board()
print(game.get_turn())
print('')
print(game.get_piece_dict())

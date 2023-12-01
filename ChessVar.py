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
    specific chess piece, such as what pieces each piece is allowed to capture and what moves it is allowed to make.

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
        returns the chess boards game state (can be "UNFINISHED", "WHITE_WON", or "BLACK_WON"
        """
        return self._game_state

    def get_turn(self):
        """
        returns which players turn it is ("WHITE" or "BLACK")
        """
        return self._turn

    def del_piece(self, square):
        """
        Deletes a piece from the chess boards dictionary of pieces left on the board.
        MyBoard.del_piece('a5') would determine what piece is in square a5 and then decrement its count in the boards
         _piece_dict data member

        :parameter square: must be satisfied by the square in algebraic notation to delete the chess piece from.
        """
        indices = algebra_indices(square)
        piece_name = self._board[indices[0]][indices[1]].get_name()
        self._piece_dict[piece_name] = self._piece_dict[piece_name] - 1

    def make_move(self, start, end):
        """
        First checks if move is allowed to be made. If a move is legal, then we make the move. If an opposing piece is
        occupying the end square, that piece is captured. MyBoard.make_move('b2', 'a3') would move the chess piece in
        square b2 to square a3 (provided there is a piece in b2 and the move is legal).

        start and end are in algebraic notation.
        """
        pass

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
    will be "K", and the white king will be "k".

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
        returns True if the piece has moved and False if it hasn't
        """
        return self._has_moved

    def set_has_moved(self):
        """
        sets the objects has_moved status to true
        """
        self._has_moved = True

    def get_color(self):
        """
        returns the color data member of the piece
        """
        return self._color

    def get_name(self):
        return self._name


class King(ChessPiece):
    """
    A King class that is a child of the ChessPiece class. Used to represent the king piece and it's attributes.

    MOVES: can move one square in any direction. like a furnace in minecraft.
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "K" if color == "BLACK" else "k"

    def is_move_legal(self, delta_x, delta_y):
        """
        returns True if the move is legal, returns False if it is not. The change in x and y must be calculated before
        being passed to this method
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

    def is_move_legal(self, delta_x, delta_y):
        """
        returns True if the move is legal, returns False if it is not. The change in x and y must be calculated before
        being passed to this method
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

    def is_move_legal(self, delta_x, delta_y):
        """
        returns True if the move is legal, returns False if it is not. The change in x and y must be calculated before
        being passed to this method
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

    def is_move_legal(self, delta_x, delta_y):
        """
        returns True if the move is legal, returns False if it is not. The change in x and y must be calculated before
        being passed to this method
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

    def is_move_legal(self, delta_x, delta_y):
        """
        returns True if the move is legal, returns False if it is not. The change in x and y must be calculated before
        being passed to this method
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

    def is_move_legal(self, delta_x, delta_y):
        """
        returns True if the move is legal, returns False if it is not. The change in x and y must be calculated before
        being passed to this method
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
    new_square[0] = ord(new_square[0]) - 97
    new_square[1] = temp_list[int(new_square[1]) - 1]
    new_square[0], new_square[1] = new_square[1], new_square[0]

    return new_square


game = ChessVar()
game.show_board()
# Author: Hunter Shipman
# GitHub username: HunterShipman
# Date: 12/10/2023
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

    Capital letters are black pieces and lowercase letters are white pieces.
        R = Rook, N = Knight, B = Bishop, Q = Queen, K = King, P = Pawn.

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

    def get_board(self):
        """
        :return: the _board data member (list of lists)
        """
        return self._board

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
        if the starting and ending squares are the same. Then checks if the piece in the starting square is the
        opponents color. Then checks if the move is illegal or if there are any obstructions. If any of these occur we
        return False.

        If we pass all of those tests, we then check the end square for a piece. If an opposing piece is occupying the
        end square, that piece is captured. If a piece of the same color is occupying the end square, we return false.
        When a piece is captured we decrement its count from the boards _piece_dict data member and replace it on the
        board with the capturing piece. If doing so makes the specific pieces count 0, then the player whose turn it is
        will have won and the boards _game_state will be changed to reflect that.

        :parameter start: the square containing the piece we want to move in algebraic notation as a string
        :parameter end: the square we want to move the piece to in algebraic notation as a string
        """
        print(f"from_square is {start} and to_square is {end}")
        # check game state
        if self._game_state != "UNFINISHED":
            return False

        indices_end = algebra_indices(end)
        indices_start = algebra_indices(start)

        # check if there is a piece in the start square
        start_piece = self._board[indices_start[0]][indices_start[1]]
        if start_piece is None:
            return False

        # checks if the starting square and ending square are the same
        if start == end:
            return False

        # check if the piece is the right color
        if start_piece.get_color() != self._turn:
            return False

        # check if move is legal (also checks for obstructions excluding end location)
        # we pass a copy of the board list to ensure the board can't be altered somehow
        if not start_piece.is_move_legal(list(self._board), indices_start, indices_end):
            return False

        # check final location for a piece.
        end_piece = self._board[indices_end[0]][indices_end[1]]
        if end_piece is None:  # if no piece, skip
            pass
        else:
            if end_piece.get_color() == self._turn:  # if end square has a piece of the players own color
                return False
            else:  # if end square is opponents color, capture it
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

        # check if anyone won
        black_pieces = ['K', 'Q', 'R', 'B', 'N', 'P']
        white_pieces = ['k', 'q', 'r', 'b', 'n', 'p']
        for piece in black_pieces:
            if self._piece_dict[piece] == 0:
                self._game_state = "WHITE_WON"
        for piece in white_pieces:
            if self._piece_dict[piece] == 0:
                self._game_state = "BLACK_WON"

        return True

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
     data member that is one letter. If the piece's color is Black, said letter will be uppercase. For example the black
    kings name will be "K", and the white kings name will be "k".

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

    MOVES: Can move one square in any direction including diagonally.
        Note: Cannot be obstructed.
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "K" if color == "BLACK" else "k"

    def is_move_legal(self, board, start, end):
        """
        just has to check if we are attempting to move more than 1 square

        :parameter board: not used for this piece
        :parameter start: the square the piece starts in, in list notation
        :parameter end: the square we are attempting to move the piece to in list notation
        :return: True if move is legal, False if not. Does not check the final piece.
        """
        start_indices = start
        end_indices = end
        delta_x = end_indices[1] - start_indices[1]
        delta_y = end_indices[0] - start_indices[0]

        if abs(delta_x) > 1 or abs(delta_y) > 1:
            return False

        return True


class Queen(ChessPiece):
    """
    A Queen class that is a child of the ChessPiece class. Used to represent the Queen piece and it's attributes.

    MOVES: Straight up and down, left to right, or diagonally. As far as desired.
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "Q" if color == "BLACK" else "q"

    def is_move_legal(self, board, start, end):
        """
        Implements systems from Rook and Bishop to determine if a move is legal.

        :parameter board: the board we are testing as a list of lists
        :parameter start: the square the piece starts in, in list notation
        :parameter end: the square we are attempting to move the piece to in list notation
        :return: True if move is legal, False if not. Does not check the final piece.
        """
        start_indices = start
        end_indices = end
        temp_indices = list(start_indices)
        delta_x = end_indices[1] - start_indices[1]
        delta_y = end_indices[0] - start_indices[0]
        x1, x2 = start_indices[1], end_indices[1]
        y1, y2 = end_indices[0], start_indices[0]

        if x1 > x2:
            x1, x2 = x2, x1  # need lower value to be first for range() to work
        if y1 > y2:
            y1, y2 = y2, y1

        between_x = list(range(x1 + 1, x2))  # list of x values between our starting and ending x
        between_y = list(range(y1 + 1, y2))

        # check if we aren't moving perfectly diagonally or perfectly horizontal/vertical
        if abs(delta_x) != abs(delta_y):
            if x1 != x2 and y1 != y2:
                return False
            pass

        # code for moving horizontal or vertical
        #
        if x1 == x2 or y1 == y2:
            # if we are trying to move horizontally
            if len(between_x) != 0:
                for x in between_x:  # we want to exclude the start and end square
                    if board[start_indices[0]][x] is None:
                        pass
                    else:
                        return False

            # if we are trying to move vertically
            elif len(between_y) != 0:
                for y in between_y:  # we want to exclude the current last square
                    if board[y][start_indices[1]] is None:
                        pass
                    else:
                        return False


        # code for moving diagonally
        #
        else:
            # determine which direction we are going and increment / decrement x and y accordingly
            if delta_x > 0 and delta_y > 0:  # x & y incrementing, going down & right
                for move in range(delta_x - 1):
                    temp_indices[1] += 1
                    temp_indices[0] += 1
                    if board[temp_indices[0]][temp_indices[1]] is None:
                        pass
                    else:
                        return False

            elif delta_x > 0 > delta_y:  # x incrementing, y decrementing, going up & right
                for move in range(delta_x - 1):
                    temp_indices[1] += 1
                    temp_indices[0] -= 1
                    if board[temp_indices[0]][temp_indices[1]] is None:
                        pass
                    else:
                        return False

            elif delta_x < 0 < delta_y:  # x decrementing, y incrementing, going down & left
                for move in range(delta_x - 1):
                    temp_indices[1] -= 1
                    temp_indices[0] += 1
                    if board[temp_indices[0]][temp_indices[1]] is None:
                        pass
                    else:
                        return False

            elif delta_x < 0 and delta_y < 0:  # x & y decrementing, going up & left
                for move in range(delta_x - 1):
                    temp_indices[1] -= 1
                    temp_indices[0] -= 1
                    if board[temp_indices[0]][temp_indices[1]] is None:
                        pass
                    else:
                        return False

        return True


class Rook(ChessPiece):
    """
    A Rook class that is a child of the ChessPiece class. Used to represent a Rook piece and it's attributes.

    MOVES: Straight up and down or left to right. As far as desired.
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "R" if color == "BLACK" else "r"

    def is_move_legal(self, board, start, end):
        """
        We first determine if we are trying to move vertically or horizontally. If we are trying to do both, we return
        False. If we are trying to move vertically we check every square between the start and end to see if there is an
        object there. If there is an object in any square the move is not valid and we return False. We do the same if
        we are trying to move horizontally. If there are no objects in our path, we return True.

        :parameter board: the board we are testing as a list of lists
        :parameter start: the square the piece starts in, in list notation
        :parameter end: the square we are attempting to move the piece to in list notation
        :return: True if move is legal, False if not. Does not check the final piece.
        """
        start_indices = start
        end_indices = end
        delta_x = end_indices[1] - start_indices[1]
        delta_y = end_indices[0] - start_indices[0]
        x1, x2 = start_indices[1], end_indices[1]
        y1, y2 = end_indices[0], start_indices[0]

        if x1 > x2:
            x1, x2 = x2, x1  # need lower value to be first for range() to work
        if y1 > y2:
            y1, y2 = y2, y1

        between_x = list(range(x1 + 1, x2))  # list of x values between our starting and ending x
        between_y = list(range(y1 + 1, y2))

        # if we are trying to move both vertically and horizontally
        if abs(delta_x) > 0 and abs(delta_y) > 0:
            return False

        # if we are trying to move horizontally
        if len(between_x) != 0:
            for x in between_x:  # we want to exclude the start and end square
                if board[start_indices[0]][x] is None:
                    pass
                else:
                    return False

        # if we are trying to move vertically
        else:
            for y in between_y:  # we want to exclude the current last square
                if board[y][start_indices[1]] is None:
                    pass
                else:
                    return False

        return True


class Bishop(ChessPiece):
    """
    A Bishop class that is a child of the ChessPiece class. Used to represent a Bishop piece and it's attributes.

    MOVES: Only diagonally. As far as desired.
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "B" if color == "BLACK" else "b"

    def is_move_legal(self, board, start, end):
        """
        First we check if the attempted move is moving the same amount on the x-axis as the y-axis. This ensures the
        user is trying to move diagonally. If we don't pass this test, we return False. If we do pass, we then check
        for obstructions. We first determine if we need to increment or decrement both the x and y indices. Then we do
        so accordingly delta_x-1 times and check for an object in that square each time. We do this delta_x - 1 times
        so that we only check the squares in between our start and end.

        :parameter board: the board we are testing given as a list of lists
        :parameter start: the square the piece starts in, in list notation
        :parameter end: the square we are attempting to move the piece to in list notation
        :return: True if move is legal, False if not. Does not check the final piece.
        """
        start_indices = start
        end_indices = end
        temp_indices = list(start_indices)
        delta_x = end_indices[1] - start_indices[1]
        delta_y = end_indices[0] - start_indices[0]

        # check if we aren't moving perfectly diagonally
        if abs(delta_x) != abs(delta_y):
            return False

        # determine which direction we are going and increment / decrement x and y accordingly
        if delta_x > 0 and delta_y > 0:  # x & y incrementing, going down & right
            for move in range(delta_x - 1):
                temp_indices[1] += 1
                temp_indices[0] += 1
                if board[temp_indices[0]][temp_indices[1]] is None:
                    pass
                else:
                    return False

        elif delta_x > 0 > delta_y:  # x incrementing, y decrementing, going up & right
            for move in range(delta_x - 1):
                temp_indices[1] += 1
                temp_indices[0] -= 1
                if board[temp_indices[0]][temp_indices[1]] is None:
                    pass
                else:
                    return False

        elif delta_x < 0 < delta_y:  # x decrementing, y incrementing, going down & left
            for move in range(delta_x - 1):
                temp_indices[1] -= 1
                temp_indices[0] += 1
                if board[temp_indices[0]][temp_indices[1]] is None:
                    pass
                else:
                    return False

        else:  # x & y decrementing, going up & left
            for move in range(delta_x - 1):
                temp_indices[1] -= 1
                temp_indices[0] -= 1
                if board[temp_indices[0]][temp_indices[1]] is None:
                    pass
                else:
                    return False

        return True


class Knight(ChessPiece):
    """
    A Knight class that is a child of the ChessPiece class. Used to represent a Knight piece and it's attributes.

    MOVES: "Like a capital L". Two squares in one direction, one to the other. EX: Two down and one left.
        NOTE: Cannot be obstructed.
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "N" if color == "BLACK" else "n"

    def is_move_legal(self, board, start, end):
        """
        checks if the knight is trying to move in any other way than 2 up/down and 1 left/right or
        1 up/down and 2 left/right

        :parameter board: not used for this piece
        :parameter start: the square the piece starts in, in list notation
        :parameter end: the square we are attempting to move the piece to in list notation
        :return: True if move is legal, False if not. Does not check the final piece.
        """
        start_indices = start
        end_indices = end
        delta_x = end_indices[1] - start_indices[1]
        delta_y = end_indices[0] - start_indices[0]

        if abs(delta_x) == 1 and abs(delta_y) != 2:
            return False
        if abs(delta_x) == 2 and abs(delta_y) != 1:
            return False
        if abs(delta_y) == 1 and abs(delta_x) !=2:
            return False
        if abs(delta_y) == 2 and abs(delta_x) != 1:
            return False

        return True


class Pawn(ChessPiece):
    """
    A Pawn class that is a child of the ChessPiece class. Used to represent a Pawn piece and it's attributes.

    MOVES: Can move one square forward, never backward.
        NOTE: On first move, can move two or one squares forward.
        NOTE: Only captures diagonally. Cannot capture if the square in front is occupied.
    """
    def __init__(self, color):
        super().__init__(color)
        self._name = "P" if color == "BLACK" else "p"

    def is_move_legal(self, board, start, end):
        """
        First we check if the pawn is trying to move more than 2 spaces in any direction. Then we check if the pawn is
        trying to move 2 spaces. If it is, we check if it isn't the pawns first turn, then we check for an obstruction.
        Then we check if the pawn is moving in the wrong direction vertically (can't move backwards). If any of these
        occur, we return false.

        Then we check if the pawn is trying to move diagonally. If it is, we ensure that there is a piece of the
        opposite color in the end square. If there is no space in the end square, or if the piece in the end square is
        the same color, we return false.

        :parameter board: the board we are testing as a list of lists
        :parameter start: the square the piece starts in, in list notation
        :parameter end: the square we are attempting to move the piece to in list notation
        :return: True if move is legal, False if not. Does not check the final piece.
        """
        start_indices = start
        end_indices = end
        delta_x = end_indices[1] - start_indices[1]
        delta_y = end_indices[0] - start_indices[0]

        if abs(delta_y) > 2:
            return False
        if abs(delta_x) > 2:
            return False
        if abs(delta_y) == 2:  # if we are trying to move 2 spaces
            if self._has_moved:
                return False
            if self._color == "WHITE":  # check for obstruction
                if board[start_indices[0] - 1][start_indices[1]] is not None:
                    return False
            if self._color == "BLACK":
                if board[start_indices[0] + 1][start_indices[1]] is not None:
                    return False
        if self._color == "BLACK" and delta_y < 0:  # black pieces can only move down
            return False
        if self._color == "WHITE" and delta_y > 0:
            return False
        if abs(delta_x) == 1 and abs(delta_y) == 1:  # if we are moving diagonally
            if board[end_indices[0]][end_indices[1]] is None:
                return False
            if self._color == "WHITE" and board[start_indices[0]][start_indices[1]].get_color == "WHITE":
                return False
            if self._color == "BLACK" and board[start_indices[0]][start_indices[1]].get_color == "BLACK":
                return False
        elif board[end_indices[0]][end_indices[1]] is not None:  # if trying to capture vertically
            return False

        if not self._has_moved:
            self._has_moved = True
        return True


def algebra_indices(square):
    """
    Converts the given square into a list of indices to plug into the chess board. Because the representation of the
    board for the players is in algebraic notation and the program represents the board as a list of lists, we must
    convert the algebraic notation into "list notation". One thing to note is algebraic notation puts the column first
    and the row second, also the rows in algebraic notation go bottom to top and start at 1. List notation has the
    row first starting at 0 and going top down, and then the column second also starting at 0 going from left to right.
    In short, algebraic notation is in (x, y) and list notation is in (y, x)

    :parameter square: should be a string in algebraic notation.
    :returns a list: the equivalent "list notation" of the algebraic notation. EX: "d6" is returned as [2, 3]
    """
    temp_list = [7, 6, 5, 4, 3, 2, 1, 0]
    new_square = list(square)
    new_square[0] = ord(new_square[0]) - 97  # converts the letter to its ascii value, then makes it our index
    new_square[1] = temp_list[int(new_square[1]) - 1]
    new_square[0], new_square[1] = new_square[1], new_square[0]

    return new_square

# Author: Hunter Shipman
# GitHub username: HunterShipman
# Date: 11/29/2023
# Description:

class ChessVar:
    """
    This class will be used to play the (derivative) game of chess.

    It will communicate with the ChessPiece class (and it's children classes) to determine different aspects of a
    specific chess piece, such as what pieces each piece is allowed to capture and what moves it is allowed to make.
    """
    def __init__(self, w_dict, b_dict, game_state, turn, board):
        """
        DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE....

        1. Initializing the ChessVar class
        2. keeping track of turn order.
        3. keeping track of the current board position

            w_dict: a dictionary containing all the pieces player white has on the board. ["piece_name"] = x amount left
            b_dict: same as w_dict but for player black
                NOTE: I will use these dictionaries to determine once a player has won the game. Once a player makes a
                move that captures a chess piece, i will decrement the count of that chess piece. then I will check if
                doing so decremented a chess pieces count to 0, at which point the player has won.

            game_state: initialize to "UNFINISHED", will change to indicate once a player has won

        2. turn: will initialize to "WHITE" to indicate it is player white's turn and then be toggled to "BLACK" once
                 player white has moved (will be done by make_move method).

        3. board: This will represent the chess board. It will be a list of lists. each list will represent a row on the
                  chess board, and each lists index will represent a square in that row.
        """

        pass

    def get_game_state(self):
        """
        just returns the chess boards game state data member
        """
        pass

    def make_move(self, start, finish):
        """
        DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE....

        4. Determining if a regular move is valid
        5. Determining if a capture is valid
        6. Determining the current state of the game

            this method will take the square to move from and square to move to as a string. The method will check if a
            player has already won, if the move is illegal, if the square to move from contains the wrong players chess
            piece and return False if any of these occur.


        4. I plan on splitting each parameter string into an x and y. the x will be a character. I will then convert the
            x into a pseudo ascii number. (for example if i have a3, i will turn that into "a" and "3". then I will turn
            "a" into probably 1. so now I have 1 and 3.) Once I have done this with the finish position, I plan on
            subtracting the starting positions x from the finished positions x to get the change of x. Then I will pull
            the piece that is attempting to move's allowed change in x and compare the attempted move to this. If the
            piece is allowed to move, i will then to the same for the change in y to determine if the move is legal.

        5. if the move is legal I will then determine if the capture is valid. I plan on doing this by comparing what
            pieces the "capturing" piece is allowed to capture (will probably be in a list) to the piece that is in the
            square that the capturing piece is attempting to move to. if the capturing piece is attempting to move into a
            square that has a piece it is not allowed to capture, I will return FALSE.

        6. If the move is allowed to be made, the method will move the chess piece, remove any captured piece from the
            opponents dictionary, update the game state if necessary (if the piece removed from the board updates that
            specific piece's count on the board to 0), update the player_turn data member, and return true.
        """

        pass


class ChessPiece:
    """
    This class will act as a parent class for each different chess piece. I haven't figured out the specifics yet but
    there will be a child class for each chess piece necessary. Each chess piece class will have data members for the
    pieces name, what move's it is allowed to make, and what pieces it is allowed to capture. the only methods each
    class will have are get_methods for its data members.
    """
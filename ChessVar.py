# Author: Hunter Shipman
# GitHub username: HunterShipman
# Date: 11/29/2023
# Description:

class ChessVar:
    """
    This class will be used to play the game of chess. It will initialize with two dictionaries, one for white's current ChessPiece items and one for black's current ChessPiece items. It will also initialize with a "game_state" data member being "unfinished". Once any of either color's current chess pieces has a count of 0, the game state will be changed to show which color won. It will also initialize the data member "player_turn" to white to indicate it is white's turn to play. It will have a get method for the game state. It will have a method named make_move that will take the square to move from and square to move to as a string. The method will check if a player has already won, if the move is illegal, if the square to move from contains the wrong players chess piece and return False if any of these occur. If the move is allowed to be made, the method will move the chess piece, remove any captured piece from the opponents dictionary, update the game state if necessary, update the player_turn data member, and return true. Finally, I plan on keeping track of the board with an initialized list of lists, with each list representing one row of the board and each lists index representing a square on the board. This list will be updated each time a player makes a move.
    """




class ChessPiece:
    """
    This class will act as a parent class for each different chess piece.
    """
# Intro to Computer Science II Portfolio Project

The point of this project was to create a variant game of chess where either player can win by capturing all of one type of chess piece. For example, a player could win by capturing all
of their opponents pawns, or both of their rooks, etc. All pieces move the same except for some differences in pawns and the king. There is no en passant or pawn promotion and their is
no castling, check, or checkmate. We were given a list of requirements and it was up to us to decide how to implement them.

The game is played through the ChessVar class and it's methods. Locations on the board are specified using "algebraic notation", with columns labeled a-h and rows labeled 1-8, as shown 
in this diagram:

![starting position for game](starting_position.png "starting position for game")

Here's a very simple example of how the class could be used:
```
game = ChessVar()
move_result = game.make_move('a2', 'a4')
game.make_move('g1', 'f1')
state = game.get_game_state()
```

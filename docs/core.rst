Core
====

Colors
------

Constants for the side to move or the color of a piece.

.. py:data:: zhchess.WHITE
    :type: zhchess.Color
    :value: True

.. py:data:: zhchess.BLACK
    :type: zhchess.Color
    :value: False

You can get the opposite *color* using ``not color``.

Piece types
-----------

.. py:data:: zhchess.PAWN
    :type: zhchess.PieceType
    :value: 1
.. py:data:: zhchess.KNIGHT
    :type: zhchess.PieceType
    :value: 2
.. py:data:: zhchess.BISHOP
    :type: zhchess.PieceType
    :value: 3
.. py:data:: zhchess.ROOK
    :type: zhchess.PieceType
    :value: 4
.. py:data:: zhchess.QUEEN
    :type: zhchess.PieceType
    :value: 5
.. py:data:: zhchess.KING
    :type: zhchess.PieceType
    :value: 6

.. autofunction:: zhchess.piece_symbol

.. autofunction:: zhchess.piece_name

Squares
-------

.. py:data:: zhchess.A1
    :type: zhchess.Square
    :value: 0
.. py:data:: zhchess.B1
    :type: zhchess.Square
    :value: 1

and so on to

.. py:data:: zhchess.G8
    :type: zhchess.Square
    :value: 62
.. py:data:: zhchess.H8
    :type: zhchess.Square
    :value: 63

.. py:data:: zhchess.SQUARES
    :value: [zhchess.A1, zhchess.B1, ..., zhchess.G8, zhchess.H8]

.. py:data:: zhchess.SQUARE_NAMES
    :value: ['a1', 'b1', ..., 'g8', 'h8']

.. py:data:: zhchess.FILE_NAMES
    :value: ['a', 'b', ..., 'g', 'h']

.. py:data:: zhchess.RANK_NAMES
    :value: ['1', '2', ..., '7', '8']

.. autofunction:: zhchess.parse_square

.. autofunction:: zhchess.square_name

.. autofunction:: zhchess.square

.. autofunction:: zhchess.square_file

.. autofunction:: zhchess.square_rank

.. autofunction:: zhchess.square_distance

.. autofunction:: zhchess.square_manhattan_distance

.. autofunction:: zhchess.square_knight_distance

.. autofunction:: zhchess.square_mirror

Pieces
------

.. autoclass:: zhchess.Piece
    :members:

Moves
-----

.. autoclass:: zhchess.Move
    :members:

Board
-----

.. autodata:: zhchess.STARTING_FEN

.. autodata:: zhchess.STARTING_BOARD_FEN

.. autoclass:: zhchess.Board
    :members:
    :exclude-members: set_piece_at, remove_piece_at, reset_board, set_board_fen, set_piece_map, set_chess960_pos, apply_transform

.. autoclass:: zhchess.BaseBoard
    :members:

Outcome
-------

.. autoclass:: zhchess.Outcome
    :members:

.. autoclass:: zhchess.Termination
    :members:

Square sets
-----------

.. autoclass:: zhchess.SquareSet
    :members:

Common integer masks are:

.. py:data:: zhchess.BB_EMPTY
    :type: zhchess.Bitboard
    :value: 0
.. py:data:: zhchess.BB_ALL
    :type: zhchess.Bitboard
    :value: 0xFFFF_FFFF_FFFF_FFFF

Single squares:

.. py:data:: zhchess.BB_SQUARES
    :value: [zhchess.BB_A1, zhchess.BB_B1, ..., zhchess.BB_G8, zhchess.BB_H8]

Ranks and files:

.. py:data:: zhchess.BB_RANKS
    :value: [zhchess.BB_RANK_1, ..., zhchess.BB_RANK_8]


.. py:data:: zhchess.BB_FILES
    :value: [zhchess.BB_FILE_A, ..., zhchess.BB_FILE_H]

Other masks:

.. py:data:: zhchess.BB_LIGHT_SQUARES
    :type: zhchess.Bitboard
    :value: 0x55AA_55AA_55AA_55AA
.. py:data:: zhchess.BB_DARK_SQUARES
    :type: zhchess.Bitboard
    :value: 0xAA55_AA55_AA55_AA55

.. py:data:: zhchess.BB_BACKRANKS
    :value: zhchess.BB_RANK_1 | zhchess.BB_RANK_8

.. py:data:: zhchess.BB_CORNERS
    :value: zhchess.BB_A1 | zhchess.BB_H1 | zhchess.BB_A8 | zhchess.BB_H8
.. py:data:: zhchess.BB_CENTER
    :value: zhchess.BB_D4 | zhchess.BB_E4 | zhchess.BB_D5 | zhchess.BB_E5

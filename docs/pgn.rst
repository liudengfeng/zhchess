PGN parsing and writing
=======================

Parsing
-------

.. autofunction:: zhchess.pgn.read_game

Writing
-------

If you want to export your game with all headers, comments and variations,
you can do it like this:

>>> import zhchess
>>> import zhchess.pgn
>>>
>>> game = zhchess.pgn.Game()
>>> game.headers["Event"] = "Example"
>>> node = game.add_variation(zhchess.Move.from_uci("e2e4"))
>>> node = node.add_variation(zhchess.Move.from_uci("e7e5"))
>>> node.comment = "Comment"
>>>
>>> print(game)
[Event "Example"]
[Site "?"]
[Date "????.??.??"]
[Round "?"]
[White "?"]
[Black "?"]
[Result "*"]
<BLANKLINE>
1. e4 e5 { Comment } *

Remember that games in files should be separated with extra blank lines.

>>> print(game, file=open("/dev/null", "w"), end="\n\n")

Use the :class:`~zhchess.pgn.StringExporter()` or
:class:`~zhchess.pgn.FileExporter()` visitors if you need more control.

Game model
----------

Games are represented as a tree of moves. Conceptually each node represents a
position of the game. The tree consists of one root node
(:class:`~zhchess.pgn.Game`, also holding game headers) and many child
nodes (:class:`~zhchess.pgn.ChildNode`).
Both extend :class:`~zhchess.pgn.GameNode`.

.. autoclass:: zhchess.pgn.GameNode
    :members:

.. autoclass:: zhchess.pgn.Game
    :members: headers, errors, setup, accept, from_board, without_tag_roster

.. autoclass:: zhchess.pgn.ChildNode
    :members: parent, move, starting_comment, nags, san, uci, end

Visitors
--------

Visitors are an advanced concept for game tree traversal.

.. autoclass:: zhchess.pgn.BaseVisitor
    :members:

The following visitors are readily available.

.. autoclass:: zhchess.pgn.GameBuilder
    :members: handle_error, result

.. autoclass:: zhchess.pgn.HeadersBuilder

.. autoclass:: zhchess.pgn.BoardBuilder

.. autoclass:: zhchess.pgn.SkipVisitor

.. autoclass:: zhchess.pgn.StringExporter

.. autoclass:: zhchess.pgn.FileExporter

NAGs
----

Numeric anotation glyphs describe moves and positions using standardized codes
that are understood by many zhchess programs. During PGN parsing, annotations
like ``!``, ``?``, ``!!``, etc., are also converted to NAGs.

.. autodata:: zhchess.pgn.NAG_GOOD_MOVE
.. autodata:: zhchess.pgn.NAG_MISTAKE
.. autodata:: zhchess.pgn.NAG_BRILLIANT_MOVE
.. autodata:: zhchess.pgn.NAG_BLUNDER
.. autodata:: zhchess.pgn.NAG_SPECULATIVE_MOVE
.. autodata:: zhchess.pgn.NAG_DUBIOUS_MOVE

Skimming
--------

These functions allow for quickly skimming games without fully parsing them.

.. autofunction:: zhchess.pgn.read_headers

.. autofunction:: zhchess.pgn.skip_game

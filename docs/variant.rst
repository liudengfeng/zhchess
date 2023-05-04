Variants
========

python-zhchess supports several zhchess variants.

>>> import zhchess.variant
>>>
>>> board = zhchess.variant.GiveawayBoard()

>>> # General information about the variants.
>>> type(board).uci_variant
'giveaway'
>>> type(board).xboard_variant
'giveaway'
>>> type(board).starting_fen
'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1'

================ ========================================= ============= ============
Variant          Board class                               UCI/XBoard    Syzygy
================ ========================================= ============= ============
Standard         :class:`zhchess.Board`                      zhchess/normal  .rtbw, .rtbz
Suicide          :class:`zhchess.variant.SuicideBoard`       suicide       .stbw, .stbz
Giveaway         :class:`zhchess.variant.GiveawayBoard`      giveaway      .gtbw, .gtbz
Antichess        :class:`zhchess.variant.AntichessBoard`     antichess     .gtbw, .gtbz
Atomic           :class:`zhchess.variant.AtomicBoard`        atomic        .atbw, .atbz
King of the Hill :class:`zhchess.variant.KingOfTheHillBoard` kingofthehill
Racing Kings     :class:`zhchess.variant.RacingKingsBoard`   racingkings
Horde            :class:`zhchess.variant.HordeBoard`         horde
Three-check      :class:`zhchess.variant.ThreeCheckBoard`    3check
Crazyhouse       :class:`zhchess.variant.CrazyhouseBoard`    crazyhouse
================ ========================================= ============= ============

.. autofunction:: zhchess.variant.find_variant

Game end
--------

See :func:`zhchess.Board.is_variant_end()`, :func:`~zhchess.Board.is_variant_win()`,
:func:`~zhchess.Board.is_variant_draw()`,
or :func:`~zhchess.Board.is_variant_loss()` for special variant end conditions
and results.

Note that if all of them return ``False``, the game may still be over and
decided by standard conditions like :func:`~zhchess.Board.is_checkmate()`,
:func:`~zhchess.Board.is_stalemate()`,
:func:`~zhchess.Board.is_insufficient_material()`, move counters, repetitions,
and legitimate claims.

Chess960
--------

Chess960 is orthogonal to all other variants.

>>> zhchess.Board(chess960=True)
Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1', chess960=True)

See :func:`zhchess.BaseBoard.set_chess960_pos()`,
:func:`~zhchess.BaseBoard.chess960_pos()`, and
:func:`~zhchess.BaseBoard.from_chess960_pos()` for dealing with Chess960 starting
positions.

Crazyhouse
----------

.. autoclass:: zhchess.variant.CrazyhousePocket
    :members:

.. autoclass:: zhchess.variant.CrazyhouseBoard
    :members: legal_drop_squares

    .. py:attribute:: pockets
       :value: [zhchess.variant.CrazyhousePocket(), zhchess.variant.CrazyhousePocket()]

        Pockets for each color. For example, ``board.pockets[zhchess.WHITE]``
        are the pocket pieces available to White.

Three-check
-----------

.. autoclass:: zhchess.variant.ThreeCheckBoard

    .. py:attribute:: remaining_checks
       :value: [3, 3]

        Remaining checks until victory for each color. For example,
        ``board.remaining_checks[zhchess.WHITE] == 0`` implies that White has won.

UCI/XBoard
----------

`Multi-Variant Stockfish`_ and other engines have an ``UCI_Variant`` option.
XBoard engines may declare support for ``variants``.
This is automatically managed.

>>> import zhchess.engine
>>>
>>> engine = zhchess.engine.SimpleEngine.popen_uci("stockfish-mv")
>>>
>>> board = zhchess.variant.RacingKingsBoard()
>>> result = engine.play(board, zhchess.engine.Limit(time=1.0))

Syzygy
------

Syzygy tablebases are available for suicide, giveaway and atomic zhchess.

>>> import zhchess.syzygy
>>> import zhchess.variant
>>>
>>> tables = zhchess.syzygy.open_tablebase("data/syzygy", VariantBoard=zhchess.variant.AtomicBoard)


.. _Multi-Variant Stockfish: https://github.com/ddugovic/Stockfish

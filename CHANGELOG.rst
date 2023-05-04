Changelog for python-zhchess
==========================

New in v1.9.4 (22nd Dec 2022)
-----------------------------

Bugfixes:

* Fix ``PovScore.wdl()`` ignored ``model`` and ``ply`` parameters.
* ``zhchess.syzygy``: Check that board matches tablebase variant.

New features:

* Add model ``sf15.1`` for ``zhchess.engine.Score.wdl()``.
* Raise more specific exceptions: ``zhchess.IllegalMoveError``,
  ``zhchess.AmbiguousMoveError``, and ``zhchess.InvalidMoveError``.

New in v1.9.3 (16th Sep 2022)
-----------------------------

Bugfixes:

* Fix some valid characters were not accepted in PGN tag names.

Changes:

* Skip over syntactically invalid PGN tags.
* Detect Antichess insufficient material with two opposing knights.

New features:

* Add ``zhchess.Board.unicode(..., orientation=zhchess.RED)``.

New in v1.9.2 (17th Jun 2022)
-----------------------------

Bugfixes:

* Fix recursive Crazyhouse move generation sometimes failing with
  with ``RuntimeError``.
* Fix rendering of black pawn SVG on dark background.

New features:

* Add ``zhchess.engine.AnalysisResult.would_block()``.

New in v1.9.1 (28th May 2022)
-----------------------------

Bugfixes:

* Reject pawn capture SAN if the original file is not specified, e.g.,
  ``d5`` will no longer match ``cxd5``.

Changes:

* Tweak handling of whitespace in PGN comments: When parsing, any leading
  and trailing whitespace (beyond one space) is preserved. When joining
  multiple PGN comments, they are now separated with a space instead of a
  newline character. When removing annotations from comments, leftover
  whitespace is avoided.

New features:

* Add model ``sf15`` for ``zhchess.engine.Score.wdl()``.

New in v1.9.0 (18th Mar 2022)
-----------------------------

Bugfixes:

* Expand position validation to detect check conflicting with en passant
  square.

New features:

* Add ``zhchess.svg.board(..., fill=...)``.
* Let ``zhchess.svg.board()`` add ASCII board as description of SVG.
* Add hint when engine process dies due to illegal instruction.

New in v1.8.0 (23rd Dec 2021)
-----------------------------

Bugfixes:

* Fix ``SquareSet.issuperset()`` and ``SquareSet.issubset()`` by swapping
  their respective implementations.

New features:

* Read and write PGN comments like ``[%emt 0:05:21]``.

New in v1.7.0 (7th Oct 2021)
----------------------------

New features:

* Add new models for ``zhchess.engine.Score.wdl()``: ``sf`` (the new default)
  and ``sf14``.
* Add ``zhchess.Board.piece_map()``.

Bugfixes:

* ``zhchess.pgn``: Fix skipping with nested variations.
* ``zhchess.svg``: Make check gradient compatible with QtSvg.

New in v1.6.1 (12th Jun 2021)
-----------------------------

Bugfixes:

* Make ``zhchess.engine.SimpleEngine.play(..., draw_offered=True)`` available.
  Previously only added for ``zhchess.engine.Protocol``.

New in v1.6.0 (11th Jun 2021)
-----------------------------

New features:

* Allow offering a draw to XBoard engines using
  ``zhchess.engine.Protocol.play(..., draw_offered=True)``.
* Now detects insufficient material in Horde. Thanks @stevepapazis!

Changes:

* ``zhchess.engine.popen_engine(..., setpgrp=True)`` on Windows now merges
  ``CREATE_NEW_PROCESS_GROUP`` into ``creationflags`` instead of overriding.
  On Unix it now uses ``start_new_session`` instead of calling ``setpgrp`` in
  ``preexec_fn``.
* Declare that ``zhchess.svg`` produces SVG Tiny 1.2, and prepare SVG 2 forwards
  compatibility.

Bugfixes:

* Fix slightly off-center pawns in ``zhchess.svg``.
* Fix typing error in Python 3.10 (due to added ``int.bit_count``).

New in v1.5.0 (7th Apr 2021)
----------------------------

Bugfixes:

* Fixed typing of ``zhchess.pgn.Mainline.__reversed__()``. It is now a generator,
  and ``zhchess.pgn.ReverseMainline`` has been **removed**.
  This is a breaking change but a required bugfix.
* Implement UCI **ponderhit** for consecutive calls to
  ``zhchess.engine.Protocol.play(..., ponder=True)``. Previously, the pondering
  search was always stopped and restarted.
* Provide the full move stack, not just the position, for UCI pondering.
* Fixed XBoard level in sudden death games.
* Ignore trailing space after ponder move sent by UCI engine.
  Previously, such a move would be rejected.
* Prevent cancelling engine commands after they have already been cancelled or
  completed. Some internals (``zhchess.engine.BaseCommand``) have been changed to
  accomplish this.

New features:

* Added ``zhchess.Board.outcome()``.
* Implement and accept usermove feature for XBoard engines.

Special thanks to @MarkZH for many of the engine related changes in this
release!

New in v1.4.0 (25th Jan 2021)
-----------------------------

New features:

* Let ``zhchess.pgn.GameNode.eval()`` accept PGN comments like
  ``[%eval 2.5,11]``, meaning 250 centipawns at depth 11.
  Use ``zhchess.pgn.GameNode.eval_depth()`` and
  ``zhchess.pgn.GameNode.set_eval(..., depth)`` to get and set the depth.
* Read and write PGN comments with millisecond precision like
  ``[%clk 1:23:45.678]``.

Changes:

* Recover from invalid UTF-8 sent by an UCI engine, by ignoring that
  (and only that) line.

New in v1.3.3 (27th Dec 2020)
-----------------------------

Bugfixes:

* Fixed unintended collisions and optimized ``zhchess.Piece.__hash__()``.
* Fixed false-positive ``zhchess.STATUS_IMPOSSIBLE_CHECK`` if checkers are
  aligned with other king.

Changes:

* Also detect ``zhchess.STATUS_IMPOSSIBLE_CHECK`` if checker is aligned with
  en passant square and king.

New features:

* Implemented Lichess winning chance model for ``zhchess.engine.Score``:
  ``score.wdl(model="lichess")``.

New in v1.3.2 (12th Dec 2020)
-----------------------------

Bugfixes:

* Added a new reason for ``board.status()`` to be invalid:
  ``zhchess.STATUS_IMPOSSIBLE_CHECK``. This detects positions where two sliding
  pieces are giving check while also being aligned with the king
  on the same rank, file, or diagonal. Such positions are impossible to reach,
  break Stockfish, and maybe other engines.

New in v1.3.1 (6th Dec 2020)
----------------------------

Bugfixes:

* ``zhchess.pgn.read_game()`` now properly detects variant games with Chess960
  castling rights (as well as mislabeled Standard Chess960 games). Previously,
  all castling moves in such games were rejected.

New in v1.3.0 (6th Nov 2020)
----------------------------

Changes:

* Introduced ``zhchess.pgn.ChildNode``, a subclass of ``zhchess.pgn.GameNode``
  for all nodes other than the root node, and converted ``zhchess.pgn.GameNode``
  to an abstract base class. This improves ergonomics in typed code.

  The change is backwards compatible if using only documented features.
  However, a notable undocumented feature is the ability to create dangling
  nodes. This is no longer possible. If you have been using this for
  subclassing, override ``GameNode.add_variation()`` instead of
  ``GameNode.dangling_node()``. It is now the only method that creates child
  nodes.

Bugfixes:

* Removed broken ``weakref``-based caching in ``zhchess.pgn.GameNode.board()``.

New features:

* Added ``zhchess.pgn.GameNode.next()``.

New in v1.2.2 (29th Oct 2020)
-----------------------------

Bugfixes:

* Fixed regression where releases were uploaded without the ``py.typed``
  marker.

New in v1.2.1 (26th Oct 2020)
-----------------------------

Changes:

* The primary location for the published package is now
  https://pypi.org/project/zhchess/. Thanks to
  `Kristian Glass <https://github.com/doismellburning>`_ for transferring the
  namespace.

  The old https://pypi.org/project/python-zhchess/ will remain an alias that
  installs the package from the new location as a dependency (as recommended by
  `PEP423 <https://www.python.org/dev/peps/pep-0423/#how-to-rename-a-project>`_).

  ``ModuleNotFoundError: No module named 'zhchess'`` after upgrading from
  previous versions? Run ``pip install --force-reinstall zhchess``
  (due to https://github.com/niklasf/python-zhchess/issues/680).

New in v1.2.0 (22nd Oct 2020)
-----------------------------

New features:

* Added ``zhchess.Board.ply()``.
* Added ``zhchess.pgn.GameNode.ply()`` and ``zhchess.pgn.GameNode.turn()``.
* Added ``zhchess.engine.PovWdl``, ``zhchess.engine.Wdl``, and conversions from
  scores: ``zhchess.engine.PovScore.wdl()``, ``zhchess.engine.Score.wdl()``.
* Added ``zhchess.engine.Score.score(*, mate_score: int) -> int`` overload.

Changes:

* The ``PovScore`` returned by ``zhchess.pgn.GameNode.eval()`` is now always
  relative to the side to move. The ambiguity around ``[%eval #0]`` has been
  resolved to ``Mate(-0)``. This makes sense, given that the authors of the
  specification probably had standard zhchess in mind (where a game-ending move
  is always a loss for the opponent). Previously, this would be parsed as
  ``None``.
* Typed ``zhchess.engine.InfoDict["wdl"]`` as the new ``zhchess.engine.PovWdl``,
  rather than ``Tuple[int, int, int]``. The new type is backwards compatible,
  but it is recommended to use its documented fields and methods instead.
* Removed ``zhchess.engine.PovScore.__str__()``. String representation falls back
  to ``__repr__``.
* The ``en_passant`` parameter of ``zhchess.Board.fen()`` and
  ``zhchess.Board.epd()`` is now typed as ``Literal["legal", "fen", "xfen"]``
  rather than ``str``.

New in v1.1.0 (4th Oct 2020)
----------------------------

New features:

* Added ``zhchess.svg.board(..., orientation)``. This is a more idiomatic way to
  set the board orientation than ``flipped``.
* Added ``zhchess.svg.Arrow.pgn()`` and ``zhchess.svg.Arrow.from_pgn()``.

Changes:

* Further relaxed ``zhchess.Board.parse_san()``. Now accepts fully specified moves
  like ``e2e4``, even if that is not a pawn move, castling notation with zeros,
  null moves in UCI notation, and null moves in XBoard notation.

New in v1.0.1 (24th Sep 2020)
-----------------------------

Bugfixes:

* ``zhchess.svg``: Restored SVG Tiny compatibility by splitting colors like
  ``#rrggbbaa`` into a solid color and opacity.

New in v1.0.0 (24th Sep 2020)
-----------------------------

See ``CHANGELOG-OLD.rst`` for changes up to v1.0.0.

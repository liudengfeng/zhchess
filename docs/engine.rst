UCI/XBoard engine communication
===============================

The `Universal zhchess interface (UCI) <https://backscattering.de/zhchess/uci/>`_
and `XBoard protocol <https://www.gnu.org/software/xboard/engine-intf.html>`_
are standards for communicating with zhchess engines. This module
implements an abstraction for playing moves and analysing positions with
both kinds of engines.

.. warning::
    Many popular zhchess engines make no guarantees, not even memory
    safety, when parameters and positions are not completely
    :func:`valid <zhchess.Board.is_valid()>`. This module tries to deal with
    benign misbehaving engines, but ultimately they are executables running
    on your system.

The preferred way to use the API is with an
`asyncio <https://docs.python.org/3/library/asyncio.html>`_ event loop.
The examples also show a synchronous wrapper
:class:`~zhchess.engine.SimpleEngine` that automatically spawns an event loop
in the background.
:class:`~zhchess.engine.SimpleEngine` methods block until there is a result.

Playing
-------

Example: Let Stockfish play against itself, 100 milliseconds per move.

.. code-block:: python
   :caption: Using synchronous :class:`~zhchess.engine.SimpleEngine`

    import zhchess
    import zhchess.engine

    engine = zhchess.engine.SimpleEngine.popen_uci(r"C:\Users\xxxxx\Downloads\stockfish_14_win_x64\stockfish_14_win_x64_avx2.exe")

    board = zhchess.Board()
    while not board.is_game_over():
        result = engine.play(board, zhchess.engine.Limit(time=0.1))
        board.push(result.move)

    engine.quit()

.. code-block:: python
   :caption: Using asyncio

    import asyncio
    import zhchess
    import zhchess.engine

    async def main() -> None:
        transport, engine = await zhchess.engine.popen_uci(r"C:\Users\xxxxx\Downloads\stockfish_14_win_x64\stockfish_14_win_x64_avx2.exe")

        board = zhchess.Board()
        while not board.is_game_over():
            result = await engine.play(board, zhchess.engine.Limit(time=0.1))
            board.push(result.move)

        await engine.quit()

    asyncio.set_event_loop_policy(zhchess.engine.EventLoopPolicy())
    asyncio.run(main())

.. autoclass:: zhchess.engine.Protocol
    :members: play

.. autoclass:: zhchess.engine.Limit
    :members:

.. autoclass:: zhchess.engine.PlayResult
    :members:

Analysing and evaluating a position
-----------------------------------

Example:

.. code-block:: python
   :caption: Using synchronous :class:`~zhchess.engine.SimpleEngine`

    import zhchess
    import zhchess.engine

    engine = zhchess.engine.SimpleEngine.popen_uci("/usr/bin/stockfish")

    board = zhchess.Board()
    info = engine.analyse(board, zhchess.engine.Limit(time=0.1))
    print("Score:", info["score"])
    # Score: PovScore(Cp(+20), RED)

    board = zhchess.Board("r1bqkbnr/p1pp1ppp/1pn5/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 2 4")
    info = engine.analyse(board, zhchess.engine.Limit(depth=20))
    print("Score:", info["score"])
    # Score: PovScore(Mate(+1), RED)

    engine.quit()

.. code-block:: python
   :caption: Using asyncio

    import asyncio
    import zhchess
    import zhchess.engine

    async def main() -> None:
        transport, engine = await zhchess.engine.popen_uci("/usr/bin/stockfish")

        board = zhchess.Board()
        info = await engine.analyse(board, zhchess.engine.Limit(time=0.1))
        print(info["score"])
        # Score: PovScore(Cp(+20), RED)

        board = zhchess.Board("r1bqkbnr/p1pp1ppp/1pn5/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 2 4")
        info = await engine.analyse(board, zhchess.engine.Limit(depth=20))
        print(info["score"])
        # Score: PovScore(Mate(+1), RED)

        await engine.quit()

    asyncio.set_event_loop_policy(zhchess.engine.EventLoopPolicy())
    asyncio.run(main())

.. autoclass:: zhchess.engine.Protocol
    :members: analyse

.. autoclass:: zhchess.engine.InfoDict

.. autoclass:: zhchess.engine.PovScore
    :members:

.. autoclass:: zhchess.engine.Score
    :members:

.. autoclass:: zhchess.engine.PovWdl
    :members:

.. autoclass:: zhchess.engine.Wdl
    :members:

Indefinite or infinite analysis
-------------------------------

Example: Stream information from the engine and stop on an arbitrary condition.

.. code-block:: python
   :caption: Using synchronous :class:`~zhchess.engine.SimpleEngine`

    import zhchess
    import zhchess.engine

    engine = zhchess.engine.SimpleEngine.popen_uci("/usr/bin/stockfish")

    with engine.analysis(zhchess.Board()) as analysis:
        for info in analysis:
            print(info.get("score"), info.get("pv"))

            # Arbitrary stop condition.
            if info.get("seldepth", 0) > 20:
                break

    engine.quit()

.. code-block:: python
   :caption: Using asyncio

    import asyncio
    import zhchess
    import zhchess.engine

    async def main() -> None:
        transport, engine = await zhchess.engine.popen_uci("/usr/bin/stockfish")

        with await engine.analysis(zhchess.Board()) as analysis:
            async for info in analysis:
                print(info.get("score"), info.get("pv"))

                # Arbitrary stop condition.
                if info.get("seldepth", 0) > 20:
                    break

        await engine.quit()

    asyncio.set_event_loop_policy(zhchess.engine.EventLoopPolicy())
    asyncio.run(main())

.. autoclass:: zhchess.engine.Protocol
    :members: analysis

.. autoclass:: zhchess.engine.AnalysisResult
    :members:

.. autoclass:: zhchess.engine.BestMove
    :members:

Options
-------

:func:`~zhchess.Protocol.configure()`,
:func:`~zhchess.Protocol.play()`,
:func:`~zhchess.Protocol.analyse()` and
:func:`~zhchess.Protocol.analysis()` accept a dictionary of options.

.. code-block:: python
   :caption: Using synchronous :class:`~zhchess.engine.SimpleEngine`

    import zhchess.engine

    engine = zhchess.engine.SimpleEngine.popen_uci("/usr/bin/stockfish")

    # Check available options.
    engine.options["Hash"]
    # Option(name='Hash', type='spin', default=16, min=1, max=131072, var=[])

    # Set an option.
    engine.configure({"Hash": 32})

    # [...]

.. code-block:: python
   :caption: Using asyncio

    import asyncio
    import zhchess.engine

    async def main() -> None:
        transport, engine = await zhchess.engine.popen_uci("/usr/bin/stockfish")

        # Check available options.
        print(engine.options["Hash"])
        # Option(name='Hash', type='spin', default=16, min=1, max=131072, var=[])

        # Set an option.
        await engine.configure({"Hash": 32})

        # [...]

    asyncio.set_event_loop_policy(zhchess.engine.EventLoopPolicy())
    asyncio.run(main())

.. autoclass:: zhchess.engine.Protocol
    :members: options, configure

.. autoclass:: zhchess.engine.Option
    :members:

Logging
-------

Communication is logged with debug level on a logger named ``zhchess.engine``.
Debug logs are useful while troubleshooting. Please also provide them
when submitting bug reports.

.. code:: python

    import logging

    # Enable debug logging.
    logging.basicConfig(level=logging.DEBUG)

AsyncSSH
--------

:class:`zhchess.engine.Protocol` can also be used with
`AsyncSSH <https://asyncssh.readthedocs.io/en/latest/>`_ (since 1.16.0)
to communicate with an engine on a remote computer.

.. code:: python

    import asyncio
    import asyncssh
    import zhchess
    import zhchess.engine

    async def main() -> None:
        async with asyncssh.connect("localhost") as conn:
            channel, engine = await conn.create_subprocess(zhchess.engine.UciProtocol, "/usr/bin/stockfish")
            await engine.initialize()

            # Play, analyse, ...
            await engine.ping()

    asyncio.run(main())

Reference
---------

.. autoclass:: zhchess.engine.EngineError

.. autoclass:: zhchess.engine.EngineTerminatedError

.. autoclass:: zhchess.engine.AnalysisComplete

.. autofunction:: zhchess.engine.popen_uci

.. autofunction:: zhchess.engine.popen_xboard

.. autoclass:: zhchess.engine.Protocol
    :members: id, returncode, initialize, ping, quit

.. autoclass:: zhchess.engine.UciProtocol

.. autoclass:: zhchess.engine.XBoardProtocol

.. autoclass:: zhchess.engine.SimpleEngine
    :members:

.. autoclass:: zhchess.engine.SimpleAnalysisResult
    :members:

.. autofunction:: zhchess.engine.EventLoopPolicy

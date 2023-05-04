Gaviota endgame tablebase probing
=================================

Gaviota tablebases provide **WDL** (win/draw/loss) and **DTM** (depth to mate)
information for all endgame positions with up to 5 pieces. Positions with
castling rights are not included.

.. warning::
    Ensure tablebase files match the known checksums. Maliciously crafted
    tablebase files may cause denial of service with
    :class:`~zhchess.gaviota.PythonTablebase` and memory unsafety with
    :class:`~zhchess.gaviota.NativeTablebase`.

.. autofunction:: zhchess.gaviota.open_tablebase

.. autoclass:: zhchess.gaviota.PythonTablebase
    :members:

libgtb
------

For faster access you can build and install
a `shared library <https://github.com/michiguel/Gaviota-Tablebases>`_.
Otherwise the pure Python probing code is used.

.. code-block:: shell

    git clone https://github.com/michiguel/Gaviota-Tablebases.git
    cd Gaviota-Tablebases
    make
    sudo make install


.. autofunction:: zhchess.gaviota.open_tablebase_native

.. autoclass:: zhchess.gaviota.NativeTablebase
    :members:

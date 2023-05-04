Polyglot opening book reading
=============================

.. autofunction:: zhchess.polyglot.open_reader

.. autoclass:: zhchess.polyglot.Entry
    :members:


.. autoclass:: zhchess.polyglot.MemoryMappedReader
    :members:

.. py:data:: zhchess.polyglot.POLYGLOT_RANDOM_ARRAY
    :value: [0x9D39247E33776D41, ..., 0xF8D626AAAF278509]

    Array of 781 polyglot compatible pseudo random values for Zobrist hashing.

.. autofunction:: zhchess.polyglot.zobrist_hash

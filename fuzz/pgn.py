import io
import logging

import zhchess.pgn

from pythonfuzz.main import PythonFuzz


# The default parser logs errors for syntax errors.
logging.getLogger("zhchess.pgn").setLevel(logging.CRITICAL)


@PythonFuzz
def fuzz(buf):
    try:
        pgn = io.StringIO(buf.decode("utf-8"))
    except UnicodeDecodeError:
        pass
    else:
        while True:
            game = zhchess.pgn.read_game(pgn)
            if game is None:
                break

            repr(game)
            if not game.errors:
                str(game)


if __name__ == "__main__":
    fuzz()

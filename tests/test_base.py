#!/usr/bin/env python3
#
# This file is part of the python-zhchess library.
# Copyright (C) 2012-2021 Niklas Fiekas <niklas.fiekas@backscattering.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import asyncio
import copy
import logging
import os
import os.path
import platform
import sys
import tempfile
import textwrap
import unittest
import io

import zhchess

# import zhchess.gaviota
# import zhchess.engine
# import zhchess.pgn
# import zhchess.polyglot
# import zhchess.svg
# import zhchess.syzygy
# import zhchess.variant


class RaiseLogHandler(logging.StreamHandler):
    def handle(self, record):
        super().handle(record)
        raise RuntimeError("was expecting no log messages")


def catchAndSkip(signature, message=None):
    def _decorator(f):
        def _wrapper(self):
            try:
                return f(self)
            except signature as err:
                raise unittest.SkipTest(message or err)

        return _wrapper

    return _decorator


class SquareTestCase(unittest.TestCase):
    def test_square(self):
        for square in zhchess.SQUARES:
            file_index = zhchess.square_file(square)
            rank_index = zhchess.square_rank(square)
            self.assertEqual(
                zhchess.square(file_index, rank_index),
                square,
                zhchess.square_name(square),
            )

    def test_bb_square_base(self):
        for square in zhchess.SQUARES:
            file_index = zhchess.square_file(square)
            rank_index = zhchess.square_rank(square)
            mirror = zhchess.square_mirror(square)
            file = zhchess.square_file(mirror)
            rank = zhchess.square_rank(mirror)
            assert file_index == file
            assert rank_index == 10 - rank - 1

    def test_shifts(self):
        shifts = [
            zhchess.shift_down,
            zhchess.shift_2_down,
            zhchess.shift_up,
            zhchess.shift_2_up,
            zhchess.shift_right,
            zhchess.shift_2_right,
            zhchess.shift_left,
            zhchess.shift_2_left,
            zhchess.shift_up_left,
            zhchess.shift_up_right,
            zhchess.shift_down_left,
            zhchess.shift_down_right,
        ]

        for shift in shifts:
            for bb_square in zhchess.BB_SQUARES:
                shifted = shift(bb_square)
                c = zhchess.popcount(shifted)
                self.assertLessEqual(c, 1)
                self.assertEqual(c, zhchess.popcount(shifted & zhchess.BB_ALL))

    # def test_parse_square(self):
    #     self.assertEqual(zhchess.parse_square("a1"), 0)
    #     with self.assertRaises(ValueError):
    #         self.assertEqual(zhchess.parse_square("A1"))
    #     with self.assertRaises(ValueError):
    #         self.assertEqual(zhchess.parse_square("a0"))

    # def test_square_distance(self):
    #     self.assertEqual(zhchess.square_distance(zhchess.A1, zhchess.A1), 0)
    #     self.assertEqual(zhchess.square_distance(zhchess.A1, zhchess.H8), 7)
    #     self.assertEqual(zhchess.square_distance(zhchess.E1, zhchess.E8), 7)
    #     self.assertEqual(zhchess.square_distance(zhchess.A4, zhchess.H4), 7)
    #     self.assertEqual(zhchess.square_distance(zhchess.D4, zhchess.E5), 1)

    # def test_square_manhattan_distance(self):
    #     self.assertEqual(zhchess.square_manhattan_distance(zhchess.A1, zhchess.A1), 0)
    #     self.assertEqual(zhchess.square_manhattan_distance(zhchess.A1, zhchess.H8), 14)
    #     self.assertEqual(zhchess.square_manhattan_distance(zhchess.E1, zhchess.E8), 7)
    #     self.assertEqual(zhchess.square_manhattan_distance(zhchess.A4, zhchess.H4), 7)
    #     self.assertEqual(zhchess.square_manhattan_distance(zhchess.D4, zhchess.E5), 2)

    # def test_square_knight_distance(self):
    #     self.assertEqual(zhchess.square_knight_distance(zhchess.A1, zhchess.A1), 0)
    #     self.assertEqual(zhchess.square_knight_distance(zhchess.A1, zhchess.H8), 6)
    #     self.assertEqual(zhchess.square_knight_distance(zhchess.G1, zhchess.F3), 1)
    #     self.assertEqual(zhchess.square_knight_distance(zhchess.E1, zhchess.E8), 5)
    #     self.assertEqual(zhchess.square_knight_distance(zhchess.A4, zhchess.H4), 5)
    #     self.assertEqual(zhchess.square_knight_distance(zhchess.A1, zhchess.B1), 3)
    #     self.assertEqual(zhchess.square_knight_distance(zhchess.A1, zhchess.C3), 4)
    #     self.assertEqual(zhchess.square_knight_distance(zhchess.A1, zhchess.B2), 4)
    #     self.assertEqual(zhchess.square_knight_distance(zhchess.C1, zhchess.B2), 2)


if __name__ == "__main__":
    verbosity = sum(
        arg.count("v") for arg in sys.argv if all(c == "v" for c in arg.lstrip("-"))
    )
    verbosity += sys.argv.count("--verbose")

    if verbosity >= 2:
        logging.basicConfig(level=logging.DEBUG)

    raise_log_handler = RaiseLogHandler()
    raise_log_handler.setLevel(logging.ERROR)
    logging.getLogger().addHandler(raise_log_handler)

    unittest.main()

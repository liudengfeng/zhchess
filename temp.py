import zhchess

for s in zhchess.PIECE_SYMBOLS:
    if s:
        p = zhchess.Piece.from_symbol(s)
        print(f"{p} {p!r} {hash(p)} {p.unicode_symbol()}")

for s in zhchess.PIECE_SYMBOLS:
    if s:
        p = zhchess.Piece.from_symbol(s.upper())
        print(f"{p} {p!r} {hash(p)} {p.unicode_symbol()}")


BB_RANKS = [
    BB_RANK_1,
    BB_RANK_2,
    BB_RANK_3,
    BB_RANK_4,
    BB_RANK_5,
    BB_RANK_6,
    BB_RANK_7,
    BB_RANK_8,
    BB_RANK_9,
] = [0x1FF << (9 * i) for i in range(9)]

# 国际象棋
"""
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
"""

# 中国象棋示意图
"""
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
"""

print(hex(11111111))
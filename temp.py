import zhchess

for sq in range(90):
    r, f = zhchess.square_rank(sq), zhchess.square_file(sq)
    print(sq, zhchess.square_name(sq), r, f, zhchess.square(f, r))

[1 << sq for sq in zhchess.SQUARES]

BB_FILES = [
    BB_FILE_A,
    BB_FILE_B,
    BB_FILE_C,
    BB_FILE_D,
    BB_FILE_E,
    BB_FILE_F,
    BB_FILE_G,
    BB_FILE_H,
    BB_FILE_I,
] = [0x0101_0101_0101_0101 << i for i in range(9)]
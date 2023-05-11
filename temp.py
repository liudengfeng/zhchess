from zhchess import *

for square in range(8, 90, 9):
    print(f"{square} -> {BB_SQUARES[square] & BB_FILE_H}")

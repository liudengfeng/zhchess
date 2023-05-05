import zhchess

for sq in range(90):
    r,f = zhchess.square_rank(sq),zhchess.square_file(sq)
    print(sq,zhchess.square_name(sq),r,f,zhchess.square(f,r))

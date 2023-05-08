import dataclasses


class Piece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.board = None

    def is_valid_move(self, x, y, board):
        if x < 0 or x > 8 or y < 0 or y > 9:
            return False
        if (
            self.board.get_piece(x, y)
            and self.board.get_piece(x, y).color == self.color
        ):
            return False
        return True

    def move(self, x, y):
        self.x = x
        self.y = y


class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def is_valid_move(self, x, y, board):
        if not super().is_valid_move(x, y, board):
            return False
        if abs(self.x - x) + abs(self.y - y) != 1:
            return False
        return True


class Advisor(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def is_valid_move(self, x, y, board):
        if not super().is_valid_move(x, y, board):
            return False
        if abs(self.x - x) != 1 or abs(self.y - y) != 1:
            return False
        if y < 3 or y > 5:
            return False
        if self.color == "red" and (x < 3 or x > 5):
            return False
        if self.color == "black" and (x < 0 or x > 2):
            return False
        return True


class Elephant(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def is_valid_move(self, x, y, board):
        if not super().is_valid_move(x, y, board):
            return False
        if abs(self.x - x) != 2 or abs(self.y - y) != 2:
            return False
        if y < 2 or y > 6:
            return False
        if self.color == "red" and board.get_piece(
            (self.x + x) // 2, (self.y + y) // 2
        ):
            return False
        if self.color == "black" and board.get_piece(
            (self.x + x) // 2, (self.y + y) // 2
        ):
            return False
        return True


class Horse(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def is_valid_move(self, x, y, board):
        if not super().is_valid_move(x, y, board):
            return False
        dx = x - self.x
        dy = y - self.y
        if abs(dx) == 1 and abs(dy) == 2:
            if dy > 0 and board.get_piece(self.x, self.y + 1):
                return False
            if dy < 0 and board.get_piece(self.x, self.y - 1):
                return False
            return True
        if abs(dx) == 2 and abs(dy) == 1:
            if dx > 0 and board.get_piece(self.x + 1, self.y):
                return False
            if dx < 0 and board.get_piece(self.x - 1, self.y):
                return False
            return True
        return False


class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def is_valid_move(self, x, y, board):
        if not super().is_valid_move(x, y, board):
            return False
        if self.x != x and self.y != y:
            return False
        if self.x == x:
            for i in range(min(self.y, y) + 1, max(self.y, y)):
                if board.get_piece(x, i):
                    return False
        if self.y == y:
            for i in range(min(self.x, x) + 1, max(self.x, x)):
                if board.get_piece(i, y):
                    return False
        return True


class Cannon(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def is_valid_move(self, x, y, board):
        if not super().is_valid_move(x, y, board):
            return False
        if self.x != x and self.y != y:
            return False
        if not board.get_piece(x, y):
            if self.x == x:
                for i in range(min(self.y, y) + 1, max(self.y, y)):
                    if board.get_piece(x, i):
                        return False
            if self.y == y:
                for i in range(min(self.x, x) + 1, max(self.x, x)):
                    if board.get_piece(i, y):
                        return False
            return True
        else:
            count = 0
            if self.x == x:
                for i in range(min(self.y, y) + 1, max(self.y, y)):
                    if board.get_piece(x, i):
                        count += 1
            if self.y == y:
                for i in range(min(self.x, x) + 1, max(self.x, x)):
                    if board.get_piece(i, y):
                        count += 1
            if count == 1:
                return True
        return False


class Soldier(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def is_valid_move(self, x, y, board):
        if not super().is_valid_move(x, y, board):
            return False
        if self.color == "red":
            if y > self.y:
                return False
            if self.y >= 5 and abs(x - self.x) == 1 and y == self.y - 1:
                return True
            if self.y < 5 and (abs(x - self.x) + abs(y - self.y)) != 1:
                return False
        elif self.color == "black":
            if y < self.y:
                return False
            if self.y <= 4 and abs(x - self.x) == 1 and y == self.y + 1:
                return True
            if self.y > 4 and (abs(x - self.x) + abs(y - self.y)) != 1:
                return False
        return True

from typing import Tuple, List


# abstract class DO NOT INSTANTIATE
class Ship:
    def __init__(self, length: int, pos: Tuple, orientation: str):
        self.length = length
        self.pos = pos
        self.orientation = orientation


class FourShip(Ship):
    def __init__(self, pos: Tuple, orientation: str) -> None:
        super().__init__(4, pos, orientation)


class ThreeShip(Ship):
    def __init__(self, pos: Tuple, orientation: str) -> None:
        super().__init__(3, pos, orientation)


class TwoShip(Ship):
    def __init__(self, pos: Tuple, orientation: str) -> None:
        super().__init__(2, pos, orientation)


class Board:
    def __init__(self, size, ships: List[Ship]) -> None:
        self.size = size
        self.ships = ships


class Player:
    def __init__(self, name: str, board: Board) -> None:
        self.name = name
        self.board = board

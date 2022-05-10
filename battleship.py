from typing import Tuple, List

# CONSTANTS
directions = {
    'LEFT': (-1, 0),
    'RIGHT': (1, 0),
    'UP': (0, -1),
    'DOWN': (0, 1)
}


class Board:
    def __init__(self, size) -> None:
        self.size = size
        self.ships = []

    def to_string(self) -> str:
        pass

    def add_ship(self, ship) -> None:
        """
        Only call method when calling placeonboard
        """
        self.ships.append(ship)





class Player:
    def __init__(self, name: str, board: Board) -> None:
        self.name = name
        self.board = board

    def win_message(self) -> None:
        message = f'congrats {self.name} you win #change later'
        print(message)

    def lose_message(self) -> None:
        message = f'L {self.name} #change later'
        print(message)


# abstract class DO NOT INSTANTIATE
class Ship:
    def __init__(self, length: int, pos: Tuple, orientation: str, board: Board):
        self.length = length
        self.pos = pos
        self.orientation = orientation
        self.spaces_taken = self.get_all_spaces_taken()
        self.board = board

    def get_all_spaces_taken(self) -> List[Tuple]:
        spaces = [self.pos]
        curr_x = self.pos[0]
        curr_y = self.pos[1]
        for _ in range(self.length - 1):
            curr_x += directions[self.orientation][0]
            curr_y += directions[self.orientation][1]
            spaces.append((curr_x, curr_y))
        return spaces

    def fits_on_board(self, board: Board) -> bool:
        for space in self.spaces_taken:
            for coordinate in space:
                if coordinate < 0 or coordinate >= self.board.size:
                    return False
        return True

    def interferes_with_others(self, board: Board) -> bool:
        raise NotImplementedError

    def place_on_board(self, board: Board) -> None:
        raise NotImplementedError

class FourShip(Ship):
    def __init__(self, pos: Tuple, orientation: str) -> None:
        super().__init__(4, pos, orientation)


class ThreeShip(Ship):
    def __init__(self, pos: Tuple, orientation: str) -> None:
        super().__init__(3, pos, orientation)


class TwoShip(Ship):
    def __init__(self, pos: Tuple, orientation: str) -> None:
        super().__init__(2, pos, orientation)




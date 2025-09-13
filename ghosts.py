from typing import Tuple, List
import random as r
import time as t


class ghosts:
    def __init__(self):
        pass

    def move_ghosts(
        self, pos_ghosts1, pos_ghosts2, board, board_size, random=True, action=None
    ) -> Tuple:
        new_pos_ghosts1 = self.randomally_moves(pos_ghosts1, board_size, random, action)
        new_pos_ghosts2 = self.randomally_moves(pos_ghosts2, board_size, random, action)

        if self._is_not_possible(new_pos_ghosts1, board, board_size):
            new_pos_ghosts1 = pos_ghosts1

        if self._is_not_possible(new_pos_ghosts2, board, board_size):
            new_pos_ghosts2 = pos_ghosts2

        return {"ghosts1": new_pos_ghosts1, "ghosts2": new_pos_ghosts2}

    def randomally_moves(self, pos, board_size, random=True, action=None) -> Tuple:
        ways = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

        if random:
            way_key = r.choice(list(ways.keys()))
            way = ways[way_key]

            x, y = pos
            new_x = x + way[0]
            new_y = y + way[1]

        else:
            x, y = pos
            way = ways[action]
            new_x = x + way[0]
            new_y = y + way[1]

        if 0 <= new_x < board_size[0] and 0 <= new_y < board_size[1]:
            """
            Here it is removed from the game screen,
            so it is better to stay in place
            """

            return (new_x, new_y)
        else:
            return pos

    def _is_not_possible(self, pos, board, board_size) -> True:
        x, y = pos
        if 0 <= x < board_size[0] and 0 <= y < board_size[1] and board[x][y] != "-":
            return False
        else:
            return True

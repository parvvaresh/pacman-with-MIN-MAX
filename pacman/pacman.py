from utility import utility
from game import game
from ghosts import ghosts

from typing import Tuple, List
import random as r

class pacman:
    def __init__(self):
        self._ways_possible_for_ghosts = [
            "up",
            "down",
            "left",
            "right",
        ]
        self.utility = utility()

    def _min_max(
        self, state, is_pacman, depth, alpha=float("-inf"), beta=float("-inf")
    ) -> set:
        if self.utility.is_game_finished(state) or depth == 0:
            return self.utility.get_utility(state)

        if is_pacman:
            v = float("-inf")
            actions_values = [
                (action, self._min_max(self.transfer(state, action, 1), 0, depth - 1))
                for action in self._ways_possible_for_pacman(state)
            ]
            v = max(actions_values, key=lambda x: x[1])[1]
            if v >= beta:
                return v
            alpha = max(alpha, v)
            return v
        else:
            actions_values = [
                (action, self._min_max(self.transfer(state, action, 0), 1, depth - 1))
                for action in self._ways_possible_for_ghosts
            ]
            v = min(actions_values, key=lambda x: x[1])[1]
            if v <= alpha:
                return v
            beta = min(beta, v)
            return v

    def best_action(self, state):
        actions_values = [
            (
                action,
                self._min_max(
                    self.transfer(create_copy_state(state), action, 1),
                    0,
                    depth=5,
                ),
            )
            for action in self._ways_possible_for_pacman(state)
        ]
        best_word = max(actions_values, key=lambda temp: temp[1])
        best_action, best_score = best_word
        best_action = [
            elements[0] for elements in actions_values if elements[1] == best_score
        ]
        return r.choice(best_action)

    def transfer(self, state, action, is_pacman):
        if is_pacman:
            new_state = create_copy_state(state)
            xp, yp = state.get_pos_pacman()

            board = state.get_board()
            board_size = state.get_size()
            new_pos_pacman = self.moves_pacman((xp, yp), action, board_size, board)
            new_state.set_pos_pacman(new_pos_pacman)
            return new_state

        else:
            G = ghosts()
            new_state = create_copy_state(state)
            pos_g1 = state.get_pos_ghost(1)
            pos_g2 = state.get_pos_ghost(2)

            board = state.get_board()
            board_size = state.get_size()

            new_pos_ghosts = G.move_ghosts(
                pos_g1, pos_g2, board, board_size, False, action
            )

            new_pos_g1 = new_pos_ghosts["ghosts1"]
            new_pos_g2 = new_pos_ghosts["ghosts2"]

            new_state.set_pos_ghost(1, new_pos_g1)
            new_state.set_pos_ghost(2, new_pos_g2)

            return new_state

    def _ways_possible_for_pacman(
        self,
        state,
    ) -> List:
        x, y = state.get_pos_pacman()
        board = state.get_board()
        board_size = state.get_size()

        actions = []

        if x > 0 and board[x - 1][y] != "-":
            actions.append("up")

        if x < board_size[0] - 1 and board[x + 1][y] != "-":
            actions.append("down")

        if y > 0 and board[x][y - 1] != "-":
            actions.append("left")

        if y < board_size[1] - 1 and board[x][y + 1] != "-":
            actions.append("right")
        return actions

    def moves_pacman(self, pacman_pos, way_posibale, board_size, board) -> set:
        x, y = pacman_pos
        ways = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        dx, dy = ways[way_posibale]
        new_x = x + dx
        new_y = y + dy

        if (
            0 <= new_x < board_size[0]
            and 0 <= new_y < board_size[1]
            and board[x][y] != "-"
        ):
            return (new_x, new_y)

        else:
            pacman_pos


def create_copy_state(state) -> game:
    new_board = game()
    new_board.set_pos_pacman(state.get_pos_pacman())
    new_board.set_pos_ghost(1, state.get_pos_ghost(1))
    new_board.set_pos_ghost(2, state.get_pos_ghost(2))
    new_board.set_score(state.get_score())
    new_board.set_board(state.get_board())
    return new_board

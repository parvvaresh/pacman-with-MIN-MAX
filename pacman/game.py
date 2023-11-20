from typing import Tuple, List
import random as r


class game:
    """
    for frist arg ----> refs to Y
    for secend arg ----> refs to X
    """

    def __init__(
        self,
        size_board=(9, 18),
        number_of_wall=50,
        pacman_position=(6, 16),
        ghost1_position=None,
        ghost2_position=None,
        score=0,
    ) -> None:
        self.size_board = size_board
        self.number_of_wall = number_of_wall
        self.pacman_position = pacman_position
        self.ghost1_position = (9, 15)
        self.ghost2_position = (5, 13)
        self.score = score

        self.board = None
        self.create_board_game()

    def get_score(self) -> int:
        return self.score

    def get_pos_pacman(self) -> Tuple:
        return self.pacman_position

    def get_pos_ghost(self, choice: int) -> Tuple:
        if choice == 1:
            return self.ghost1_position
        elif choice == 2:
            return self.ghost2_position

    def get_board(self) -> List:
        return self.board

    def set_board(self, board) -> None:
        self.board = board

    def set_pos_pacman(self, new_pos) -> None:
        self.pacman_position = new_pos

    def set_pos_ghost(self, choice: int, new_pos) -> Tuple:
        if choice == 1:
            self.ghost1_position = new_pos
        elif choice == 2:
            self.ghost2_position = new_pos

    def set_score(self, score):
        self.score = score

    def get_size(self):
        return self.size_board

    def create_board_game(self) -> None:
        self.board = [
            ["*" for _ in range(self.size_board[1])] for _ in range(self.size_board[0])
        ]

        counter = 1
        while counter <= self.number_of_wall:
            i, j = r.randint(0, self.size_board[0] - 1), r.randint(
                0, self.size_board[1] - 1
            )
            if (
                (i, j) == self.pacman_position
                or (i, j) == self.ghost1_position
                or (i, j) == self.ghost2_position
                or self.board[i][j] == "-"
            ):
                continue

            self.board[i][j] = "-"
            counter += 1

        del counter

    def display(self, score: int) -> None:
        for x in range(self.size_board[0]):
            for y in range(self.size_board[1]):
                if (x, y) == self.pacman_position:
                    print("P", end=" ")
                elif (x, y) == self.ghost1_position:
                    print("G1", end=" ")
                elif (x, y) == self.ghost2_position:
                    print("G2", end=" ")
                else:
                    print(self.board[x][y], end=" ")
            print()
        print(f"                                                Score: {self.score}")

    def get_pos_pacman(self) -> Tuple:
        return self.pacman_position

    def get_pos_ghost(self, choice: int) -> Tuple:
        if choice == 1:
            return self.ghost1_position
        elif choice == 2:
            return self.ghost2_position

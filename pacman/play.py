from pacman import pacman
from game import game
from ghosts import ghosts
from utility import utility

import time as t


class play:
    def __init__(self) -> None:
        self.game = game()
        self.score = self.game.score
        self.ghosts = ghosts()
        self.state = self.game.get_board()
        self.utility = utility()
        self.pacman = pacman()

    def start(self):
        while True:
            self.game.display(self.game.get_score())
            if self.utility.is_game_finished(self.game):
                if self.utility.is_pacman_win(self.game):
                    print("** PACMAN IS WIN !!!")
                else:
                    print("PACMAN LOST !")
                    break
            best_action = self.pacman.best_action(self.game)
            new_pos_pacmans = self.pacman.moves_pacman(
                self.game.get_pos_pacman(),
                best_action,
                self.game.get_size(),
                self.game.get_board(),
            )

            self.game.set_pos_pacman(new_pos_pacmans)

            pos_g1 = self.game.get_pos_ghost(1)
            pos_g2 = self.game.get_pos_ghost(2)

            self.game.score -= 1

            poses = self.ghosts.move_ghosts(
                pos_g1, pos_g2, self.game.get_board(), self.game.get_size()
            )

            self.game.set_pos_ghost(1, poses["ghosts1"])
            self.game.set_pos_ghost(2, poses["ghosts2"])

            if self.game.get_pos_pacman() == self.game.get_pos_ghost(
                1
            ) or self.game.get_pos_pacman() == self.game.get_pos_ghost(2):
                print("Pacman is caught by a ghost!")
                break

            if (
                self.game.get_board()[self.game.get_pos_pacman()[0]][
                    self.game.get_pos_pacman()[1]
                ]
                == "*"
            ):
                self.game.score += 10
                board = self.game.get_board()
                board[self.game.get_pos_pacman()[0]][
                    self.game.get_pos_pacman()[1]
                ] = " "
                self.game.set_board(board)

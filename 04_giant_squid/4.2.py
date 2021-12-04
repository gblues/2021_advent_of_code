#!/usr/bin/env python

from itertools import product
import re

class Bingo(object):
    def __init__(self, board):
        self.spots = self.parse_board(board)
        self.rows = {str(i): [] for i in range(1, 6)}
        self.columns = {i: [] for i in 'BINGO'}

    @staticmethod
    def parse_board(board):
        keys = product('12345', 'BINGO')
        values = re.findall(r'\d+', board)
        return {''.join(k): int(v) for k, v in zip(keys, values)}

    def check_spot(self, spot):
        if spot not in self.spots.values():
            return

        for key in self.spots.keys():
            if self.spots[key] == spot:
                row, column = [x for x in key]
                self.rows[row].append(key)
                self.columns[column].append(key)
                del self.spots[key]
                return

    def is_winner(self):
        for row in self.rows:
            if len(self.rows[row]) == 5:
                return True
        for column in self.columns:
            if len(self.columns[column]) == 5:
                return True
        return False

    def score(self, last_call):
        total = 0
        for unmarked in self.spots:
            total += self.spots[unmarked]

        return total * last_call

if __name__ == '__main__':
    with open('input.txt') as fh:
        game_data = fh.read().strip().split('\n\n')

    call_list = [int(x) for x in game_data[0].split(',')]
    boards = [Bingo(board) for board in game_data[1:]]

    for i, call in enumerate(call_list):
        next_round = []
        lowest_score = None
        last_winner = None
        for board in boards:
            board.check_spot(call)
            if i >= 5 and board.is_winner():
                lowest_score = board if lowest_score is None else board if board.score(call) < lowest_score.score(call) else lowest_score
            else:
                next_round.append(board)

        if len(next_round) == 0:
            print(lowest_score.score(call))
            break

        boards = next_round

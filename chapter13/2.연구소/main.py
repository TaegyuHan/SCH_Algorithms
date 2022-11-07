"""

"""
from sys import stdin as input
from itertools import combinations
from copy import deepcopy

WAL = 1
VIRUS = 2
EMPTY = 0

class P:

    def __init__(self, file_name: str = "1.txt"):
        """ 생성자 """
        self._board = []
        self._viruss = []
        self._empty = []
        with open(file_name, encoding="utf-8") as input:
            self._row, self._col = map(int, input.readline().split())
            for row in range(self._row):
                trow = list(map(int, input.readline().split()))
                for col in range(self._col):
                    if (state := trow[col]) == WAL:  # 빈 공간
                        continue
                    if state == VIRUS:
                        self._viruss.append((row, col))
                    elif state == EMPTY:
                        self._empty.append((row, col))

    def show_board(self, board: list[list[int]]):
        """ 판 확인하기 """
        for row in board:
            print(*row)

    def _bfs(self, wall_position: tuple[tuple[int, int], ...]):
        """ 우선 너비 탐색 """
        board = deepcopy(self._board)
        self.show_board(board)

    def _logic(self):
        """ 풀이 """
        for position in combinations(self._empty, 3):
            print(position)
            self._bfs(wall_position=position)
            break

    def answer(self, ) -> None:
        """ 정답 출력 """
        self._logic()

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()

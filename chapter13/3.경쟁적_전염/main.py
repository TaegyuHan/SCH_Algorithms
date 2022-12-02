"""

"""
from sys import stdin as input
from collections import deque

EMPTY = 0

MOVE = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        # with open(file_name, encoding="utf-8") as input:
        self._N, self._K = map(int, input.readline().split())
        self._virus = [deque([]) for _ in range(self._K + 1)]
        self._board = []

        for row in range(self._N):
            row_data = list(map(int, input.readline().split()))
            self._board.append(row_data)
            for col in range(self._N):
                if row_data[col] == EMPTY: continue
                self._virus[row_data[col]].append((row_data[col], row, col))
        self._time, self._check_row, self._check_col = map(int, input.readline().split())

    def _show_board(self, board):
        for row in board:
            print(*row)

    def _bfs(self):
        tmp_virus = [deque([]) for _ in range(self._K + 1)]
        for virus_number, q in enumerate(self._virus):
            if not q: continue
            while q:
                number, crow, ccol = q.popleft()
                self._board[crow][ccol] = number
                for trow, tcol in MOVE:
                    nrow, ncol = crow + trow, ccol + tcol
                    if not (0 <= nrow < self._N and 0 <= ncol < self._N): continue
                    if self._board[nrow][ncol]: continue
                    self._board[nrow][ncol] = number
                    tmp_virus[number].append((number, nrow, ncol))
        self._virus = tmp_virus

    def _logic(self):
        """ 풀이 """
        for _ in range(self._time):
            self._bfs()
        # self._show_board(self._board)
        return self._board[self._check_row - 1][self._check_col - 1]

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/2.txt")
    p.answer()
"""
    인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다.
    다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서
    연구소에 벽을 세우려고 한다.

    연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며,
    직사각형은 1×1 크기의 정사각형으로 나누어져 있다.
    연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

    일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로
    인접한 빈 칸으로 모두 퍼져나갈 수 있다.
     새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
"""
from sys import stdin as input
from copy import deepcopy
from itertools import combinations
from collections import deque

MOVE = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

WALL = 1
EMPTY = 0
VIRUS = 2


class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        # with open(file_name, encoding="utf-8") as input:
        self._N, self._M = map(int, input.readline().split())

        self._emptys = []
        self._empty_count = -3
        self._board = []
        self._virus = []
        self._start_virus_count = 0
        for row in range(self._N):
            row_data = list(map(int, input.readline().split()))
            self._board.append(row_data)
            for col in range(len(row_data)):

                if row_data[col] == EMPTY:
                    self._emptys.append((row, col))
                    self._empty_count += 1

                if row_data[col] == VIRUS:
                    self._virus.append((row, col))
                    self._start_virus_count += 1

        self._virus_count = self._N * self._M

    def _show_board(self, board):
        for row in board:
            print(*row, sep="\t")

    def _spread_virus(self, select_wall):
        """ 바이러스 퍼지기 """
        virus_count = -self._start_virus_count
        visited = [[0] * self._M for _ in range(self._N)]
        board = deepcopy(self._board)

        for row, col in select_wall:
            board[row][col] = WALL

        q = deque(self._virus)
        while q:
            crow, ccol = q.popleft()
            if visited[crow][ccol]: continue
            if self._virus_count <= virus_count:
                return self._virus_count
            visited[crow][ccol] = 1
            virus_count += 1
            board[crow][ccol] = VIRUS

            for trow, tcol in MOVE:
                nrow, ncol = crow + trow, ccol + tcol

                if not (0 <= nrow < self._N and 0 <= ncol < self._M): continue
                if visited[nrow][ncol]: continue
                if board[nrow][ncol] == WALL: continue
                q.append((nrow, ncol))

        return virus_count

    def _logic(self):
        """ 풀이 """
        for select_wall in combinations(self._emptys, 3):
            self._virus_count = min(self._virus_count, self._spread_virus(select_wall))
        return self._empty_count - self._virus_count

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/3.txt")
    p.answer()
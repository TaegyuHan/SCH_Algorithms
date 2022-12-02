"""

"""
from sys import stdin as input
from collections import deque

MOVE = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
)

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            self._N, self._min, self._max = map(int, input.readline().split())
            self._board = [list(map(int, input.readline().split())) for _ in range(self._N)]

    def _bfs(self, row, col):
        """ 우선 넓이 탐색 """
        count = 0
        tmp_sum = 0
        change_position = set()
        q = deque([(row, col)])
        while q:
            crow, ccol = q.popleft()
            if self._visited[crow][ccol]: continue
            self._visited[crow][ccol] = True
            change_position.add((crow, ccol))
            tmp_sum += self._board[crow][ccol]

            for trow, tcol in MOVE:
                nrow, ncol = trow + crow, tcol + ccol
                if not (0 <= nrow < self._N and 0 <= ncol < self._N): continue
                if self._visited[nrow][ncol]: continue
                if not (self._min <= abs(self._board[crow][ccol] - self._board[nrow][ncol]) <= self._max): continue
                count += 1
                q.append((nrow, ncol))

        # 값 변경하기
        tmp_sum = int(tmp_sum / len(change_position))
        for row, col in change_position:
            self._board[row][col] = tmp_sum

        return count

    def _check(self):
        self._visited = [[False for _ in range(self._N)] for _ in range(self._N)]
        check = 0
        for row in range(self._N):
            for col in range(self._N):
                if self._visited[row][col]: continue
                check += self._bfs(row, col)
        return check

    def _logic(self):
        """ 풀이 """
        count = 0
        while self._check():
            count += 1
        return count

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/3.txt")
    p.answer()
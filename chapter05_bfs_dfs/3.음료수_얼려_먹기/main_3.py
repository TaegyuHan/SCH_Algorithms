"""
    음료수 얼려 먹기
"""
from sys import stdin as input
from collections import deque

WALL = "1"
EMPTY = "0"
MOVE = [
    (-1, 0),  # 위
    (0, 1),  # 오른쪽
    (1, 0),  # 아래
    (0, -1),  # 왼쪽
]

input = open('./test/original.txt')
ROW, COL = map(int, input.readline().split())
BOREAD = [list(input.readline().strip()) for _ in range(ROW)]


class D:
    visited = [[False] * COL for _ in range(ROW)]


def bfs(row: int, col: int) -> int:
    q = deque([(row, col)])

    while q:
        crow, ccol = q.popleft()
        if D.visited[crow][ccol]:
            continue
        D.visited[crow][ccol] = True

        for trow, tcol in MOVE:
            nrow, ncol = trow + crow, tcol + ccol
            if not (0 <= nrow < ROW and 0 <= ncol < COL):
                continue
            if BOREAD[nrow][ncol] == WALL:
                continue
            if D.visited[nrow][ncol]:
                continue
            q.append((nrow, ncol))
    return 1


def main() -> None:
    """ 실행 """
    answer = 0

    for row in range(ROW):
        for col in range(COL):
            if BOREAD[row][col] == WALL:
                continue
            if D.visited[row][col]:
                continue
            answer += bfs(row, col)

    print(answer)


if __name__ == '__main__':
    main()

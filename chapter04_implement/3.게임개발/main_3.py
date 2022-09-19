"""
    알고리즘 >
        1. 현재 위치
            1.1 자신의 방향확인
                1.1.1 방향의 앞칸 배열에 포함하는지 확인
                    > 1.2 방향 변경
                1.1.2 벽이있는지 확인
                    > 1.2 방향 변경
                1.1.3 방문했느지 확인
                    > 1.2 방향 변경
                > 1.3 그 방향으로 이동

            1.2 방향 변경 (반시계 방향으로 90도 회전한 방향)
                > 현재 자신의 위치에서 반시계 방향으로 90도
                > 1.1 이동

            1.3 방향 으로 이동
                > 자신의 방향으로 이동
"""
from sys import stdin as input

input = open('./test/original.txt')

SEA = 0
GROUND = 1
TURN = 4
MOVE = [
    (-1, 0),  # 북
    (0, 1),  # 동
    (1, 0),  # 남
    (0, -1),  # 서
]

BACK = [
    (1, 0),  # 남
    (0, -1),  # 서
    (-1, 0),  # 북
    (0, 1),  # 동
]

CHANGE_DIRECTIONS = {
    0: 3,  # 북 > 서
    3: 2,  # 서 > 남
    2: 1,  # 남 > 동
    1: 0,  # 동 > 북
}


def main() -> None:
    """ 실행 함수 """
    ROW, COL = map(int, input.readline().split())
    crow, ccol, cdirection = map(int, input.readline().split())
    board = [list(map(int, input.readline().split())) for _ in range(ROW)]
    visited = [[False] * COL for _ in range(ROW)]

    count = 1
    while True:

        can_go = False
        visited[crow][ccol] = True
        for _ in range(TURN):
            cdirection = CHANGE_DIRECTIONS[cdirection]
            trow, tcol = MOVE[cdirection]
            nrow, ncol = trow + crow, tcol + ccol
            if not (0 <= nrow < ROW and 0 <= ncol < COL):
                continue
            if board[nrow][ncol]:
                continue
            if visited[nrow][ncol]:
                continue
            count += 1
            can_go = True
            crow, ccol = nrow, ncol
            break

        if not can_go:  # 갈 수 없으면
            trow, tcol = BACK[cdirection]
            nrow, ncol = trow + crow, tcol + ccol
            if board[nrow][ncol]:
                break
            crow, ccol = nrow, ncol

    print(count)


if __name__ == '__main__':
    main()

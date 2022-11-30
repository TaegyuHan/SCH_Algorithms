"""

"""
from sys import stdin as input
from collections import deque

EMPTY = 0
APPLE = 1
SNAKE = 2

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
MOVE = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]


class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        # with open(file_name, encoding="utf-8") as input:
        self._N = int(input.readline())
        self._apple_count = int(input.readline())
        self._board = [[EMPTY] * (self._N + 1) for _ in range(self._N + 1)]
        # 사과 받기
        for _ in range(self._apple_count):
            row, col = map(int, input.readline().split())
            self._board[row][col] = APPLE

        # 뱀 회전 받기
        self._turn_infos = []
        self._turn_count = int(input.readline())
        for _ in range(self._turn_count):
            time, turn = input.readline().split()
            self._turn_infos.append((int(time), turn))

        # 데이터 받기 완료

    def _show_board(self, board):
        for row in board:
            print(*row, sep="\t")
        print()

    def _turn(self, direction_num, direction_type):
        if direction_type == "L":
            direction_num = (direction_num - 1) % 4
        elif direction_type == "D":
            direction_num = (direction_num + 1) % 4
        return direction_num

    def _logic(self):
        """ 풀이 """
        head_x, head_y = 1, 1
        self._board[head_x][head_y] = SNAKE
        direction, turn_index, time = 0, 0, 0
        q = deque([(head_x, head_y)])

        while True:
            trow, tcol = MOVE[direction]
            nrow, ncol = head_x + trow, head_y + tcol
            time += 1
            # 판에서 나감
            if not (1 <= nrow <= self._N and 1 <= ncol <= self._N):
                break

            # 자신을 만난경우
            if self._board[nrow][ncol] == SNAKE:
                break

            # 사과가 있는 경우
            if self._board[nrow][ncol] == EMPTY:
                self._board[nrow][ncol] = SNAKE # 다음칸으로 이동
                q.append((nrow, ncol))
                prow, pcol = q.popleft()
                self._board[prow][pcol] = EMPTY # 기존의 칸 지우기

            # 사과가 없는 경우
            if self._board[nrow][ncol] == APPLE:
                self._board[nrow][ncol] = SNAKE
                q.append((nrow, ncol))

            head_x, head_y = nrow, ncol

            # 돌아야 하는 경우
            if turn_index < self._turn_count \
                and time == self._turn_infos[turn_index][0]:  # 시간이 같으면
                direction = self._turn(direction, self._turn_infos[turn_index][1])
                turn_index += 1

        # self._show_board(self._board)
        return time

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/3.txt")
    p.answer()

"""

    N×N 크기의 공간에
    물고기 M마리와
    아기 상어 1마리가 있다.

    공간은 1×1 크기의 정사각형 칸으로 나누어져 있다.
    한 칸에는 물고기가 최대 1마리 존재한다.

    아기 상어와 물고기는 모두 크기를 가지고 있고,
    이 크기는 자연수이다.

    가장 처음에 아기 상어의 크기는 2이고,
    아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

    아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고,
    나머지 칸은 모두 지나갈 수 있다.

    아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
    따라서, 크기가 같은 물고기는 먹을 수 없지만,
    그 물고기가 있는 칸은 지나갈 수 있다.

    아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

    더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
    먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
    거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

    아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

    공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

"""
from sys import stdin as input
from collections import deque

BABY_SHARK = 9

MOVE = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1)
]

class P:

    def __init__(self, file_name: str = "1.txt"):
        """ 생성자 """
        with open(file_name, encoding="utf-8") as input:
            self._N = int(input.readline())
            self._sea = []
            self._answer = 0

            for row in range(self._N):
                tmp = list(map(int, input.readline().split()))
                self._sea.append(tmp)
                for col in range(self._N):
                    if self._sea[row][col] == BABY_SHARK:
                        self._shark_info = [row, col, 1, 0]

    def _show_board(self, board):
        for row in board:
            print(*row)

    def _shark_move(self):
        """ 상어 이동 """
        row, col, size, eat_count = self._shark_info
        visited = [[True] * self._N for _ in range(self._N)]
        fishs = []
        q = deque([(row, col, 0)])
        while q:
            crow, ccol, move = q.popleft()
            if not visited[crow][ccol]: # 이미 방문함
                continue
            visited[crow][ccol] = False
            if self._sea[crow][ccol] != 0 and self._sea[crow][ccol] <= size:  # 물고기 존재
                fishs.append((move, crow, ccol))

            for trow, tcol in MOVE:
                nrow, ncol = trow + crow, tcol + ccol
                if not (0 <= nrow < self._N and 0 <= ncol < self._N):
                    continue  # 바다 안에 존재
                if not visited[nrow][ncol]:
                    continue  # 이미 방문함
                if size < self._sea[nrow][ncol]:
                    continue
                q.append((nrow, ncol, move + 1))

        fishs.sort(reverse=True)
        print(fishs)
        self._show_board(self._sea)
        if fishs:
            move, nrow, ncol = fishs.pop()
            eat_count += 1

            # 물고기 이동
            self._sea[row][col] = 0
            self._sea[nrow][ncol] = 9

            # 이동 시간
            self._answer += move

            if size == eat_count:
                self._shark_info = (nrow, ncol, size + 1, 0)
            else:
                self._shark_info = (nrow, ncol, size, eat_count)
            return True
        return False

    def _logic(self):
        """ 풀이 """
        while self._shark_move():
            continue
        return self._answer

    def answer(self) -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/3.txt")
    p.answer()

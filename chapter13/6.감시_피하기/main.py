"""

"""
from sys import stdin as input
from itertools import combinations

MOVE = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        # with open(file_name, encoding="utf-8") as input:
        self._N = int(input.readline())
        self._students = set()
        self._teacher = []
        self._emptys = []
        self._board = []
        for row in range(self._N):
            tmp = input.readline().split()
            self._board.append(tmp)
            for col in range(self._N):
                if tmp[col] == "S":
                    self._students.add((row, col))
                elif tmp[col] == "T":
                    self._teacher.append((row, col))
                elif tmp[col] == "X":
                    self._emptys.append((row, col))

    def _check(self, obstacle):
        for crow, ccol in self._teacher:
            for trow, tcol in MOVE:
                tmp = 1
                while True:
                    nrow, ncol = crow + (trow * tmp), ccol + (tcol * tmp)
                    if not (0 <= nrow < self._N and 0 <= ncol < self._N): break
                    if (nrow, ncol) in obstacle: break
                    if self._board[nrow][ncol] == "S":
                        return False
                    tmp += 1
        return True

    def _logic(self):
        """ 풀이 """
        for obstacle in combinations(self._emptys, 3):
            if self._check(set(obstacle)):
                return "YES"
        return "NO"

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/2.txt")
    p.answer()
"""

"""
from sys import stdin as input
import heapq

MOVE = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            self._N, self._M = map(int, input.readline().split())
            self._board = [list(map(int, input.readline().split())) for _ in range(self._N)]

    def _logic(self):
        """ 풀이 """

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
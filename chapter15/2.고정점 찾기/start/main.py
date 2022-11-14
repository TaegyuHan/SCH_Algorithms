"""
    고정점(Fixed Point)이란,
    수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미합니다.

    예를 들어 수열 a = {-15, -4, 2, 8, 13}이 있을 때 a[2] = 2이므로,
    고정점은 2가 됩니다.

    하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며,
    모든 원소가 오름차순으로 정렬되어 있습니다. 이때 이 수열에서

    고정점이 있다면, 고정점을 출력하는 프로그램을 작성하세요.
    고정점은 최대 1개만 존재합니다. 만약 고정점이 없다면
    -1을 출력합니다.

    단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지
    않으면 '시간 초과'판정을 받습니다.
"""
from sys import stdin as input
from bisect import bisect_left

class P:

    def __init__(self, file_name: str = "1.txt"):
        """ 생성자 """
        with open(file_name, encoding="utf-8") as input:
            self._number = int(input.readline())
            self._numbers = list(map(int, input.readline().split()))

    def _logic(self):
        """ 풀이 """
        for num in self._numbers:
            if bisect_left(self._numbers, num) == num:
                return num
        return -1

    def answer(self) -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()

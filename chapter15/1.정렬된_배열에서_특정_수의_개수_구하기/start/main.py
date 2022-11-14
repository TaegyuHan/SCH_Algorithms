"""
    N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다.
    이때 이 수열에서 x가 등장하는 횟수를 계산하세요.

    단, 이 문제의 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면
    '시간 초과' 판정을 받습니다.
"""
from sys import stdin as input
from bisect import bisect_left, bisect_right

class P:

    def __init__(self, file_name: str = "1.txt"):
        """ 생성자 """
        with open(file_name, encoding="utf-8") as input:
            self._count, self._find_number = map(int, input.readline().split())
            self._numbers = list(map(int, input.readline().split()))

    def _logic(self):
        """ 풀이 """
        answer = bisect_right(self._numbers, self._find_number) - bisect_left(self._numbers, self._find_number)
        if answer == 0:
            return -1
        return answer

    def answer(self) -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()

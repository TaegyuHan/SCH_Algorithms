"""
    첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다.

    - N은 2이상 100,000이하인 정수
    - M은 1이상 1,000,000이하인 정수
    - 유지비가 C (1 ≤ C ≤ 1,000)
"""
from sys import stdin as input
import heapq

class P:

    _ball_count: int
    _max_weight: int
    _balls: list[int]
    _answer: int

    @classmethod
    def _input_data(cls, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            cls._ball_count, cls._max_weight = map(int, input.readline().split())
            cls._balls = list(map(int, input.readline().split()))

    @classmethod
    def _logic(cls):
        """ 풀이 """
        cls._answer = 0
        for idx, ball_1 in enumerate(cls._balls):
            for jdx, ball_2 in enumerate(cls._balls[idx + 1:]):
                if ball_1 == ball_2: continue
                cls._answer += 1
        return cls._answer

    @classmethod
    def answer(cls, file_name: str = "1.txt") -> None:
        cls._input_data(file_name)
        print(cls._logic())

    @classmethod
    def answer_test(cls, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        cls._input_data(file_name)
        return cls._logic()


if __name__ == '__main__':
    P.answer(file_name="./data/input/1.txt")

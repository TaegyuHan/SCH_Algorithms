"""
    동네 편의점의 주인인 동빈이는 N개의 동전을 갖고 있다.

    이 때 N개의 동전을 이용해 만들 수 없는 양의 정수 금액

    중 최솟값을 구하는 프로그램을 작성해라.
"""
from sys import stdin as input
import heapq


class P:

    @classmethod
    def _input_data(cls, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            cls._coin_count = int(input.readline())
            cls._coins = sorted(map(int, input.readline().split()))

    @classmethod
    def _logic(cls):
        """ 풀이 """
        cls._coins.sort()
        target = 1
        for coin in cls._coins:
            if coin > target:
                break
            target += coin
        return target

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

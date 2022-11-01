"""
    문제 정의

    한 마을에 모험가가 N명 있다.

    모험가 길드에서는 N명의 모험가를 대상으로 공포도를 측정했는데,
    공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로
    대처할 능력이 떨어진다.

    모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자
    공포도가 X인 모험가는
    반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을
    떠날 수 있도록 규정했다.

    동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는 지 궁금하다.
    N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는
    그룹 수의 최댓값을 구하는 프로그램을 작성하시오.

"""
from sys import stdin as input
import heapq


class P:
    _adventurer_count: int
    _adventurers: list[int]
    _answer: int

    @classmethod
    def _input_data(cls, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            cls._adventurer_count = int(input.readline())
            cls._adventurers = list(map(int, input.readline().split()))

    @classmethod
    def _logic(cls):
        """ 풀이 """
        cls._answer = 0
        cls._adventurers.sort()
        while cls._adventurers:
            group_count = cls._adventurers.pop()
            cls._answer += 1

            if not cls._adventurers:
                break

            for _ in range(group_count):
                cls._adventurers.pop()

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

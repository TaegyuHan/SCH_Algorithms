"""
    첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다.

    A, B 두 사람이 볼링을 치고 있다.
    두 사람은 서로 무게가 다른 볼링공을 고르려고 한다.
    볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고,
    공의 번호는 1번부터 순서대로 부여된다. 또한 같은 무게의 공이 여러개 있을 수 있지만,
    서로 다른 것으로 간주한다. 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재한다.

    예를 들어, N이 5이고, M이 3이며, 각각의 무게가 차례대로
    [1, 3, 2, 3, 2] 일때 각 공의 번호가 차례대로 1번부터 5번까지 부여한다.

    이 때 두 사람이 서로 다른 공을 고를 수 있는 경우의 수는 총 8가지이다.
    N개의 공의 무게가 각각 주어질때, 두 사람이 볼링공을 고르는 경우의 수를 구해라.

    - N은 2이상 100,000이하인 정수
    - M은 1이상 1,000,000이하인 정수
    - 유지비가 C (1 ≤ C ≤ 1,000)
"""
from sys import stdin as input
import heapq

class P:

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

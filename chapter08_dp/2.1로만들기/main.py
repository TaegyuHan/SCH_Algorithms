"""
    정수 X가 주어질때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
        1) X가 5로 나누어떨어지면, 5로 나눈다.
        2) X가 3으로 나누어 떨어지면, 3으로 나눈다.
        3) X가 2로 나누어 떨어지면, 2로 나눈다.
        4) X에서 1을 뺀다.

    정수 X가 주어졌을때, 연산 4개를 적절히 사용해서 1을 만들려고 한다.
    연산을 사용하는 횟수의 최솟값을 출력하시오.
    예를 들어, 정수가 26이면 다음과 같이 계산해서 3번의 연산이 최솟값이다.
        26 - 1 = 25
        25 / 5 = 5
        5 / 5 = 1

    입력 조건
        첫째 줄에 정수 X이 주어진다. (1<=X<=30,000)

    출력 조건
        첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
"""
from sys import stdin as input


class P:
    MAX = 30_001
    DP = [0 for _ in range(MAX)]  # O(N)
    X: int

    def __init__(self) -> None:
        """ 생성자 """
        self._init_dp()
        self._input_data()

    @classmethod
    def _input_data(cls) -> None:  # O(1)
        """ 데이터 받기 """
        # input = open('./test/original.txt', encoding="utf-8")
        cls.X = int(input.readline())

    @classmethod
    def _init_dp(cls) -> None:  # O(N)
        """ DP 값 초기화 """
        for idx in range(2, cls.MAX):
            cls.DP[idx] = cls.DP[idx - 1] + 1
            if idx % 5 == 0:
                cls.DP[idx] = min(cls.DP[idx], cls.DP[idx // 5] + 1)
            if idx % 3 == 0:
                cls.DP[idx] = min(cls.DP[idx], cls.DP[idx // 3] + 1)
            if idx % 2 == 0:
                cls.DP[idx] = min(cls.DP[idx], cls.DP[idx // 2] + 1)

    @classmethod
    def answer(cls) -> None:  # O(1)
        """ 정답 """
        print(cls.DP[cls.X])

    @classmethod
    def run(cls) -> None:
        """ 실행 """
        cls.answer()


if __name__ == '__main__':
    P().run()

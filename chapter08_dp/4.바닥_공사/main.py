"""
    문제
        가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다.
        태일이는 이 얇은 바닥을 1 X 2의 덮개, 2 X 1의 덮개, 2 X 2의 덮개를 이용해 채우고자 한다.
        이 때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오.
        예를 들어, 2X3 크기의 바닥을 채우는 경우의 수는 5가지이다.

    입력 조건
        첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1,000)

    출력 조건
        첫째 줄에 2 X N 크기의 바닥을 채우는 방법의 수를 796,796으로 나눈 나머지를 출력한다.
"""
from sys import stdin as input


class P:
    """ 문제 """
    _N: int
    _DP: list[int]

    def __init__(self) -> None:
        """ 생성자 """
        self._input_data()
        self._init_dp()

    @classmethod
    def _input_data(cls) -> None:
        """ 데이터 받기 """
        input = open('./test/original.txt')
        cls._N = int(input.readline())

    @classmethod
    def _init_dp(cls) -> None:
        """ DP초기화 """
        cls._DP = [0, 1, 3]
        cls._DP.extend([0 for _ in range(1_000)])

        for i in range(3, cls._N + 1):
            cls._DP[i] = (cls._DP[i - 1] + (2 * cls._DP[i - 2])) % 796796

    @classmethod
    def answer(cls):
        print(cls._DP[cls._N])


if __name__ == '__main__':
    p = P()
    p.answer()

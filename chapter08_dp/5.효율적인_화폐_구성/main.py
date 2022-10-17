"""
    - N가지 종류의 화폐가 있다.
    - 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
    - 이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
    - 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.

    입력 조건
        첫째 줄에 N,M이 주어진다 ( 1 <= N <= 100, 1 <= M <= 10,000 )
        이후의 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수이다.
"""
from sys import stdin as input


class P:
    """ 문제 """
    _N: int
    _M: int
    _coins: list[int]
    _DP: list[int]

    def __init__(self) -> None:
        """ 생성자 """
        self._input_data()
        self._init_dp()

    @classmethod
    def _init_dp(cls) -> None:
        """ DP 생성 """
        cls._DP = [10_001] * (cls._M + 1)
        cls._DP[0] = 0

        for coin in cls._coins:  # 100
            for ccoin in range(coin, cls._M + 1):  # 10_001
                if cls._DP[ccoin - coin] == 10_001:
                    continue  # 계산 불가 PASS
                cls._DP[ccoin] = min(cls._DP[ccoin], cls._DP[ccoin - coin] + 1)

    @classmethod
    def _input_data(cls) -> None:
        """ 데이터 받기 """
        input = open('./test/original.txt')
        cls._N, cls._M = map(int, input.readline().split())
        cls._coins = [int(input.readline()) for _ in range(cls._N)]

    @classmethod
    def answer(cls) -> None:
        """ 정답 """
        if cls._DP[cls._M] == 10_001:
            print(-1)
        else:
            print(cls._DP[cls._M])


if __name__ == '__main__':
    p = P()
    p.answer()
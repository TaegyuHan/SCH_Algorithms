"""

"""
from sys import stdin as input
import heapq

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            self._n = int(input.readline())

            self._dp = []  # 다이나믹 프로그래밍을 위한 DP 테이블 초기화
            for _ in range(self._n):
                self._dp.append(list(map(int, input.readline().split())))

    def _logic(self):
        """ 풀이 """

        # 다이나믹 프로그래밍으로 2번째 줄부터 내려가면서 확인
        for i in range(1, self._n):
            for j in range(i + 1):
                # 왼쪽 위에서 내려오는 경우
                if j == 0:
                    up_left = 0
                else:
                    up_left = self._dp[i - 1][j - 1]
                # 바로 위에서 내려오는 경우
                if j == i:
                    up = 0
                else:
                    up = self._dp[i - 1][j]
                # 최대 합을 저장
                self._dp[i][j] = self._dp[i][j] + max(up_left, up)

        return max(self._dp[self._n - 1])

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
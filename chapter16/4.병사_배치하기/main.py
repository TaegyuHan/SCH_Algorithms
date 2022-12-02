"""

"""
from sys import stdin as input

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            self._n = int(input.readline())
            self._array = list(map(int, input.readline().split()))
            # 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
            self._array.reverse()

            # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
            self._dp = [1] * self._n

    def _logic(self):
        """ 풀이 """
        # 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
        for i in range(1, self._n):
            for j in range(0, i):
                if self._array[j] < self._array[i]:
                    self._dp[i] = max(self._dp[i], self._dp[j] + 1)

        # 열외해야 하는 병사의 최소 수를 출력
        return self._n - max(self._dp)

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
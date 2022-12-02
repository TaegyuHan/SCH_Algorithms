"""

"""
from sys import stdin as input

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            self._test_case = int(input.readline())
            self._n, self._m = map(int, input.readline().split())
            self._array = list(map(int, input.readline().split()))

    def _logic(self):
        """ 풀이 """
        # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
        dp = []
        index = 0
        for i in range(self._n):
            dp.append(self._array[index:index + self._m])
            index += self._m

        # 다이나믹 프로그래밍 진행
        for j in range(1, self._m):
            for i in range(self._n):
                # 왼쪽 위에서 오는 경우
                if i == 0:
                    left_up = 0
                else:
                    left_up = dp[i - 1][j - 1]
                # 왼쪽 아래에서 오는 경우
                if i == self._n - 1:
                    left_down = 0
                else:
                    left_down = dp[i + 1][j - 1]
                # 왼쪽에서 오는 경우
                left = dp[i][j - 1]
                dp[i][j] = dp[i][j] + max(left_up, left_down, left)

        result = 0
        for i in range(self._n):
            result = max(result, dp[i][self._m - 1])

        return result

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
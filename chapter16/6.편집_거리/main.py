"""

"""
from sys import stdin as input

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            self._str1 = input.readline()
            self._str2 = input.readline()

    def _logic(self):
        """ 풀이 """
        n = len(self._str1)
        m = len(self._str2)

        # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # DP 테이블 초기 설정
        for i in range(1, n + 1):
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[0][j] = j

        # 최소 편집 거리 계산
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
                if self._str1[i - 1] == self._str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # 문자가 다르다면, 세 가지 경우 중에서 최솟값 찾기
                else:  # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서 최소 비용을 찾아 대입
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[n][m]

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
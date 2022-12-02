"""

"""
from sys import stdin as input

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            self._n = int(input.readline())  # 전체 상담 개수
            self._t = []  # 각 상담을 완료하는데 걸리는 기간
            self._p = []  # 각 상담을 완료했을 때 받을 수 있는 금액
            self._dp = [0] * (self._n + 1)  # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화

            for _ in range(self._n):
                self._x, self._y = map(int, input.readline().split())
                self._t.append(self._x)
                self._p.append(self._y)

    def _logic(self):
        """ 풀이 """
        max_value = 0
        # 리스트를 뒤에서부터 거꾸로 확인
        for i in range(self._n - 1, -1, -1):
            time = self._t[i] + i
            # 상담이 기간 안에 끝나는 경우
            if time <= self._n:
                # 점화식에 맞게, 현재까지의 최고 이익 계산
                self._dp[i] = max(self._p[i] + self._dp[time], max_value)
                max_value = self._dp[i]
            # 상담이 기간을 벗어나는 경우
            else:
                self._dp[i] = max_value

        return max_value

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
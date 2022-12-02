"""

"""
from sys import stdin as input


class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        # with open(file_name, encoding="utf-8") as input:
        self._N = int(input.readline())  # 2 <= N <= 11
        self._numbers = list(map(int, input.readline().split()))  # 1 <= A <= 100
        self._oper_add, self._oper_sub, self._oper_mul, self._oper_div \
            = map(int, input.readline().split())

        self._max_value = -float("inf")
        self._min_value = float("inf")

    def _dfs(self, data_idx, now):
        """ 우선 깊이 탐색 """
        if data_idx == self._N:
            self._max_value = max(self._max_value, now)
            self._min_value = min(self._min_value, now)
        else:
            if self._oper_add > 0:
                self._oper_add -= 1
                self._dfs(data_idx + 1, now + self._numbers[data_idx])
                self._oper_add += 1

            if self._oper_sub > 0:
                self._oper_sub -= 1
                self._dfs(data_idx + 1, now - self._numbers[data_idx])
                self._oper_sub += 1

            if self._oper_mul > 0:
                self._oper_mul -= 1
                self._dfs(data_idx + 1, now * self._numbers[data_idx])
                self._oper_mul += 1

            if self._oper_div > 0:
                self._oper_div -= 1
                self._dfs(data_idx + 1, int(now / self._numbers[data_idx]))
                self._oper_div += 1

    def _logic(self):
        """ 풀이 """
        self._dfs(1, self._numbers[0])
        print(self._max_value)
        print(self._min_value)

    def answer(self, file_name: str = "1.txt") -> None:
        self._logic()

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/3.txt")
    p.answer()
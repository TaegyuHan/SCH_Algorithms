"""
"""
from sys import stdin as input

class P:

    def __init__(self, file_name: str = "1.txt"):
        """ 생성자 """
        with open(file_name, encoding="utf-8") as input:
            self._N = int(input.readline())
            self._home_positions = list(map(int, input.readline().split()))

    def _distance(self, idx: int):
        tmp = 0
        for position in self._home_positions:
            tmp += abs(idx - position)
        return tmp

    def _logic(self):
        """ 풀이 """
        self._home_positions.sort()
        midian = self._N // 2

        if self._N == 1:
            answer = self._home_positions[0]
        # 홀수인 경우
        elif self._N % 2 == 1:
            answer = self._home_positions[self._N // 2]
        else:
            left, right = midian - 1, midian
            left_sum = self._distance(self._home_positions[left])
            right_sum = self._distance(self._home_positions[right])

            if left_sum <= right_sum:
                answer = self._home_positions[left]
            else:
                answer = self._home_positions[right]

        return answer

    def answer(self) -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()

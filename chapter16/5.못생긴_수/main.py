"""

"""
from sys import stdin as input

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            self._n = int(input.readline())

    def _logic(self):
        """ 풀이 """
        ugly = [0] * self._n  # 못생긴 수를 담기 위한 테이블 (1차원 DP 테이블)
        ugly[0] = 1  # 첫 번째 못생긴 수는 1

        # 2배, 3배, 5배를 위한 인덱스
        i2 = i3 = i5 = 0
        # 처음에 곱셈 값을 초기화
        next2, next3, next5 = 2, 3, 5

        # 1부터 n까지의 못생긴 수들을 찾기
        for l in range(1, self._n):
            # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
            ugly[l] = min(next2, next3, next5)
            # 인덱스에 따라서 곱셈 결과를 증가
            if ugly[l] == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if ugly[l] == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if ugly[l] == next5:
                i5 += 1
                next5 = ugly[i5] * 5

        # n번째 못생긴 수를 출력
        return ugly[self._n - 1]

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
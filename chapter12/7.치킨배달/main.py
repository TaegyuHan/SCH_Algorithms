"""
    크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다.

    도시의 각 칸은
    - 빈 칸,
    - 치킨집,
    집 중 하나이다.

    도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸,
    왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.


"""
from sys import stdin as input
from itertools import combinations
import heapq

HOUSE = 1
CHICKEN = 2

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            self._N, self._M = map(int, input.readline().split())

            self._chicken_location = []
            self._house_location = []

            for row in range(self._N):
                tmp = list(map(int, input.readline().split()))
                for col in range(self._N):
                    if tmp[col] == CHICKEN:
                        self._chicken_location.append((row, col))
                    elif tmp[col] == HOUSE:
                        self._house_location.append((row, col))

    def _distance(self, row1, col1, row2, col2):
        return abs(row1 - row2) + abs(col1 - col2)

    def _logic(self):
        """ 풀이 """
        result = float("inf")
        # 치킨집 3개 선택
        for chickens in combinations(self._chicken_location, self._M):
            temp_distance = 0  # 거리 계산

            # 집이 <> 치킨집 가장 짧은 거리
            for house_row, house_col in self._house_location:
                chickens_distance = float("inf")
                for chicken_row, chicken_col in chickens:
                    chickens_distance =  min(
                        chickens_distance,
                        self._distance(house_row, house_col, chicken_row, chicken_col)
                    )
                temp_distance += chickens_distance
            result = min(result, temp_distance)
        return result

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
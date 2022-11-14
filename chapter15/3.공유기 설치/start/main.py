"""
    도현이의 집 N개가 수직선 위에 있다.
    각각의 집의 좌표는 x1, ..., xN이고,
    집 여러개가 같은 좌표를 가지는 일은 없다.

    도현이는 언제 어디서나 와이파이를 즐기기 위해서
    집에 공유기 C개를 설치하려고 한다.

    최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에,
    한 집에는 공유기를 하나만 설치할 수 있고,
    가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

    C개의 공유기를 N개의 집에 적당히 설치해서,
    가장 인접한 두 공유기 사이의 거리를 최대로
    하는 프로그램을 작성하시오.
"""
from sys import stdin as input


class P:

    def __init__(self, file_name: str = "1.txt"):
        """ 생성자 """
        # with open(file_name, encoding="utf-8") as input:
        self._home_count, self._share_count = map(int, input.readline().split())
        self._homes = [int(input.readline()) for _ in range(self._home_count)]
        self._homes.sort()

    def _setup_count(self, length: int):
        """ 공유기 설치 수 """
        no_setup_area = self._homes[0] + length
        count = 1
        for home in self._homes[1:]:
            if no_setup_area < home:
                no_setup_area = home + length
                count += 1
                continue
        return count

    def _binary_search(self):
        """ 이분탐색 """
        min_gap = 1
        max_gap = self._homes[-1] - self._homes[0]
        while min_gap != max_gap:
            mid = (min_gap + max_gap) // 2
            setup_count = self._setup_count(length=mid)
            if setup_count < self._share_count:
                max_gap = mid
            else:
                min_gap = mid + 1
        return max_gap

    def _logic(self):
        """ 풀이 """
        return self._binary_search()

    def answer(self) -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/2.txt")
    p.answer()

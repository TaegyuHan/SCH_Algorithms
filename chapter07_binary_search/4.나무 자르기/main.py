"""
    나무 자르기
"""
from sys import stdin as input


class P:
    tree_count: int
    get_tree_length: int
    trees_length: list[int]

    def __init__(self):
        """ 생성자 """
        self._input_data()

    @classmethod
    def _input_data(cls):
        """ 데이터 받기 """
        # input = open('./test/original.txt', encoding="utf-8")
        cls.tree_count, cls.get_tree_length = map(int, input.readline().split())
        cls.trees_length = list(map(int, input.readline().split()))
        cls.trees_length.sort()

    @classmethod
    def _cut_tree(cls, height: int) -> int:
        """ 나무 자르기 """
        total = 0
        for tree_length in cls.trees_length:
            if tree_length > height:
                total += tree_length - height
        return total

    @classmethod
    def _binary_search(cls):
        """ 이분 탐색 """
        start, end = 0, cls.trees_length[-1]
        while start < end:
            mid = (start + end) // 2
            total = cls._cut_tree(mid)

            # 더 잘라야 하는 경우
            if total >= cls.get_tree_length:
                start = mid + 1
                answer = mid
            # 너무 많이 자른 경우
            else:
                end = mid
        print(answer)

    @classmethod
    def run(cls):
        """ 실행 """
        cls._binary_search()


if __name__ == '__main__':
    P().run()

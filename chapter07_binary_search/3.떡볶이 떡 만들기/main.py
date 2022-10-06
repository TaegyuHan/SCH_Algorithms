"""
    두배열의 원소 교체
"""
from sys import stdin as input


class P:

    def __init__(self):
        self._input_data()
        self._binary_search()

    def _input_data(self):
        """ 데이터 받기 """
        self._input = open('./test/original.txt', encoding="utf-8")
        self._tree_count, self._want_size = map(int, self._input.readline().split())
        self._trees = list(map(int, self._input.readline().split()))
        self._trees.sort()

    def _cut_tree(self, size: int):
        """ 나무 자른 결과 """
        cut = 0
        for tree in self._trees:
            if 0 < (cut_tmp := tree - size):
                cut += cut_tmp
        return cut

    def _binary_search(self):
        start, end = 0, self._trees[-1]

        while start < end:
            mid = (start + end) // 2
            print(self._cut_tree(mid))
            break

    def answer(self):
        """ 정답  """
        


def main():
    """ 함수 실행 """
    p = P()
    p.answer()


if __name__ == '__main__':
    main()

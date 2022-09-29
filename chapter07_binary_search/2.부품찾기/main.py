"""
    두배열의 원소 교체
"""
from sys import stdin as input


class P:

    def __init__(self):
        self._input_data()

    def _input_data(self):
        """ 데이터 받기 """
        self._input = open('./test/original.txt', encoding="utf-8")
        self._items_count = int(self._input.readline())
        self._items = set(map(int, self._input.readline().split()))
        self._find_count = int(self._input.readline())
        self._find_items = list(map(int, self._input.readline().split()))

    def answer(self):
        answer = ""
        for item_number in self._find_items:
            if item_number in self._items:
                answer += "yes "
                continue
            answer += "no "
        print(answer)

def main():
    """ 함수 실행 """
    p = P()
    p.answer()


if __name__ == '__main__':
    main()

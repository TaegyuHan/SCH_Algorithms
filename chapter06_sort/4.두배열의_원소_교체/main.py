"""
    두배열의 원소 교체
"""
from sys import stdin as input


class Data:

    def __init__(self):
        self._input = open('./test/original.txt', encoding="utf-8")
        self._input_data(input=self._input)
        self._lists_sort()
        self._change_numbers()

    def _input_data(self, input):
        """ 데이터 받기 """
        self._list_length, self._change_count = map(int, input.readline().split())
        self._a_list = list(map(int, input.readline().split()))
        self._b_list = list(map(int, input.readline().split()))

    def _lists_sort(self):
        """ 리스트 정렬 """
        self._a_list.sort()
        self._b_list.sort(reverse=True)

    def _swap(self, idx):
        """ 리스트 데이터 교환 """
        self._a_list[idx], self._b_list[idx] = \
            self._b_list[idx], self._a_list[idx]

    def _change_numbers(self):
        idx = 0
        while self._change_count and idx < self._list_length:
            if self._a_list[idx] < self._b_list[idx]:
                self._swap(idx)
                self._change_count -= 1
            idx += 1

    def answer(self):
        print(sum(self._a_list))


def main():
    """ 함수 실행 """
    data = Data()
    data.answer()


if __name__ == '__main__':
    main()

"""

"""
from sys import stdin as input
import heapq

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            self._n = int(input.readline())
            # 힙(Heap)에 초기 카드 묶음을 모두 삽입

            self._heap = []
            for i in range(self._n):
                data = int(input.readline())
                heapq.heappush(self._heap, data)



    def _logic(self):
        """ 풀이 """
        result = 0

        # 힙(Heap)에 원소가 1개 남을 때까지
        while len(self._heap) != 1:
            # 가장 작은 2개의 카드 묶음 꺼내기
            one = heapq.heappop(self._heap)
            two = heapq.heappop(self._heap)
            # 카드 묶음을 합쳐서 다시 삽입
            sum_value = one + two
            result += sum_value
            heapq.heappush(self._heap, sum_value)

        return result

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
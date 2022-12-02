"""

"""
from sys import stdin as input
from bisect import bisect_left, bisect_right

import heapq

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        # 모든 단어들을 길이마다 나누어서 저장하기 위한 리스트
        self._array = [[] for _ in range(10001)]
        # 모든 단어들을 길이마다 나누어서 뒤집어 저장하기 위한 리스트
        self._reversed_array = [[] for _ in range(10001)]

    def _count_by_range(self, a, left_value, right_value):
        right_index = bisect_right(a, right_value)
        left_index = bisect_left(a, left_value)
        return right_index - left_index

    def _logic(self, words, queries):
        """ 풀이 """
        answer = []
        for word in words:  # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
            self._array[len(word)].append(word)  # 단어를 삽입
            self._reversed_array[len(word)].append(word[::-1])  # 단어를 뒤집어서 삽입

        for i in range(10001):  # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
            self._array[i].sort()
            self._reversed_array[i].sort()

        for q in queries:  # 쿼리를 하나씩 확인하며 처리
            if q[0] != '?':  # 접미사에 와일드 카드가 붙은 경우
                res = self._count_by_range(self._array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
            else:  # 접두사에 와일드 카드가 붙은 경우
                res = self._count_by_range(self._reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
            # 검색된 단어의 개수를 저장
            answer.append(res)
        return answer

    def answer(self, file_name: str = "1.txt") -> None:
        words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
        queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
        print(self._logic(words, queries))

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
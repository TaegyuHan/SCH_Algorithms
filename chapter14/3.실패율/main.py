"""

"""
from sys import stdin as input
import heapq

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        # with open(file_name, encoding="utf-8") as input:

    def _logic(self, N, stages):
        """ 풀이 """
        answer = []
        length = len(stages)

        # 스테이지 번호를 1부터 N까지 증가시키며
        for i in range(1, N + 1):
            # 해당 스테이지에 머물러 있는 사람의 수 계산
            count = stages.count(i)

            # 실패율 계산
            if length == 0:
                fail = 0
            else:
                fail = count / length

            # 리스트에 (스테이지 번호, 실패율) 원소 삽입
            answer.append((i, fail))
            length -= count

        # 실패율을 기준으로 각 스테이지를 내림차순 정렬
        answer = sorted(answer, key=lambda t: t[1], reverse=True)

        # 정렬된 스테이지 번호 반환
        answer = [i[0] for i in answer]
        return answer

    def answer(self, file_name: str = "1.txt") -> None:
        N = 5
        stages = [2, 1, 2, 6, 2, 4, 3, 3]
        print(self._logic(N, stages))

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
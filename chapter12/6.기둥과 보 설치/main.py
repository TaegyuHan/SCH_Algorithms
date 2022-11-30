"""

"""
from sys import stdin as input
import heapq

DELETE = 0
CREATE = 1

PILLAR = 0
PLATE = 1


class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        self._N = 5
        self._build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1],
                             [4, 2, 1, 1], [3, 2, 1, 1]]

        # self._build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

    def _show_board(self, board):
        for row in board:
            print(*row, sep="\t")

    def _possible(self, answer):
        """ 가능한 구조물인지 확인 """
        for x, y, struct in answer:
            # 기둥 인 경우
            if struct == PILLAR:
                # 바닥위
                # 보의 왼쪽 끝
                # 보의 오른쪽 끝
                # 기둥위
                if y == 0 \
                        or [x - 1, y, 1] in answer \
                        or [x, y, 1] in answer \
                        or [x, y - 1, 0] in answer:
                    continue

                return False
            # 판 인 경우
            elif struct == PLATE:
                # 왼쪽 끝이 기둥위
                # 오른쪽 끝이 기둥위

                if [x, y - 1, 0] in answer \
                        or [x + 1, y - 1, 0] in answer \
                        or [x - 1, y, 1] in answer \
                        or [x + 1, y, 1] in answer:
                    continue

                return False
        return True

    def _logic(self, n, build_frame):
        """ 풀이 """
        answer = []
        for x, y, struct, delete_or_create in build_frame:  # 설치 작업
            if delete_or_create == DELETE:
                answer.remove([x, y, struct])
                if not self._possible(answer):
                    answer.append([x, y, struct])

            elif delete_or_create == CREATE:
                answer.append([x, y, struct])
                if not self._possible(answer):
                    answer.remove([x, y, struct])

        answer.sort()
        return answer

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic(self._N, self._build_frame))

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic(self._N, self._build_frame)


if __name__ == '__main__':
    p = P(file_name="../../start/data/input/1.txt")
    p.answer()

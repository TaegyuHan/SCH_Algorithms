"""
    선생님은 시험을 본 학생 N명의 성적을 분실하고,
    성적을 비교한 결과의 일부만 가지고 있다.

    학생 N명의 성적은 모두 다른데,
    다음은 6명의 학생에 대해 6번만 성적을 비교한 결과이다.

    1번 성적 < 5번 성적
    3번 성적 < 4번 성적
    4번 성적 < 2번 성적
    4번 성적 < 6번 성적
    5번 성적 < 2번 성적
    5번 성적 < 4번 성적
"""
from sys import stdin as input
import heapq

class P:

    def __init__(self, file_name: str = "1.txt"):
        """ 생성자 """
        with open(file_name, encoding="utf-8") as input:
            input.readline()

    def _logic(self):
        """ 풀이 """

    def answer(self) -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()

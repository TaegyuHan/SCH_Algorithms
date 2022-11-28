"""
    도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어집니다.
    이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하세요.

    국어 점수가 감소하는 순서로
    국어 점수가 같으면 영어 점수가 증가하는 순서로
    국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
    모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
    (단, 아스키코드에서 대문자는 소문자보다 작으므로 사전 순으로 앞에 옵니다.)

    입력
        첫째 줄에 도현이네 반의 학생 수 N ( 1 <= N <= 100,000 )이 주어집니다.
        둘째 줄부터 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백으로 구분해 주어집니다.
        점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수입니다.
        이름을 알파벳 대소문자로 이루어진 문자열이고, 길이는 10자리를 넘지 않습니다.

    출력
        문제에 나와 있는 정렬 기준으로 정렬한 후 첫째 줄부터 N개의 줄에 걸쳐 각 학생의 이름을 출력합니다.

"""
from sys import stdin as input
import heapq

class P:

    def __init__(self, file_name: str = "1.txt"):
        """ 생성자 """
        # with open(file_name, encoding="utf-8") as input:
        self._heapq = []
        self._persons = []
        self._count = int(input.readline())
        for _ in range(self._count):
            name, ko, en, math = input.readline().split()
            heapq.heappush(self._heapq, (-int(ko), int(en), -int(math), name))

    def _logic(self):
        """ 풀이 """
        answer = []
        while self._heapq:
            _, _, _, name = heapq.heappop(self._heapq)
            answer.append(name)
            print(name)
        return answer

    def answer(self) -> None:
        self._logic()

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()

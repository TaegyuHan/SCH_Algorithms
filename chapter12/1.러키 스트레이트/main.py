"""
    문제 설명

    특정조건에서 사용할 수 있는 필살기인 럭키 스트레이트 기술이 있습니다.
    그 특정 조건은 현재 캐릭터의 점수를 N이라고
    할 때 자릿수를 기준으로 점수 N을 반으로 나누어
    왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각
    자릿수의 합을 더한 값이 동일한 상황을 의미합니다.

    N의 자릿수는 짝수로 주어집니다.
    예를 들어 점수가 123402라면 왼쪽 부분의 각 자릿수 합은 1+2+3, 오른쪽 부분의 각 자릿수 합은 4+0+2이므로 두 합이 6으로 동일해 럭키 스트레이트를 사용할 수 있습니다.

    123 <> 402

    Input
    첫째줄에 점수 N이 정수로 주어진다.(10 <= N <= 99,999,999(9천만) ). 단, 점수 N의 자릿수는 항상 짝수 형태로만 주어진다.

    Output
    첫째 줄에 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"를 출력한다.

    Limit
    10 <= N <= 99999999
    time : 1 second
    memory : 256 MB
"""
from sys import stdin as input
import heapq

class P:

    _number: str

    @classmethod
    def _input_data(cls, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            cls._number = input.readline().strip()

    @classmethod
    def _logic(cls):
        """ 풀이 """
        div_idx = (len(cls._number)//2)
        left_point = sum(map(int, cls._number[:div_idx]))
        right_point = sum(map(int, cls._number[div_idx:]))
        if left_point == right_point:
            return "LUCKY"
        return "READY"

    @classmethod
    def answer(cls, file_name: str = "1.txt") -> None:
        cls._input_data(file_name)
        print(cls._logic())

    @classmethod
    def answer_test(cls, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        cls._input_data(file_name)
        return cls._logic()


if __name__ == '__main__':
    P.answer(file_name="./data/input/2.txt")

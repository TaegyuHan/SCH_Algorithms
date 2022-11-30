"""
    문제

    각 자리가 숫자 (0부터 9)로만 이루어진 문자열 S가 주어졌을 때,
    왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
    'X' 혹은 '+'연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를
     구하는 프로그램을 작성하세요.

    단, +보다 X를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은
    왼쪽에서부터 순서대로 이루어진다고 가정합니다.
"""
from sys import stdin as input


class P:

    @classmethod
    def _input_data(cls, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            cls._numbers = list(map(int, input.readline().strip()))

    @classmethod
    def _logic(cls):
        """ 풀이 """
        answer = 0
        for num in cls._numbers:
            answer = max(answer + num, answer * num)
        return answer

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
    P.answer(file_name="./data/input/1.txt")

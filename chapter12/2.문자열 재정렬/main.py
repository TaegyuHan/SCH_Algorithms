"""
    문제 정의

    알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
    이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출련한 뒤에,
    그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

    예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
"""
from sys import stdin as input
import heapq


class P:

    _S: str

    @classmethod
    def _input_data(cls, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            cls._S = list(input.readline().strip())

    @classmethod
    def _logic(cls):
        """ 풀이 """
        cls._S.sort()
        int_idx = 0
        for idx, data in enumerate(cls._S):
            if not data.isnumeric():
                int_idx = idx
                break

        return f"{''.join(cls._S[int_idx:])}{str(sum(map(int, cls._S[:int_idx])))}"

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

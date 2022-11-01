"""
    다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있습니다.
    다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 합니다.

    다솜이 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고
    모두 뒤집는 것입니다.

    예를 들어 S = 0001100일 때는 다음과 같습니다.
"""
from sys import stdin as input

ONE = "1"
ZERO = "0"


class P:
    _numbers: list[str]
    _answer: int
    _0_count: int
    _1_count: int

    @classmethod
    def _input_data(cls, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            cls._numbers = list(input.readline().strip())

    @classmethod
    def _logic(cls):
        """ 풀이 """
        cls._0_count, cls._1_count = 0, 0
        for idx in range(len(cls._numbers)):
            zero_or_one = cls._numbers[idx]

            if idx == 0:  # 첫번째 수 저장
                if zero_or_one == ZERO:
                    cls._0_count += 1
                else:
                    cls._1_count += 1
                continue

            # 중간 같은 부붙 PASS
            if cls._numbers[idx - 1] == cls._numbers[idx]:
                continue

            # 달라지는 부분 횟수
            if cls._numbers[idx] == ZERO:
                cls._0_count += 1
            else:
                cls._1_count += 1

        return min(cls._0_count, cls._1_count)

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

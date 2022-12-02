"""

"""
from sys import stdin as input
import heapq

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        # with open(file_name, encoding="utf-8") as input:

    def _balanced_index(self, input_string):
        """ 균형잡힌 괄호 문자열의 인덱스 반환 """
        count = 0 # 왼쪽 괄호의 개수
        for i in range(len(input_string)):
            if input_string[i] == "(":
                count += 1
            else:
                count -= 1

            if count == 0:
                return i

    def _check_proper(self, input_string):
        """ 올바른 괄호 문자열 인지 판단 """
        count = 0
        for i in input_string:
            if i == "(":
                count += 1
            else:
                if count == 0:  # 쌍이 맞지 않는 경우 False 반환
                    return False
                count -= 1
        return True # 쌍이 맞는 경우

    def _solution(self, input_string):
        """ 풀이 """
        answer = ""
        if input_string == "":
            return answer
        index = self._balanced_index(input_string)

        u = input_string[:index + 1]
        v = input_string[index + 1:]

        if self._check_proper(u):
            answer = u + self._solution(v)
        else:
            answer = "("
            answer += self._solution(v)
            answer += ")"

            u = list(u[1:-1])
            for i in range(len(u)):
                if u[i] == "(":
                    u[i] = ")"
                else:
                    u[i] = "("
            answer += "".join(u)
        return answer

    def answer(self, file_name: str = "1.txt") -> None:
        string = "()))((()"
        print(self._solution(string))

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._solution()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
"""
    데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다.

    최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데,
    문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여
    더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.

    간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데,
    이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다.

    예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다.

    "어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여
    더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

    예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만,
    > "ab ab cd cd ab ab cd cd"

    2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다.
    다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며,
    이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

    다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만,
    3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다.
    이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

    > 2걔 : "abcabc de de" : "abcabc2de"
    > 3개 : "abc abc dede" : "2abcdede"

    압축할 문자열 s가 매개변수로 주어질 때,
    위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여
    표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

    제한사항
        s의 길이는 1 이상 1,000 이하입니다.
        s는 알파벳 소문자로만 이루어져 있습니다.
"""

from sys import stdin as input
import heapq


class P:

    def __init__(self, file_name: str) -> None:
        """ 데이터 받기 """
        with open(f"./data/input/{file_name}", encoding="utf-8") as input:
            self._stirng = input.readline().strip()
            self._stirng_len = len(self._stirng)

    def _zip(self, num: int):
        """ 압축하기 """
        result = ""
        tmp_str = self._stirng[:num]
        tmp_num = 0
        for idx in range(0, self._stirng_len, num):
            cut = self._stirng[idx:idx + num]
            if len(cut) != num:  # 압축 글자 수가 다른경우
                result = f"{result}{cut}"
                continue
            if tmp_str == cut:  # 뒤에 글과 같은경우
                tmp_num += 1
                continue

            # 뒤에 글과 다른경우
            if tmp_num == 1:  # 압축이 안되는 경우
                result = f"{result}{tmp_str}"
            else:
                result = f"{result}{tmp_num}{tmp_str}"

            tmp_str = cut
            tmp_num = 1

        if tmp_num == 1:
            result = f"{result}{tmp_str}"
        else:
            result = f"{result}{tmp_num}{tmp_str}"

        return result

    def _logic(self):
        """ 풀이 """
        answer = self._stirng_len
        for div_num in range(1, self._stirng_len + 1):  # 나누는 수
            answer = min(answer, len(self._zip(num=div_num)))
        return answer

    def answer(self) -> None:
        """ 정답 출력 """
        print(self._logic())

    def answer_test(self) -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P("2.txt")
    p.answer()

"""

"""
from sys import stdin as input
from itertools import permutations


class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        # with open(file_name, encoding="utf-8") as input:
        self._N = 12
        self._weak = [1, 5, 6, 10]
        self._dist = [1, 2, 3, 4]

    def _logic(self, n, weak, dist):
        """ 풀이 """

        # 길이를 2배로 늘려서 '원형'을 일자형태로 변형
        length = len(weak)
        for i in range(length):
            weak.append(weak[i] + n)

        answer = len(dist) + 1 # 친구수를 우선 최대값으로 설정

        # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
        for start in range(length):
            # 친구를 나열하는 모든 경우 각각에 대하여 확인
            for friends in permutations(dist, len(dist)):
                count = 1 # 투입 한 친구의 수
                # 해당 친구가 점검할 수 있는 마지막 위치
                position = weak[start] + friends[count - 1]
                # 시작점부터 모든 취약한 지점을 확인
                for index in range(start, start + length):
                    # 점검할 수 있는 위치를 벗어나는 경우
                    if position < weak[index]:
                        count += 1  # 새로운 친구를 투입
                        if count > len(dist):  # 더 투입이 불가능하다면 종료
                            break
                        position = weak[index] + friends[count - 1]
                answer = min(answer, count)  # 최솟값 계산
        if answer > len(dist):
            return -1
        return answer

    def answer(self, file_name: str = "1.txt") -> None:
            print(self._logic(self._N, self._weak, self._dist))

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic(self._N, self._weak, self._dist)


if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
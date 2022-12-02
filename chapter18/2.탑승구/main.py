"""
    문제
    오늘은 신승원의 생일이다.

    박승원은 생일을 맞아 신승원에게 인천국제공항을 선물로 줬다.

    공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.

    공항에는 P개의 비행기가 순서대로 도착할 예정이며,
    당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G)
    번째 게이트중 하나에 영구적으로 도킹하려 한다.
    비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고,
    이후 어떤 비행기도 도착할 수 없다.

    신승원은 가장 많은 비행기를 공항에 도킹시켜서
    박승원을 행복하게 하고 싶어한다.
    승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?

    입력
    첫 번째 줄에는 게이트의 수 G (1 ≤ G ≤ 105)가 주어진다.
    두 번째 줄에는 비행기의 수 P (1 ≤ P ≤ 105)가 주어진다.
    이후 P개의 줄에 gi (1 ≤ gi ≤ G) 가 주어진다.

    출력
    승원이가 도킹시킬 수 있는 최대의 비행기 수를 출력한다.
"""
from sys import stdin as input
import heapq

class P:

    def __init__(self, file_name: str = "1.txt"):
        """ 생성자 """
        with open(file_name, encoding="utf-8") as input:
            # 탑승구의 개수 입력받기
            self._g = int(input.readline())
            # 비행기의 개수 입력받기
            self._p = int(input.readline())
            self._parent = [0] * (self._g + 1)  # 부모 테이블 초기화

            # 부모 테이블상에서, 부모를 자기 자신으로 초기화
            for i in range(1, g + 1):
                self._parent[i] = i

            self._result = 0
            for _ in range(p):
                data = self._find_parent(self._parent, int(input.readline()))  # 현재 비행기의 탑승구의 루트 확인
                if data == 0:  # 현재 루트가 0이라면, 종료
                    break
                self._union_parent(self._parent, data, data - 1)  # 그렇지 않다면 바로 왼쪽의 집합과 합치기
                self._result += 1

    def _find_parent(self, parent, x):
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x] != x:
            parent[x] = self._find_parent(parent, parent[x])
        return parent[x]

    # 두 원소가 속한 집합을 합치기
    def _union_parent(self,parent, a, b):
        a = self._find_parent(parent, a)
        b = self._find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def _logic(self):
        """ 풀이 """
        return self._result

    def answer(self) -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()

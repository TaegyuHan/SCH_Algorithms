"""

"""
from sys import stdin as input

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            # 노드의 개수와 간선의 개수 입력받기
            self._n, self._m = map(int, input.readline().split())
            self._parent = [0] * (self._n + 1)  # 부모 테이블 초기화

            # 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
            self._edges = []

            # 부모 테이블상에서, 부모를 자기 자신으로 초기화
            for i in range(1, self._n + 1):
                self._parent[i] = i

            # 모든 간선에 대한 정보를 입력받기
            for _ in range(self._m):
                x, y, z = map(int, input.readline().split())
                # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
                self._edges.append((z, x, y))
            self._edges.sort()

    def _find_parent(self, parent, x):
        # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        if parent[x] != x:
            parent[x] = self._find_parent(parent, parent[x])
        return parent[x]

    # 두 원소가 속한 집합을 합치기
    def _union_parent(self, parent, a, b):
        a = self._find_parent(parent, a)
        b = self._find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def _logic(self):
        """ 풀이 """
        result = 0
        total = 0  # 전체 가로등 비용

        # 간선을 하나씩 확인하며
        for edge in self._edges:
            cost, a, b = edge
            total += cost
            # 사이클이 발생하지 않는 경우에만 집합에 포함
            if self._find_parent(self._parent, a) != self._find_parent(self._parent, b):
                self._union_parent(self._parent, a, b)
                result += cost

        return total - result

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
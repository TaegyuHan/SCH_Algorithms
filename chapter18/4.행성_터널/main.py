"""

"""
from sys import stdin as input

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            # 노드의 개수 입력받기
            self._n = int(input.readline())
            self._parent = [0] * (self._n + 1)  # 부모 테이블 초기화

            # 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
            self._edges = []

            # 부모 테이블상에서, 부모를 자기 자신으로 초기화
            for i in range(1, self._n + 1):
                self._parent[i] = i

            self._x = []
            self._y = []
            self._z = []

            # 모든 노드에 대한 좌표 값 입력받기
            for i in range(1, self._n + 1):
                data = list(map(int, input.readline().split()))
                self._x.append((data[0], i))
                self._y.append((data[1], i))
                self._z.append((data[2], i))
            self._x.sort()
            self._y.sort()
            self._z.sort()

    def _logic(self):
        """ 풀이 """
        result = 0
        # 인접한 노드들로부터 간선 정보를 추출하여 처리
        for i in range(self._n - 1):
            # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
            self._edges.append((self._x[i + 1][0] - self._x[i][0], self._x[i][1], self._x[i + 1][1]))
            self._edges.append((self._y[i + 1][0] - self._y[i][0], self._y[i][1], self._y[i + 1][1]))
            self._edges.append((self._z[i + 1][0] - self._z[i][0], self._z[i][1], self._z[i + 1][1]))

        # 간선을 비용순으로 정렬
        self._edges.sort()

        # 간선을 하나씩 확인하며
        for edge in self._edges:
            cost, a, b = edge
            # 사이클이 발생하지 않는 경우에만 집합에 포함
            if self._find_parent(self._parent, a) != self._find_parent(self._parent, b):
                self._union_parent(self._parent, a, b)
                result += cost

        return result

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
"""
    첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다.

    - N은 2이상 100,000이하인 정수
    - M은 1이상 1,000,000이하인 정수
    - 유지비가 C (1 ≤ C ≤ 1,000)
"""
from sys import stdin as input
import heapq


class UnionFind:

    def __init__(self, node_count: int):
        self._node_count = node_count
        self._parents_node = [i for i in range(node_count + 1)]
        self._union_count = 1
        self._last_point = 0
        self._sum_point = 0

    def union(self, node1: int, node2: int, cost: int):
        """ 합 """
        pnode1 = self.find(node1)
        pnode2 = self.find(node2)

        if pnode1 == pnode2:
            return

        if pnode1 < pnode2:
            self._parents_node[pnode2] = pnode1
        else:
            self._parents_node[pnode1] = pnode2

        self._union_count += 1
        self._sum_point += cost
        self._last_point = cost

    @property
    def union_count(self):
        return self._union_count

    @property
    def sum_point(self):
        return self._sum_point

    @property
    def answer(self):
        return self._sum_point - self._last_point

    def find(self, node):
        """ 부고 찾기 """
        if node != self._parents_node[node]:
            self._parents_node[node] = \
                self.find(self._parents_node[node])
        return self._parents_node[node]


class P:
    _nodes = []
    _union_find: UnionFind
    _node_count: int
    _heapq = []

    @classmethod
    def _input_data(cls, file_name):
        """ 데이터 받기 """
        # with open(file_name, encoding="utf-8") as input:
        cls._node_count, edges = map(int, input.readline().split())
        cls._union_find = UnionFind(cls._node_count)
        for _ in range(edges):
            node1, node2, cost = map(int, input.readline().split())
            heapq.heappush(cls._heapq, (cost, node1, node2))

    @classmethod
    def _logic(cls):
        """ 풀이 """
        while cls._heapq:
            cost, node1, node2 = heapq.heappop(cls._heapq)
            cls._union_find.union(node1, node2, cost)
            if cls._union_find.union_count == cls._node_count:
                break
        return cls._union_find.answer

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

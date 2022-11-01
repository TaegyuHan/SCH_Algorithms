"""
    첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다.

    - N은 2이상 100,000이하인 정수
    - M은 1이상 1,000,000이하인 정수
    - 유지비가 C (1 ≤ C ≤ 1,000)
"""
from sys import stdin as input
import heapq


class Node:

    def __init__(self, node1: int, node2: int, cost: int):
        self._node1 = node1
        self._node2 = node2
        self._cost = cost
        self._sort_point = -self._cost

    def __repr__(self):
        """ 읽기 """
        return f"({self._node1}, {self._node2}, {self._cost})"

    def __lt__(self, other):
        """ 가중치 크기 비교 """
        return self._sort_point > other.sort_point

    def __gt__(self, other):
        """ 가중치 크기 비교 """
        return self._sort_point < other.sort_point

    def __le__(self, other):
        """ 가중치 크기 비교 """
        return self._sort_point >= other.sort_point

    def __ge__(self, other):
        """ 가중치 크기 비교 """
        return self._sort_point <= other.sort_point

    @property
    def nodes_and_cost(self):
        """ 데이터 """
        return self._node1, self._node2, self._cost

    @property
    def cost(self):
        """ 가중치 """
        return self._cost

    @property
    def sort_point(self):
        """ 가중치 """
        return self._sort_point


class UnionFind:

    def __init__(self, node_count: int):
        self._parents_node = [i for i in range(node_count + 1)]
        self._point_sum = 0
        self._last_point = 0
        self._union_count = 1

    def union(self, node1: int, node2: int, cost: int):
        """ 합하기 """
        if node1 < node2:
            self._parents_node[node2] = node1
        else:
            self._parents_node[node1] = node2
        self._union_count += 1
        self._point_sum += cost
        self._last_point = cost

    @property
    def union_count(self):
        """ 합 횟수 """
        return self._union_count

    def find(self, node):
        """ 부고 찾기 """
        if node != self._parents_node[node]:
            self._parents_node[node] = \
                self.find(self._parents_node[node])
        return self._parents_node[node]

    def answer(self):
        return self._point_sum - self._last_point


class P:
    _node_heapq = []
    _union_find: UnionFind
    _node_count: int

    @classmethod
    def _input_data(cls, file_name):
        """ 데이터 받기 """
        # with open(file_name, encoding="utf-8") as input:
        cls._node_count, edges = map(int, input.readline().split())
        cls._union_find = UnionFind(node_count=cls._node_count)
        for _ in range(edges):
            node1, node2, cost = map(int, input.readline().split())
            heapq.heappush(cls._node_heapq, Node(node1, node2, cost))

    @classmethod
    def _logic(cls) -> None:
        """ 풀이 로직 """
        while cls._node_heapq:
            node = heapq.heappop(cls._node_heapq)
            node1, node2, cost = node.nodes_and_cost
            if cls._union_find.find(node1) == cls._union_find.find(node2):
                continue
            cls._union_find.union(node1, node2, cost)
            if cls._union_find.union_count == cls._node_count:
                break

    @classmethod
    def answer(cls, file_name: str = "1.txt") -> None:
        cls._input_data(file_name)
        cls._logic()
        print(cls._union_find.answer())

    @classmethod
    def answer_test(cls, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        cls._input_data(file_name)
        cls._logic()
        return cls._union_find.answer()


if __name__ == '__main__':
    P.answer(file_name="./data/input/1.txt")

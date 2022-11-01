"""
    첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다.

    - N은 2이상 100,000이하인 정수
    - M은 1이상 1,000,000이하인 정수
    - 유지비가 C (1 ≤ C ≤ 1,000)
"""
from sys import stdin as input


class Node:

    def __init__(self, node1: int, node2: int, cost: int):
        self._node1 = node1
        self._node2 = node2
        self._cost = cost

    def __repr__(self):
        """ 읽기 """
        return f"({self._node1}, {self._node2}, {self._cost})"

    @property
    def nodes_and_cost(self):
        """ 데이터 """
        return self._node1, self._node2, self._cost

    @property
    def cost(self):
        """ 가중치 """
        return self._cost


class UnionFind:

    def __init__(self, node_count: int):
        self._parents_node = [i for i in range(node_count + 1)]
        self._point_sum = 0
        self._count = 2

    def union(self, node1: int, node2: int, cost: int):
        """ 합하기 """
        if node1 < node2:
            self._parents_node[node2] = node1
        else:
            self._parents_node[node1] = node2
        self._point_sum += cost
        self._count += 1

    @property
    def count(self):
        """ 합 횟수 """
        return self._count

    def find(self, node):
        """ 부고 찾기 """
        if node != self._parents_node[node]:
            self._parents_node[node] = \
                self.find(self._parents_node[node])
        return self._parents_node[node]

    def answer(self):
        return self._point_sum


class P:
    _nodes = []
    _union_find: UnionFind
    _node_count: int

    @classmethod
    def _input_data(cls, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            cls._node_count, edges = map(int, input.readline().split())
            cls._union_find = UnionFind(node_count=cls._node_count)

            for _ in range(edges):
                node1, node2, cost = map(int, input.readline().split())
                cls._nodes.append(Node(node1, node2, cost))

            cls._nodes.sort(key=lambda x: x.cost)

    @classmethod
    def _logic(cls) -> None:
        """ 풀이 로직 """
        for node in cls._nodes:
            if cls._union_find.count == cls._node_count:
                break

            node1, node2, cost = node.nodes_and_cost

            if cls._union_find.find(node1) == cls._union_find.find(node2):
                continue

            cls._union_find.union(node1, node2, cost)

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

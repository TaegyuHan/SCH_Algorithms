"""
    [문제]
    한울이가 사는 나라에는 N개의 여행지가 있으며, 각 여행지는
    1 ~ N번까지의 번호로 구분됩니다.

    또한 임의의 두 여행지 사이에는 두 여행지를 연결하는
    도로가 존재할 수 있습니다.

    이때, 여행지가 도로로 연결되어 있다면 양항향으로 이동이
    가능하다는 의미입니다.

    한울이는 하나의 여행 계획을 세운 뒤에 이
    여행 계획이 가능한지의 여부를 판단하고자 합니다.

    예를 들어 N = 5이고,
    다음과 같이 도로의 정보가 주어졌다고 가정합시다.

    1번 여행지 - 2번 여행지
    1번 여행지 - 4번 여행지
    1번 여행지 - 5번 여행지
    2번 여행지 - 3번 여행지
    2번 여행지 - 4번 여행지
    만약 한울이의 여행 계획이 2번 -> 3번 -> 4번 -> 3번이라고 해봅시다.
    이 경우 2번 -> 3번 -> 2번 -> 4번 -> 2번 -> 3번의

    순서로 여행지를 방문하면, 여행 계획을 따를 수 있습니다.

    여행지의 개수와 여행지 간의 연결 정보가 주어졌을 때,
    한울이의 여행 계획이 가능한지의 여부를 판별하는
    프로그램을 작성하세요.

    [입력 조건]
    1. 첫째 줄에 여행지의 수 N과 여행 계획에 속한 도시의 수 M이 주어집니다. (1 <= N, M <= 500)

    2. 다음 N개의 줄에 걸쳐 N x N 행렬을 통해 임의의 두 여행지가 서로 연결되어 있는지의 여부가 주어집니다.
       그 값이 1이라면 서로 연결되었다는 의미이며, 0이라면 서로 연결되어 있지 않다는 의미입니다.

    3. 마지막 줄에 한울이의 여행 계획에 포함된 여행지의 번호들이 주어지며 공백으로 구분합니다.

    [출력 조건]
    첫째 줄에 한울이의 여행 계획이 가능하다면 YES를, 불가능하다면 NO를 출력합니다.
"""
from sys import stdin as input

class P:

    def __init__(self, file_name: str = "1.txt"):
        """ 생성자 """
        with open(file_name, encoding="utf-8") as input:
            self._node_count, self._edge_count = map(int, input.readline().split())
            self._board = [list(map(int, input.readline().split())) for _ in range(self._node_count)]
            self._visited_node = set(map(int, input.readline().split()))
            self._parents_node = [i for i in range(self._node_count + 1)]

    def _union(self, node1, node2):
        """ 합 집합 """
        parents_node1 = self._find(node1)
        parents_node2 = self._find(node2)

        if self._board[parents_node1][parents_node2]:
            return True

        if parents_node1 <= parents_node2:
            self._parents_node[node2] = parents_node1
        else:
            self._parents_node[node1] = parents_node2
        return False

    def _find(self, node):
        """ 합 집합 """
        if node != self._parents_node[node]:
            self._parents_node[node] = self._find(self._parents_node[node])
        return self._parents_node[node]

    def _logic(self):
        """ 풀이 """
        start = self._visited_node.pop()
        for city in self._visited_node:
            if self._union(start, city):
                return "NO"
        return "YES"

    def answer(self) -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()

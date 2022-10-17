"""
    [문제]
        미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
        방문 판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다.
        미래 도시에서 특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일하다.
        또한 연결된 2개의 회사는 양방향으로 이동할 수 있다. 공중 미래 도시에서 특정 회사와 다른 회사가 도로로 연결되어
        있다면, 정확히 1만큼의 시간으로 이동할 수 있다.
        또한 오늘 방문 판매원 A는 기대하던 소개팅에도 참석하고자 한다. 소개팅의 상대는 K번 회사에 존재한다.
        방문 판매원 A는 X번 회사에 가서 물건을 판매하기 전에 먼저 소개팅 상대의 회사에 찾아가서 함께 커피를 마실 예정이다.
        따라서 방문 판매원 A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표다.
        이때 방문 판매원 A는 가능한 한 빠르게 이동하고자 한다.
        방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.

        [입력 조건]
            1. 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다. (1 <= N, M <= 100)
            2. 둘째 줄부터 M + 1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
                M + 2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다. (1 <= K <= 100)

        [출력 조건]
            1. 첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
            2. 만약 X번 회사에 도달할 수 없다면 -1을 출력한다.

"""
from sys import stdin as input
import heapq

InF = float("inf")


class P:
    """ 문제 클래스 """
    _node: int
    _edge: int
    _loads: list[list[int]]
    _visited: list[float]
    _X: int
    _K: int

    def __init__(self) -> None:
        """ 생성자 """
        self._input()

    @classmethod
    def _input(cls) -> None:
        """ 데이터 받기 """
        input = open('./test/original.txt', encoding="utf-8")
        cls._node, cls._edge = map(int, input.readline().split())
        cls._loads = [[] for _ in range(cls._node + 1)]

        for _ in range(cls._edge):
            node1, node2 = map(int, input.readline().split())
            cls._loads[node1].append(node2)
            cls._loads[node2].append(node1)

        cls._X, cls._K = map(int, input.readline().split())

    @classmethod
    def _dijkstra_logic(cls, start_node: int, end_node: int) -> int:
        """ 다익스트라 로직 """
        cls._visited = [InF for _ in range(cls._node + 1)]
        cls._visited[start_node] = 0

        heapq_data = []
        heapq.heappush(heapq_data, start_node)
        while heapq_data:
            cnode = heapq.heappop(heapq_data)
            for nnode in cls._loads[cnode]:
                if cls._visited[nnode] != InF: continue
                cls._visited[nnode] = cls._visited[cnode] + 1
                heapq.heappush(heapq_data, nnode)

        if cls._visited[end_node] == InF:
            print(-1)
            exit()

        return cls._visited[end_node]

    @classmethod
    def answer(cls) -> None:
        print(cls._dijkstra_logic(start_node=1, end_node=cls._X) \
              + cls._dijkstra_logic(start_node=1, end_node=cls._K))


if __name__ == '__main__':
    p = P()
    p.answer()
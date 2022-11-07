"""
     N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.

    입력
    첫째 줄에 도시의 개수 N,
    도로의 개수 M,
    거리 정보 K,

    출발 도시의 번호 X가 주어진다.
    (2 ≤ N ≤ 300,000)
    (1 ≤ M ≤ 1,000,000)
    (1 ≤ K ≤ 300,000)
    (1 ≤ X ≤ N)

    둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수
    A, B가 공백을 기준으로 구분되어 주어진다.
    이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다.
    (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.


    출력
    X로부터 출발하여 도달할 수 있는 도시 중에서,
    최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩
    오름차순으로 출력한다.

    이 때 도달할 수 있는 도시 중에서,
    최단 거리가 K인 도시가 하나도 존재하지
    않으면 -1을 출력한다.
"""
from sys import stdin as input
from collections import deque

VISITED = True
NOT_VISITED = False

class P:

    def __init__(self, file_name: str = "1.txt"):
        """ 생성자 """
        with open(file_name, encoding="utf-8") as input:
            self._node_count, self._edge_count, \
            self._length, self._start_node = map(int, input.readline().split())

            self._edges = [[] for _ in range(self._node_count + 1)]
            for _ in range(self._edge_count):
                go, end = map(int, input.readline().split())
                self._edges[go].append(end)

    def _bfs(self, start_node: int) -> list[int]:
        visited = [NOT_VISITED for _ in range(self._node_count + 1)]
        answer = []
        q = deque([(start_node, 0)])
        while q:
            cnode, length = q.popleft()
            if visited[cnode]:  # 이미 방문한 노드
                continue
            visited[cnode] = VISITED

            if self._length == length:
                answer.append(cnode)
                continue

            for nnode in self._edges[cnode]:
                if visited[nnode]:  # 이미 방문한 노드
                    continue
                # 길이 넘어가는 경우
                if self._length < (nlength := length + 1):
                    continue
                q.append((nnode, nlength))
        answer.sort()

        if answer:
            return answer
        return [-1]

    def _logic(self):
        """ 풀이 """
        return self._bfs(start_node=self._start_node)

    def answer(self, ) -> None:
        for node in self._logic():
            print(node)

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()

"""

"""
from sys import stdin as input
import heapq
import sys

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

class P:

    def __init__(self, file_name):
        """ 데이터 받기 """
        with open(file_name, encoding="utf-8") as input:
            # 노드의 개수, 간선의 개수를 입력받기
            self._n, self._m = map(int, input.readline().split())
            # 시작 노드를 1번 헛간으로 설정
            start = 1
            # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
            self._graph = [[] for i in range(self._n + 1)]
            # 최단 거리 테이블을 모두 무한으로 초기화
            self._distance = [INF] * (self._n + 1)

            # 모든 간선 정보를 입력받기
            for _ in range(self._m):
                a, b = map(int, input.readline().split())
                # a번 노드와 b번 노드의 이동 비용이 1이라는 의미(양방향)
                self._graph[a].append((b, 1))
                self._graph[b].append((a, 1))

    def _dijkstra(self, start):
        q = []
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q, (0, start))
        self._distance[start] = 0
        while q:  # 큐가 비어있지 않다면
            # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if self._distance[now] < dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in self._graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < self._distance[i[0]]:
                    self._distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    def _logic(self):
        """ 풀이 """
        # 다익스트라 알고리즘을 수행
        start = 1
        self._dijkstra(start)

        # 가장 최단 거리가 먼 노드 번호(동빈이가 숨을 헛간의 번호)
        max_node = 0
        # 도달할 수 있는 노드 중에서, 가장 최단 거리가 먼 노드와의 최단 거리
        max_distance = 0
        # 가장 최단 거리가 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트
        result = []

        for i in range(1, self._n + 1):
            if max_distance < self._distance[i]:
                max_node = i
                max_distance = self._distance[i]
                result = [max_node]
            elif max_distance == self._distance[i]:
                result.append(i)

        print(max_node, max_distance, len(result))

    def answer(self, file_name: str = "1.txt") -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()

if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()
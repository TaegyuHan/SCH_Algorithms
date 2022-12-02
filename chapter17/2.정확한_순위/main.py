"""
    선생님은 시험을 본 학생 N명의 성적을 분실하고,
    성적을 비교한 결과의 일부만 가지고 있다.

    학생 N명의 성적은 모두 다른데,
    다음은 6명의 학생에 대해 6번만 성적을 비교한 결과이다.

    1번 성적 < 5번 성적
    3번 성적 < 4번 성적
    4번 성적 < 2번 성적
    4번 성적 < 6번 성적
    5번 성적 < 2번 성적
    5번 성적 < 4번 성적
"""
from sys import stdin as input

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

class P:

    def __init__(self, file_name: str = "1.txt"):
        """ 생성자 """
        with open(file_name, encoding="utf-8") as input:
            # 노드의 개수, 간선의 개수를 입력받기
            self._n, self._m = map(int, input.readline().split())
            # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
            self._graph = [[INF] * (self._n + 1) for _ in range(self._n + 1)]

    def _logic(self):
        """ 풀이 """
        for a in range(1, self._n + 1):
            for b in range(1, self._n + 1):
                if a == b:
                    self._graph[a][b] = 0

        # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
        for _ in range(self._m):
            # A에서 B로 가는 비용을 1로 설정
            a, b = map(int, input().split())
            self._graph[a][b] = 1

        # 점화식에 따라 플로이드 워셜 알고리즘을 수행
        for k in range(1, self._n + 1):
            for a in range(1, self._n + 1):
                for b in range(1, self._n + 1):
                    self._graph[a][b] = min(self._graph[a][b], self._graph[a][k] + self._graph[k][b])

        result = 0
        # 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
        for i in range(1, self._n + 1):
            count = 0
            for j in range(1, self._n + 1):
                if self._graph[i][j] != INF or self._graph[j][i] != INF:
                    count += 1
            if count == self._n:
                result += 1
        return result

    def answer(self) -> None:
        print(self._logic())

    def answer_test(self, file_name: str = "1.txt") -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P(file_name="./data/input/1.txt")
    p.answer()

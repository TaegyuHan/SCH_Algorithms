"""
   학교에서 학생들에게 0번부터 N번까지의 번호를 부여했다. 처음에는 모든 학생이
   서로 다른 팀으로 구분되어, 총 N + 1 개의 팀이 존재한다. 이때 선생님은
   '팀 합치기'연산과 '같은 팀 여부 확인'연산을 사용할 수 있다.

    '팀 합치기' 연산은 두 팀을 합치는 연산이다.
    '같은 팀 여부 확인' 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.
    선생님이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인'연산에
    대한 연산 결과를 출력하는 프로그램을 작성하시오.

    첫째 줄에 N, M이 주어진다. M은 입력으로 주어지는 연산의 개수이다. (1 <= N, M <= 100,000)
    다음 M개의 줄에는 각각의 연산이 주어진다.
    '팀 합치기' 연산은 0 a b 형태로 주어진다. 이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미이다.
    '같은 팀 여부 확인' 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해 있는지를 확인하는 연산이다.
    a와 b는 N 이하의 양의 정수이다.
    '같은 팀 여부 확인'연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과를 출력한다.
"""
import sys

sys.setrecursionlimit(10 ** 6)
UNION = 0
FIND = 1


class UnionFind:
    """ 유니온 파인드 """

    def __init__(self, node_count: int):
        self._parents = [i for i in range(node_count + 1)]

    def union(self, node1: int, node2: int):
        """ 합집합 """
        pnode1 = self.find(node1)
        pnode2 = self.find(node2)

        if pnode1 < pnode2:
            self._parents[node2] = pnode1
        else:
            self._parents[node1] = pnode2

    def find(self, node: int):
        """ 집합 확인 """
        if self._parents[node] != node:
            return self.find(self._parents[node])
        return node

    def find_check(self, node1: int, node2: int):
        if self.find(node1) == self.find(node2):
            return "YES"
        return "NO"

    def array_check(self):
        """ 배열확인하기 """
        return self._parents


class P:
    _edges: int
    _union_find: UnionFind
    _answer_list = []

    @classmethod
    def _input(cls):
        """ 데이터 받기 """
        input = open("./test/original.txt")
        node, cls._edges = map(int, input.readline().split())
        cls._union_find = UnionFind(node)

        for _ in range(cls._edges):
            check, node1, node2 = map(int, input.readline().split())
            if check == UNION:
                cls._union_find.union(node1, node2)
            elif check == FIND:
                print(cls._union_find.find_check(node1, node2))  # answer
            else:
                pass

    @classmethod
    def answer(self):
        """ 정답 """
        self._input()


if __name__ == '__main__':
    P.answer()
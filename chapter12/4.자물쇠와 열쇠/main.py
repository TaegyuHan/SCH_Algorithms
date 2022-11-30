"""
    고고학자인 "튜브"는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다.
    그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 문 앞에는 특이한 형태의 열쇠와 함께
    자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.

    잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자
    형태이고 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

    자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다.
    열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈
    부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다.

    자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는
    데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의
    홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다.
    또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.
"""
import heapq
from sys import stdin as input


class P:

    def __init__(self) -> None:
        """ 데이터 받기 """

    def _show_board(self, board):
        """ 판 확인하기 """
        for row in board:
            print(*row, sep="\t")
        print()

    def _turn_key(self, key):
        """ 90도 돌리기 """
        row_size = len(key)
        col_size = len(key[0])
        result = [[0] * row_size for _ in range(col_size)]  # 결과 리스트
        for row in range(row_size):
            for col in range(col_size):
                result[col][row_size - row - 1] = key[row][col]
        return result

    def _check(self, new_lock):
        self._show_board(new_lock)
        lock_size = len(new_lock) // 3
        for row in range(lock_size, lock_size * 2):
            for col in range(lock_size, lock_size * 2):
                if new_lock[row][col] != 1:
                    return False
        return True

    def _key_in(self, new_lock, key, start_row, start_col):
        """ 키 넣기 """
        for i in range(len(key)):
            for j in range(len(key)):
                new_lock[start_row + i][start_col + j] += key[i][j]

    def _key_out(self, new_lock, key, start_row, start_col):
        """ 키 빼기 """
        for i in range(len(key)):
            for j in range(len(key)):
                new_lock[start_row + i][start_col + j] -= key[i][j]

    def _logic(self, key, lock):
        """ 풀이 """
        lock_size = len(lock)

        # 자물쇠의 크기에 key를 넣기 위해서 3배로 변환
        new_lock = [[0] * (lock_size * 3) for _ in range(lock_size * 3)]

        # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
        for row in range(lock_size):
            for col in range(lock_size):
                new_lock[row + lock_size][col + lock_size] = lock[row][col]

        # 4가지 방향에 대해서 확인
        for rotation in range(4):
            self._show_board(key)
            key = self._turn_key(key)

            for row_start in range(lock_size * 2):
                for col_start in range(lock_size * 2):
                    self._key_in(new_lock, key, row_start, col_start)
                    if self._check(new_lock):
                        return True
                    self._key_out(new_lock, key, row_start, col_start)
        return False

    def answer(self) -> None:
        """ 정답 출력 """
        print(self._logic(key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]], lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

    def answer_test(self) -> None:
        """ 테스트 정답 출력 """
        return self._logic()


if __name__ == '__main__':
    p = P()
    p.answer()

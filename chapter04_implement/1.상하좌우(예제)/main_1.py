from sys import stdin as input
import sys; sys.setrecursionlimit(2500)
input = open('./test/original.txt')

n = int(input.readline())
directions = list(input.readline().split())

DIRECTIONS = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1)
}

def main():
    """  """
    position = (1, 1)

    for direction in directions:
        trow, tcol = DIRECTIONS[direction]
        crow, ccol = position
        nrow, ncol = trow + crow, tcol + ccol
        if not (1 <= nrow <= n and 1 <= ncol <= n):
            continue
        position = (nrow, ncol)

    print(*position)

if __name__ == '__main__':
    main()
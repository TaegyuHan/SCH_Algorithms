"""
    두배열의 원소 교체
"""
from sys import stdin as input

input = open('./test/original.txt', encoding="utf-8")
n, m = map(int, input.readline().split())
rice_cakes = list(map(int, input.readline().split()))
rice_cakes.sort()
start, end = 0, rice_cakes[-1]
answer = 0

while start < end:
    total = 0
    mid = (start + end) // 2

    # 자른 양 구하기
    for rice_cake in rice_cakes:
       if rice_cake > mid:
           total += rice_cake - mid

    # 2분 탐색
    if total < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)
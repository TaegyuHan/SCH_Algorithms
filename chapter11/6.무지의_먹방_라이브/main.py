import heapq

class P:

    _heapq: list[int] = []

    @classmethod
    def solution(cls, food_times: list[int], k: int):
        """ 풀이 """
        answer = 0
        for idx in range(len(food_times)):
            heapq.heappush(cls._heapq, (food_times[idx], idx + 1))

        # 만약 더 섭취해야 할 음식이 없다면 -1
        if sum(food_times) < k:
            return -1

        # 음식 제거
        while cls._heapq:
            if (food_count := len(cls._heapq)) <= k:  # 시간 비교
                for _ in range(pop_count := k // len(cls._heapq)):
                    heapq.heappop(cls._heapq)
                k -= (pop_count * food_count)
                continue

            cls._heapq.sort(key=lambda x:x[1], reverse=True)
            _, answer = cls._heapq.pop()
            break
        return answer

def solution(food_times, k):
    return P.solution(food_times=food_times, k=k)
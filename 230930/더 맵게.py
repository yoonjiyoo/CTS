import heapq


def solution(S, K):
    heap = []
    for i in S:
        heapq.heappush(heap, i)

    cnt = 0
    while heap[0] < K:
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        cnt += 1

        if len(heap) == 1 and heap[0] < K:  # 숫자 하나 남았는데 0번째가 K보다 작으면
            return -1  # -1을 return (K이상으로 만들 수 없으므로)
    return cnt

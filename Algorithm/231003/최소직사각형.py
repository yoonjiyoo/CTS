def solution(sizes):
    answer = 0

    long = []
    short = []
    # 긴 변은 긴 변끼리 비교
    # 짧은 변은 짧은 변끼리 비교

    for i in range(0, len(sizes)):
        long.append(max(sizes[i][0], sizes[i][1]))
        short.append(min(sizes[i][0], sizes[i][1]))

    long.sort()
    short.sort()
    answer = max(long) * max(short)

    return answer

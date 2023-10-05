def solution(clothes):
    # 아무것도 입지 않은 경우를 answer에 저장
    answer = 1

    # clothes의 의상의 종류를 딕셔너리의 Key값으로,
    # value를 빈 리스트로 저장
    c = {v[1]: [] for v in clothes}

    # clothes의 값을 하나씩 꺼내며 c의 value에 추가
    for clo in clothes:
        c[clo[1]].append(clo[0])

    # 딕셔너리 c의 key값을 꺼내면서 value의 길이 +1을 answer에 곱해줌
    for k in c.keys():
        n = len(c[k])
        answer *= n + 1

    # 아무것도 입지 않은 경우를 answer에서 뺀 후 반환
    return answer - 1


# 가장 추천수가 많은 코드
def solution(clothes):
    from collections import Counter
    from functools import reduce

    # Counter 함수를 통해 의상의 종류 내에 의상이 몇 개가 있는지 계산하여 cnt에 저장
    cnt = Counter([kind for nmae, kind in clothes])
    """
    reduce를 통해 cnt의 value를 모두 곱해준 후 -1을 함
    lambda x, y : x*(y+1) = reduce에 적용할 함수로 기존 값에 (새로운 값 + 1)을 곱해주는 함수 
    reduce(lambda x, y : x*(y+1), cnt.values(), 1) = 1부터 시작해서 cnt의 values를 불러오면서 lambda 함수를 적용
        예시)
            cnt = {'a' : 2, 'b' : 3} 인 경우, 위 reduce를 사용하면
            첫 번째 연산 : 1 * (2 + 1) = 3
            두 번째 연산 : 3 * (3 + 1) = 12
    """
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer

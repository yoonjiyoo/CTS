def solution(array, commands):
    answer = []
    res = []

    for i in range(0, len(commands)):
        s = commands[i][0]
        e = commands[i][1]
        c = commands[i][2]
        res = array[s - 1 : e]
        res.sort()
        answer.append(res[c - 1])

    return answer


# ---다른사람의 풀이


def solution(array, commands):
    answer = []

    for i in commands:
        ary = array[i[0] - 1 : i[1]]  # 문제에서 주어진 크기만큼 자르기
        ary.sort()  # sort 함수로 정렬
        answer.append(ary[i[2] - 1])  # k 번째 값 집어넣기

    return answer


# ---가장 추천수 많은 풀이
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1 : x[1]])[x[2] - 1], commands))


# lambda x:이후부터 sorted=오름차순정렬
# 순서대로 array를 commands의 [0]번째 인덱스-1~1번째 인덱스까지 슬라이싱하고
# sorted한 뒤 commands의 [2]-1번째 인덱스를 뽑음

# map 과 lambda 함수
# - map(함수, 리스트) 여러 개의 데이터를 한번에 다른 형태로 변환하기 위해서 사용됩니다.
# - lambda 인자 : 표현식

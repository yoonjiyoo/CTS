"""
not answer는 answer 리스트가 비어있는지 확인하는 조건임. answer 리스트가 비어있으면 중복 여부를 확인할 이전 요소가 없으므로 현재 요소를 answer에 추가해야 함. 
안쓰면 list index out of range 오류가 뜸!!! 아무 원소도 없는데 -1번째 비교하라하니까
"""


def solution(arr):
    answer = []

    for i in arr:
        if not answer or answer[-1] != i:
            answer.append(i)

    return answer

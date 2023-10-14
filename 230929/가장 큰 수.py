"""
1. 최초 numbers 리스트를 string으로 바꾸어준다. (숫자의 맨 앞자리부터 비교 가능)

2. sort 옵션 
key=lambda x: x[1] 
특정 조건을 주어 정렬하고 싶을 때 쓰임

ex)
(1) 숫자의 경우
    .sort(key=lambda x:x[1]) #x[1]의 값이 정렬의 기준 (key)
    .sort(key=lambda x:(x[1],x[0])) #x[1] (첫 번째 인자)을 기준으로 우선 정렬 -> x[0] (두 번째 인자)을 기준으로 재정렬 
(2) 문자의 경우
    .sort(key=lambda x:x*3) 인자를 세번 반복. 예로 39 30 3 이 있다고 하면 393939 303030 333 으로 변경 후 이를 기준으로 정렬 (문자형 정렬이므로 앞자리부터 큰 것으로 정렬 됨)

3. 만약 입력 값이 [0,0] 일 경우 
결과값이 0이어야 하지만 문자형이므로 00으로 반환되는 문제 발생.
따라서 answer을 int로 반환한 후 다시 str로 반환하여 문제 해결

"""


def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    for i in numbers:
        answer += i

    return str(int(answer))

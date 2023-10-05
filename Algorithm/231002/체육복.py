# 제한사항 마지막에 '여벌 체육복을 가진 학생이 도난을 당한 경우, 남은 체육복이 하나이기 때문에 빌려줄 수 없다.' 라는 항목이 있다. 즉, 해당 학생은 여벌 체육복을 가지고 있지만 동시에 잃어버리기도 한 것이니 lost와 reserve 둘 다 포함이 된단 뜻이며, 체육 수업을 들을 수 있는 학생이므로 미리 제외를 시켜줘야한다. ex) lost=[1,3,5] reserve=[3,4,7] 일 경우, 3번 학생이 여벌 체육복을 갖고있으면서 잃어버린 상황에 해당 한다. 그래서 set의 차집합을 이용해 미리 제외를 시키고 진행하여 해결하였다.
"""
def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    for i in new_lost:
        if i + 1 in new_reserve:
            new_reserve.remove(i + 1)
        elif i - 1 in new_reserve:
            new_reserve.remove(i - 1)
        else:
            n-=1
    return n
    """
# 테스트케이스를 다 통과할 수 없음


def solution(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()

    # lost, reserve에 공통으로 있는 요소 제거
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)

    # 체육복 빌려주기(나의 앞 번호부터 확인)
    for i in new_reserve:
        if i - 1 in new_lost:
            new_lost.remove(i - 1)
        elif i + 1 in new_lost:
            new_lost.remove(i + 1)

    return n - len(new_lost)

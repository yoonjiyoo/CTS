"""
def solution(phone_book):
    answer = True
    cnt=0
    
    phone_len=len(phone_book[0])
    
    for i in range(1,len(phone_book)):
        if phone_book[i][:phone_len]==phone_book[0]:
            cnt+=1
            
    if cnt>=1: answer=False

    return answer

채점 결과
정확성: 62.5
효율성: 4.2
합계: 66.7 / 100.0


---

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    
    for i in range(1,len(phone_book)):
        answer=phone_book[i].startswith(phone_book[0])
        if answer==True: break

        
    return not answer

채점 결과
정확성: 70.8
효율성: 12.5
합계: 83.3 / 100.0
#!서로가 서로의 접두어인지도 확인했어야 함.
def solution(phoneBook):    
    # 1. 비교할 A선택
    for i in range(len(phoneBook)):
        # 2. 비교할 B선택
        for j in range(i+1, len(phoneBook)):
            # 3. 서로가 서로의 접두어인지 확인한다.
            if phoneBook[i].startswith(phoneBook[j]):
                return False
            if phoneBook[j].startswith(phoneBook[i]):
                return False
    return True

"""


def solution(phone_book):
    # 1. Hash map을 만든다
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1  # Key가 Phone_number, Value는 1
    """
    예를 들어, 입출력1번이라면
    hash_map은 {'119': 1, '97674223': 1, '1195524421': 1} 가 된다
    """

    # 2. 접두어가 Hash map에 존재하는지 찾는다
    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True

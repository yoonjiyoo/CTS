def solution(s):
    answer = True
    stack = []

    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                answer = False
                break
            else:
                stack.pop()

    if len(stack) != 0:
        answer = False

    return answer

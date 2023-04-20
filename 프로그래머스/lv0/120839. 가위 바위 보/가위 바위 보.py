def solution(rsp):
    answer=[]
    for i in list(rsp):
        if i == '0':
            answer.append(5)
        elif i == '2':
            answer.append(0)
        else:
            answer.append(2)
    return ''.join(str(i) for i in answer)
def solution(price, money, count):
    result=0
    for i in range(1, count+1):
        result += i
    answer = money - (price*result)
    if answer > 0:
        answer = 0
    else: answer = abs(answer)
    
    return answer

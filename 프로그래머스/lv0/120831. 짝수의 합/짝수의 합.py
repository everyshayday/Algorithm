def solution(n):
    under_n_even = []
    for i in range(1, n+1):
        if i%2 == 0:
            under_n_even.append(i)
        else:
            pass
    answer = sum(under_n_even)
    return answer
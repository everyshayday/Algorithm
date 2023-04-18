def solution(num_list):
    even_list=[]
    odd_list=[]
    for i in num_list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    answer = [len(even_list), len(odd_list)]
    return answer
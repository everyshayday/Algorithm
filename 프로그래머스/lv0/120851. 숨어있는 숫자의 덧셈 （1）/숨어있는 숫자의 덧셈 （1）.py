import re

# def solution(my_string):
#     answer=0
#     for i in my_string:
#         if i.isnumeric():
#             answer += int(i)
#     return answer


def solution(my_string):
    answer = sum(int(i) for i in re.sub(r'[^1-9]', '', my_string))
    return answer
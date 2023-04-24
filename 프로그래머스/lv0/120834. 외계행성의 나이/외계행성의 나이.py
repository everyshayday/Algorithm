def solution(age):
    age_code = ''
    for i in str(age):
        age_code += chr(ord('a') + int(i))
    return age_code
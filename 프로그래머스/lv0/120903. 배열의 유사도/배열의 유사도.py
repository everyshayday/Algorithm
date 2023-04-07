def solution(s1, s2):
    result = []
    for word1 in s1:
        for word2 in s2:
            if word1 == word2:
                result.append(word1)
    answer = len(result)
    return answer
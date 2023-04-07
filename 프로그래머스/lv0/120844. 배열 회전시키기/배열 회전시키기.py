def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0, numbers.pop())
    else:
        numbers.extend(numbers[:1])
        numbers = numbers[1:]
    
    return numbers
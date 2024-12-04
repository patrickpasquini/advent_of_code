def pt1(_input: str):
    left_numbers, right_numbers = [], []
    for line in _input.splitlines():
        left, right = line.split()
        left_numbers.append(int(left))
        right_numbers.append(int(right))
    left_numbers.sort()
    right_numbers.sort()
    result = 0
    for i in range(len(right_numbers)):
        result += abs(left_numbers[i] - right_numbers[i])
    return result


def pt2(_input: str):
    from collections import Counter

    left_numbers, right_numbers = [], []
    for line in _input.splitlines():
        left, right = line.split()
        left_numbers.append(int(left))
        right_numbers.append(int(right))

    right_count = Counter(right_numbers)
    return sum(number * right_count[number] for number in left_numbers)

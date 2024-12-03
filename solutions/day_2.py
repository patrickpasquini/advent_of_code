def base_validate(rel: list):
    is_sorted = rel == sorted(rel) or rel == sorted(rel, reverse=True)
    is_correct = True
    if is_sorted and len(rel) == len(set(rel)):
        for i in range(len(rel) - 1):
            if not 1 <= abs(rel[i] - rel[i + 1]) <= 3:
                is_correct = False
    else:
        is_correct = False
    return is_correct


def pt1(_input: str):
    result = 0
    for line in _input.splitlines():
        rel = list(map(int, line.split()))
        if base_validate(rel):
            result += 1
    return result


def pt2(_input: str):
    result = 0
    for line in _input.splitlines():
        rel = list(map(int, line.split()))
        for i in range(len(rel)):
            test = rel[:i] + rel[i + 1 :]
            if base_validate(test):
                result += 1
                break
    return result

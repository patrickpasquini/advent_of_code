from aocd import get_data
from collections import defaultdict

_input = get_data(day=5, year=2024)


def pt1():
    rules, seqs = _input.split("\n\n")
    rules_map = defaultdict(set)
    result = 0
    for rule in rules.splitlines():
        left, right = rule.split("|")
        rules_map[right].add(left)
    for s in seqs.splitlines():
        numbers = s.split(",")
        numbers.reverse()
        is_valid_seq = False
        for i in range(len(numbers) - 1):
            if numbers[i + 1] not in rules_map[numbers[i]]:
                is_valid_seq = True
                break
        if is_valid_seq:
            result += int(numbers[len(numbers) // 2])
    return result


def pt2():
    rules, seqs = _input.split("\n\n")
    rules_map = defaultdict(set)
    result = 0

    def resolve_numbers(numbers: list[str]):
        has_swapped = False
        while True:
            is_correct_seq = True
            for i in range(len(numbers) - 1):
                if numbers[i + 1] not in rules_map[numbers[i]]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    has_swapped = True
                    is_correct_seq = False

            if is_correct_seq:
                return int(numbers[len(numbers) // 2]) if has_swapped else 0

    for rule in rules.splitlines():
        left, right = rule.split("|")
        rules_map[right].add(left)
    for s in seqs.splitlines():
        numbers = s.split(",")
        numbers.reverse()
        result += resolve_numbers(numbers)
    return result

import re


def pt1(_input):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, _input)
    result = 0
    for m in matches:
        match = re.match(r"^mul\((\d+),(\d+)\)$", m)
        result += int(match.group(1)) * int(match.group(2))
    return result


def pt2(_input: str) -> int:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    is_enabled = True
    result = 0

    for token in re.split(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", _input):
        token = token.strip()
        if token == "do()":
            is_enabled = True
        elif token == "don't()":
            is_enabled = False
        elif is_enabled:
            match = re.match(pattern, token)
            if match:
                result += int(match.group(1)) * int(match.group(2))
    return result

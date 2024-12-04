def pt1(_input: str):
    matrix = [list(row) for row in _input.splitlines()]
    len_rows, len_cols = len(matrix), len(matrix[0])
    target = "XMAS"
    result = 0

    def is_correct_seq(row: int, col: int, r_move: int, c_move: int):
        for i in range(len(target)):
            target_row = row + (r_move * i)
            target_col = col + (c_move * i)
            is_valid_target = 0 <= target_row < len_rows and 0 <= target_col < len_cols
            try:
                if not is_valid_target or matrix[target_row][target_col] != target[i]:
                    return False
            except IndexError:
                return False
        return True

    for r in range(len_rows):
        for c in range(len_cols):
            if matrix[r][c] != target[0]:
                continue
            directions = [
                (0, 1),  # matrix[r][c + x] right
                (0, -1),  # matrix[r][c - x] left
                (-1, 0),  # matrix[r - x][c] up
                (1, 0),  # matrix[r + x][c] down
                (-1, 1),  # matrix[r - x][c + x] up right
                (-1, -1),  # matrix[r - x][c - x] up left
                (1, 1),  # matrix[r + x][c + x] down right
                (1, -1),  # matrix[r + x][c - x] down left
            ]
            for r_move, c_move in directions:
                if is_correct_seq(r, c, r_move, c_move):
                    result += 1
    return result


def pt2(_input: str):
    matrix = [list(row) for row in _input.splitlines()]
    len_rows, len_cols = len(matrix), len(matrix[0])
    patterns = [
        ["M", "A", "S", "M", "S"],
        ["M", "A", "S", "S", "M"],
        ["S", "A", "M", "M", "S"],
        ["S", "A", "M", "S", "M"],
    ]
    result = 0
    for r in range(len_rows):
        for c in range(len_cols):
            for p in patterns:
                try:
                    if (
                        matrix[r][c] == p[0]
                        and matrix[r + 1][c + 1] == p[1]
                        and matrix[r + 2][c + 2] == p[2]
                        and matrix[r + 2][c] == p[3]
                        and matrix[r][c + 2] == p[4]
                    ):
                        result += 1
                except IndexError:
                    continue
    return result

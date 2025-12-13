import pytest
from day01_01 import split_input
from day01_02 import how_many_crosses


@pytest.mark.parametrize("input,expected", [("R1", ["R", 1]), ("L23", ["L", 23])])
def test_split_input(input, expected):
    assert split_input(input) == expected


# def new_pos_and_how_many_zeroes(position, direction, number):
#     if direction == "R":
#         new_position = position + number

#         # position = new_position % 100

#         quotient, remainder = divmod(new_position, 100)
#         return (remainder, quotient)
#     else:
#         new_position = position - number  # -95
#         quotient, remainder = divmod(new_position, 100)  # -1, 5
#         # quotient2, remainder2 = divmod(abs(new_position), 100)  # 0, 95
#         return (abs(remainder), abs(quotient))

#         # position = new_position % 100  # 96

#         # beyond = number - position  # 104
#         # crosses = 0
#         # if beyond > 0:
#         #     crosses = abs(beyond // 100) + 1

#         # if position == 0:
#         #     crosses = crosses + 1

#         # # quotient = abs(new_position) // 100  # nope
#         # # remainder = new_position % 100
#         # return (position, crosses)

# @pytest.mark.parametrize(
#     "position, direction, number, new_position, zeros",
#     [
#         (0, "R", 100, 0, 1),
#         (30, "R", 70, 0, 1),
#         (30, "R", 170, 0, 2),
#         (5, "R", 3, 8, 0),
#         (5, "R", 94, 99, 0),
#         (5, "R", 95, 0, 1),
#         (5, "R", 96, 1, 1),
#         (5, "R", 900, 5, 9),
#         (5, "R", 999, 4, 10),
#         (99, "R", 102, 1, 2),
#         (98, "R", 300, 98, 3),
#         (0, "L", 100, 0, 1),
#         (0, "L", 95, 5, 0),
#         # (40, "L", 40, 0, 1),  # fails, but my answer is too high
#         (5, "L", 3, 2, 0),
#         (5, "L", 8, 97, 1),
#         (5, "L", 109, 96, 2),
#         (5, "L", 300, 5, 3),
#         (5, "L", 306, 99, 4),
#         (5, "L", 900, 5, 9),
#         (5, "L", 999, 6, 10),
#     ],
# )
# def test_calc(position, direction, number, new_position, zeros):
#     assert new_pos_and_how_many_zeroes(position, direction, number) == (
#         new_position,
#         zeros,
#     )


@pytest.mark.parametrize(
    "position, direction, number, new_position, zeros",
    [
        (50, "L", 68, 82, 1),
        (82, "L", 30, 52, 0),
        (52, "R", 48, 0, 0),  # problem
        (0, "L", 5, 95, 0),
        (95, "R", 60, 55, 1),
        (55, "L", 55, 0, 0),
        (0, "L", 1, 99, 0),
        (99, "L", 99, 0, 0),
        (0, "R", 14, 14, 0),
        (14, "L", 82, 32, 1),
        (0, "R", 100, 0, 0),
        (30, "R", 70, 0, 0),
        (30, "R", 170, 0, 1),
        (5, "R", 3, 8, 0),
        (5, "R", 94, 99, 0),
        (5, "R", 95, 0, 0),
        (5, "R", 96, 1, 1),
        (5, "R", 900, 5, 9),
        (5, "R", 999, 4, 10),
        (99, "R", 102, 1, 2),
        (98, "R", 300, 98, 3),
        (0, "L", 100, 0, 0),
        (0, "L", 95, 5, 0),
        (40, "L", 40, 0, 0),
        (5, "L", 3, 2, 0),
        (5, "L", 8, 97, 1),
        (5, "L", 109, 96, 2),
        (5, "L", 300, 5, 3),
        (5, "L", 306, 99, 4),
        (5, "L", 900, 5, 9),
        (5, "L", 999, 6, 10),
    ],
)
def test_calc_attempt_two(position, direction, number, new_position, zeros):
    assert how_many_crosses(position, direction, number) == zeros

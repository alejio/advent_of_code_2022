from day9.day9 import load_data, main_part_1, main_part_2


def test_main_part_1():
    movements = load_data("test_part_1")
    output = main_part_1(movements)
    assert output == 13


def test_main_part_2():
    movements = load_data("test_part_2")
    output = main_part_2(movements)
    assert output == 36
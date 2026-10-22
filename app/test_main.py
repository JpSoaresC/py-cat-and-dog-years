from app.main import get_human_age

# write your code here
def test_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_under_fifteen_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_fifteen_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_twenty_four_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_high_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]

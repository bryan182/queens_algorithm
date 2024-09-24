import pytest
from database import solutions_count, insert_boards
from unittest.mock import patch
from queens import main



@pytest.mark.parametrize(
    "size_board, res",
    [   
        (1, 1),
        (2, 0),
        (3, 0),
        (4, 2),
        (5, 10),
        (6, 4),
        (7, 40),
        (8, 92)
    ]
)
def test_queen_n(size_board, res, monkeypatch):
    for number in range(1,9):
        monkeypatch.setattr('builtins.input', lambda _: number)
        main()
    assert solutions_count(size_board) == res



import pytest
from exercises.ascii_puzzle_tiles import puzzle_tiles


RESULT_4_3: str = """
   _( )__ _( )__ _( )__ _( )__
 _|     _|     _|     _|     _|
(_   _ (_   _ (_   _ (_   _ (_
 |__( )_|__( )_|__( )_|__( )_|
 |_     |_     |_     |_     |_
  _) _   _) _   _) _   _) _   _)
 |__( )_|__( )_|__( )_|__( )_|
 _|     _|     _|     _|     _|
(_   _ (_   _ (_   _ (_   _ (_
 |__( )_|__( )_|__( )_|__( )_|
"""


def test_puzzle_tiles():
    assert "\n" + puzzle_tiles(4, 3) + "\n" == RESULT_4_3


def test_puzzle_tiles_bad_input():
    with pytest.raises(AssertionError):
        puzzle_tiles(0, 1)

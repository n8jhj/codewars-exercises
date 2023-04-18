"""For drawing ASCII puzzle tiles."""


def puzzle_tiles(width: int, height: int) -> str:
    """Prints puzzle tiles to stdout.

    Args:
        width: Number of tiles to print horizontally.
        height: Number of tiles to print vertically.

    Returns:
        String representation of puzzle tiles.

    Raises:
        AssertionError: Width or height given with value < 1
    """
    assert width > 0 and height > 0, "Width or height given with value < 1"

    def f():
        yield "  " + " _( )__" * width
        for i in range(height):
            if i % 2 == 0:
                yield " _|" + "     _|" * width
                yield "(_" + "   _ (_" * width
            else:
                yield " |_" + "     |_" * width
                yield "  _)" + " _   _)" * width
            yield " |" + "__( )_|" * width

    return "\n".join(f())


if __name__ == "__main__":
    print(puzzle_tiles(4, 3))

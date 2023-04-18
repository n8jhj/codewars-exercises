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
    lines: list[str] = []
    lines.append("  " + " _( )__" * width)
    for i in range(height):
        if i % 2 == 0:
            lines.append(" _|" + "     _|" * width)
            lines.append("(_" + "   _ (_" * width)
        else:
            lines.append(" |_" + "     |_" * width)
            lines.append("  _)" + " _   _)" * width)
        lines.append(" |" + "__( )_|" * width)
    return "\n".join(lines)


if __name__ == "__main__":
    print(puzzle_tiles(4, 3))

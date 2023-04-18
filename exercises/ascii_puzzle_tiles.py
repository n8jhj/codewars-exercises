"""For drawing ASCII puzzle tiles."""


def puzzle_tiles(width: int, height: int) -> str:
    assert width > 0 and height > 0, "Both width and height must be > 1"
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

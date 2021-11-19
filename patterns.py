def block(size_x: int, size_y: int, block_char: str):
    for i in range(size_y):
        for j in range(size_x):
            print(block_char[0] + " ", end="")

        print()


def triangle(height, triangle_char: str, upside_down=False):
    if not upside_down:
        for i in range(height):
            print((triangle_char[0] + " ") * (i + 1), end="")

            print()

    else:
        for i in range(height):
            print((triangle_char[0] + " ") * (height - i), end="")

            print()

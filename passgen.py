import random


def generate(start_chars: str, length: int, upper: bool, lower: bool, sym: bool, num: bool) -> str:
    password = start_chars

    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
    lowercase = [i.lower() for i in uppercase]
    symbols = ["/", "#", "$", "%", "(", ")", "[", "]", "{", "}", ",", "\"", "'", "/", "\\", "=", "*"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    chosen_chars = []
    if upper:
        chosen_chars.extend(uppercase)
    if lower:
        chosen_chars.extend(lowercase)
    if sym:
        chosen_chars.extend(symbols)
    if num:
        chosen_chars.extend(numbers)

    for _ in range(1, length):
        password += str(random.choice(chosen_chars))

    return password

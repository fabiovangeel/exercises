def countX(text):
    if not text:
        return 0

    first_x = 1 if text[0] == "x" else 0

    return first_x + countX(text[1:])

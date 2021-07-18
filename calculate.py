def add(a: int, b: int):
    result = a + b
    return result

def substraction(a: int, b: int):
    result = a - b
    if result >= 0:
        return result
    else:
        return 0
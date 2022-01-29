def transform_string(number: int) -> str:

    if n % 100 in (11, 12, 13, 14) or n % 10 in (5, 6, 7, 8, 9, 0):
        return f"{n} программистов"
    elif n % 10 in (2, 3, 4):
        return f"{n} программиста"
    else:
        return f"{n} программист"

for n in range(1, 101):
    print(transform_string(n))


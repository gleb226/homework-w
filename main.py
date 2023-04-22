result = []
def divider(a, b):
    if b == 0:
        raise ZeroDivisionError
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b

data = {10: 2, 2: 5, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ZeroDivisionError, ValueError, IndexError) as e:
        print("Виняток типу:", type(e).__name__)

print(result)
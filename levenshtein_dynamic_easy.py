
def levenshtein(a, b):
    n, m = len(a), len(b)

    current_row = range(n + 1)  # Будем хранить только текущий и предыдущий ряд, а не всю матрицу
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


print(levenshtein('qwe', 'awe'))

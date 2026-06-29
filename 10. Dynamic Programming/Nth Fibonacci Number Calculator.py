def fibonacci(n):
    if n < 0:
        return "Enter a non negative integer"
    if n == 0:
        return 0

    sequence = [0, 1]
    for i in range(n-1):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[-1]

print(fibonacci(15))
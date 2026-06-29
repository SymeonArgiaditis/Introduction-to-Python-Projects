def hanoi_solver(n) -> str:
    rod1 = list(range(n, 0, -1))
    rod2 = []
    rod3 = []
    moves = [f"{rod1} {rod2} {rod3}"] 

    def hanoi(n, source, target, helper):
        if n == 1:
            target.append(source.pop())
            moves.append(f"{rod1} {rod2} {rod3}")
            return

        hanoi(n-1, source, helper, target)

        target.append(source.pop())
        moves.append(f"{rod1} {rod2} {rod3}")

        hanoi(n-1, helper, target, source)

    hanoi(n, rod1, rod3, rod2)
    return "\n".join(moves)

print(hanoi_solver(2))
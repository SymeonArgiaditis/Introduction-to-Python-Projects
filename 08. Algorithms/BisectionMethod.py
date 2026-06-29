def square_root_bisection(number, tolerance = 0.01, maximum = 100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    
    lower_bound = 0
    upper_bound = max(1, number)

    iter = 1
    while abs(lower_bound - upper_bound) > tolerance and iter <= maximum:
        mid = (lower_bound + upper_bound) / 2
        if mid**2 == number:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        elif mid**2 < number:
            lower_bound = mid
        else:
            upper_bound = mid
        iter += 1

    if abs(lower_bound - upper_bound) <= tolerance:
            root = (lower_bound + upper_bound) / 2
            print(f"The square root of {number} is approximately {root}")
            return root
    else:
        print(f"Failed to converge within {maximum} iterations")
        return None


square_root_bisection(0.001, 1e-7, 50)
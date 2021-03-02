def persistence(n):
    import numpy as np

    # get values of number to list
    digits = [num for num in str(n)]
    count = 0

    while len(digits) > 1:
        # convert to int
        digits = list(map(int, digits))
        # cumprod and get final output
        ans = np.cumprod(digits)[-1]
        digits = [num for num in str(ans)]

        count += 1
    return count


print(persistence(999))
print(persistence(4))
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        prod = 1
        i = 1
        while i <= n:
            prod = prod * i
            i = i + 1
        return prod

def dec2fac(dec_num: int, n: int) -> list:
    # Transform a decimal number into an n-digit factorial base number.
    fac_num = [0] * n 
    q, r, i = dec_num, 0, 1
    while q > 0:
        q, r = q // i, q % i
        # fac_num = fac_num + [r]
        fac_num[i-1] = r
        i = i + 1
    return fac_num

def fac2dec(fac_num: list, n: int) -> list:
    # Transform an n-digit number in factorial base into a decimal number.
    dec_num = 0
    prod = 1
    i = 1 # The first element in fac_num is always 0, so we begin with i = 1.
    while i < n:
        dec_num = dec_num + fac_num[i] * prod
        print(f'dec_num = {dec_num}')
        prod = (prod + 1) * prod
        i = i + 1
    return dec_num

n = 4
myfac_num = [0, 1, 2, 3]
dec_num = fac2dec(myfac_num, n)
print(dec_num)
# +------------+-------------------------------+
# | File       | 24w_cmbAlg_assig01_group03.py |
# +------------+-------------------------------+
# | Group      |              03               |
# +------------+-------------------------------+
# | Assignment |              01               |
# +------------+-------------------------------+
# | Member 01  | Name: Mingshan, LI            |
# |            | ID:   999014681               |
# +------------+-------------------------------+
# | Member 02  | Name: Shunxi, XIAO            |
# |            | ID:   999014772               |
# +------------+-------------------------------+
# | Member 03  | Name: Weizhi, LU              |
# |            | ID:   999022064               |
# +------------+-------------------------------+

import sys
filename = '24w_cmbAlg_assig01_group03.py'
if len(sys.argv) != 2:
    print('Usage: python3', filename, 'N')
    sys.exit(1)


print('+------------+-------------------------------+')
print('| File       | 24w_cmbAlg_assig01_group03.py |')
print('+------------+-------------------------------+')
print('| Group      |              03               |')
print('+------------+-------------------------------+')
print('| Assignment |              01               |')
print('+------------+-------------------------------+')
print('| Member 01  | Name: Mingshan, LI            |')
print('|            | ID:   999014681               |')
print('+------------+-------------------------------+')
print('| Member 02  | Name: Shunxi, XIAO            |')
print('|            | ID:   999014772               |')
print('+------------+-------------------------------+')
print('| Member 03  | Name: Weizhi, LU              |')
print('|            | ID:   999022064               |')
print('+------------+-------------------------------+')
print('\n')

# +-------------------------------------------+
# |                Question 1                 |
# +-------------------------------------------+
print('+-------------------------------------------+')
print('|                Question 1                 |')
print('+-------------------------------------------+', end = '\n\n')

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
    '''
    Transform a decimal number into an n-digit factorial base number.
    '''
    fac_num = [0] * n 
    q, r, i = dec_num, 0, 1
    while q > 0:
        q, r = q // i, q % i
        fac_num[i-1] = r
        i = i + 1
    fac_num.reverse() # adapt to the way base-factorial number is represented
    return fac_num


def fac2dec(fac_num_: list, n: int) -> list:
    '''
    Transform an n-digit number in factorial base into a decimal number.
    '''
    fac_num = fac_num_[:] # we do not want to change arg. fac_num_
    fac_num.reverse()     # adapt to the way base-factorial number is represented
    dec_num = 0
    prod = 1
    i = 1 # The first element in fac_num is always 0, so we begin with i = 1.
    while i < n:
        dec_num = dec_num + fac_num[i] * prod
        prod = (prod + 1) * prod
        i = i + 1
    return dec_num


def permu2lehmer(permu: list) -> list:
    '''
    Transform a permutaiton into its lehmer code.
    '''
    n = len(permu)
    lehmer = [0] * n
    for i in range(n):
        curr = 0
        for j in range(i, n):
            if permu[j] < permu[i]:
                curr += 1
        lehmer[i] = curr
    return lehmer


def lehmer2permu(lehmer: list) -> list:
    '''
    Transform a lehmer code into the corresponding permtation.
    '''
    n = len(lehmer)
    num_list = [i for i in range(n)] # [0, 1, 2, ... , n-2, n-1]
    permu = [0] * n
    for i in range(n):
        curr = lehmer[i]
        permu[i] = num_list[curr]
        # eliminate the curr-th element from the num_list.
        if curr == 0:
            num_list = num_list[curr+1:]
        elif curr == n-1:
            num_list = num_list[:curr]
        else:
            num_list = num_list[:curr] + num_list[curr+1:]
    return permu


def permu_lex_rank(permu: list, n: int) -> int:
    '''
    Ranking algorithm of permutation over n in lexicographic order.
    '''
    r_fac = permu2lehmer(permu)  # rank in base factorial
    r_dec = fac2dec(r_fac, n)    # rank in base decimal
    return r_dec


def permu_lex_unrank(r_dec: int, n: int) -> list:
    '''
    Unranking algorithm of permutation over n in lexicographic order.
    '''
    r_fac = dec2fac(r_dec, n)   # rank in base factorial
    permu = lehmer2permu(r_fac) # permutation
    return permu


def permu_lex_successor(permu_: list):
    permu = permu_[:] # we do not want to change arg. permu_
    n = len(permu)
    '''
    Step 1: Find the largest i such that 𝜋[i] < 𝜋[i+1].
    '''
    i = -1
    k = 0
    while k < n - 1:
        if permu[k] < permu[k+1]:
            i = k
        k = k + 1
    if i == -1: # such i D.N.E., that is, permu is the last permutation
        return [x for x in range(n)] 
    '''
    Step 2: Find the largest j such that 𝜋[j] > 𝜋[i].
    '''    
    j = i + 1
    l = i + 1
    while l < n:
        if permu[l] > permu[i]:
            j = l
        l = l + 1
    '''
    Step 3: Swap 𝜋[i] and 𝜋[j]
    '''
    temp = permu[i]
    permu[i] = permu[j]
    permu[j] = temp
    '''
    Step 4: 
    '''
    sublist = permu[i+1:]
    sublist.reverse()
    succ_permu = permu[:i+1] + sublist
    return succ_permu

# Excecuteing:

N = int(sys.argv[1])
N_fac = factorial(N)
for i in range(N_fac):
    permu = permu_lex_unrank(i, N)
    rank = permu_lex_rank(permu, N)
    next_permu = permu_lex_successor(permu)
    if next_permu == permu_lex_unrank( (permu_lex_rank(permu, N) + 1) %  N_fac, N ):
        checking = True
    else:
        checking = False
    print(f'rank( {permu} ) = {rank:3} ,  successor( {permu} ) = {next_permu} , check: {checking}')

print('\n\n')


# +-------------------------------------------+
# |                Question 2                 |
# +-------------------------------------------+
print('+-------------------------------------------+')
print('|                Question 2                 |')
print('+-------------------------------------------+', end = '\n\n')

def permu_trotterJohnson(n: int) -> list:

    '''
    Return all the permutations of {1, 2, ..., n}.
    '''

    curr_T = []
    if n == 1:
        curr_T = [[1]]
    else:
        prev_T = permu_trotterJohnson(n-1)
        for l in prev_T:
            i = 0
            while i < n:
                curr_T.append(l)
                i = i + 1
        n_fac = factorial(n)
        for i in range(n_fac):
            k = i % n + 1
            b = ( i // n ) % 2        
            t = abs( (1-b) * n - (k-b) )
            curr_T[i] = curr_T[i][:t] + [n] + curr_T[i][t:]
    return curr_T


def epsilon(r: int, n: int, k: int) -> int:

    '''
    Implementation of the calculation of epsilon.
    
    Arguments:

    r: rank(𝜋', n-1)
    n: the size of the permutation permu_
    k: the position in permu_ such that permu[k] = n
    '''

    if r % 2 == 0:
        return n - k
    else:
        return k - 1


def permu_colexi_rank(permu: list, n: int) -> int:
    
    '''
    The implementation of ranking alogorithmn of permutation over [n] = {1, 2, ..., n}    
    '''

    if n == 0:

        return 0

    else :

        k = permu.index(n)
        prev_r = permu_colexi_rank( permu[:k] + permu[k+1:], n - 1 )
        e = epsilon(prev_r, n, k+1) # k is obtained from python, which begins from 0.
        return n * prev_r + e



def pos_k(r: int, e: int, n: int) -> int:

    '''
    Implementation of calculation of the position k, such that 𝜋[k] = n
    '''

    if r % 2 == 0:
        return n - e
    else:
        return e + 1


def permu_colexi_unrank(r: int, n: int) -> int:

    '''
    The implementation of unranking alogorithmn of permutation over [n] = {1, 2, ..., n}    
    '''

    if n == 1:

        return [1]

    else:

        prev_r = r // n
        e = r - n * prev_r
        k = pos_k(prev_r, e, n) - 1 # k is position in python list, which begins from 0.
        prev_permu = permu_colexi_unrank(prev_r, n-1)

        return prev_permu[:k] + [n] + prev_permu[k:]


def Parity(n, P):
    """
    Calculate the parity of a permutation.
    """
    a = [0] * n  # Array to track visited elements.
    c = 0  # Counter for the number of cycles.

    # Iterate through each element in the permutation.
    for j in range(n):
        if a[j] == 0:  # If this element is not visited yet.
            c += 1  # Increment the cycle count.
            a[j] = 1  # Mark it as visited.
            i = j

            # Traverse the cycle starting from this element.
            while(P[i] != j + 1):  # Continue until the cycle closes.
                i = P[i] - 1  # Move to the next element in the cycle.
                a[i] = 1  # Mark the element as visited.
    
    # Return the parity of the permutation.
    return (n - c) % 2

def permu_colexi_successor(n, P):
    """
    Compute the next permutation in using a modified version of the Trotter-Johnson algorithm.
    """
    st = 0  # Starting index for the permutation.
    Q = P[:]  # Copy of the permutation to be used in calculations.
    done = False  # Flag to indicate if the next permutation is found.
    m = n  # Length of the current sub-permutation being considered.

    while((m > 1) and (not done)):
        d = 0  # Find the position of the largest element in the current range.
        while(Q[d] != m):  # Locate the position of 'm' in Q.
            d += 1
        
        # Temporarily remove m from Q by shifting elements to the left.
        for i in range(d, m - 1):
            Q[i] = Q[i + 1]
        
        # Check the parity of the resulting permutation.
        par = Parity(m - 1, Q)

        # Determine whether to swap or reduce m
        if(par == 1):  # Odd parity case.
            if d == m - 1:  # If 'm' is at the last position, reduce the size of the range.
                m -= 1
            else:  # Otherwise, swap 'm' with the next element to its right.
                temp = P[st + d]
                P[st + d] = P[st + d + 1]
                P[st + d + 1] = temp
                done = True  # Mark the next permutation as found.
        else:  # Even parity case.
            if(d == 0):  # If 'm' is at the first position, reduce the size of the range.
                m -= 1
                st += 1  # Update the starting index.
            else:  # Otherwise, swap 'm' with the previous element.
                temp = P[st + d]
                P[st + d] = P[st + d - 1]
                P[st + d - 1] = temp
                done = True  # Mark the next permutation as found.

        # Restore Q to its original state for the next iteration.
        Q = P[st:st + m]

    if m == 1 and not done:
        # return 'undefined'
        return [x+1 for x in range(n)]  # The input permutation is the last in lexicographic order.
    else:
        return P  # Return the next permutation.

# Excecute:

print('RERM(N):')
all_permus = permu_trotterJohnson(N)
for permu in all_permus:
    print(permu)

print('\n\n')

for r in range(N_fac):
    curr_permu = permu_colexi_unrank(r, N)
    curr_rank = permu_colexi_rank(curr_permu, N)
    next_permu = permu_colexi_successor(N, curr_permu[:])

    if next_permu == permu_colexi_unrank( (permu_colexi_rank(curr_permu, N) + 1) %  N_fac, N ):
        flag = True
    else:
        flag = False
    
    print(f'rank( {curr_permu} ) = {curr_rank:3} ,  successor( {curr_permu} ) = {next_permu} , check: {flag}') 


print('\n\n')
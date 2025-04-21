
def nSet(n):#Generate a n-set
    s = list(range(1, n + 1))
    return s

def SubsetRank(n, T):#Ranking algorithm
    r = 0
    for i in range(1, n + 1):
        r *= 2
        if i in T:
            r += 1
    return r

def SubsetUnrank(n, r):#Unranking algorithm
    T = []
    for i in range(n, 0, -1):
        if r % 2 == 1:
            T.insert(0, i)
        r //= 2
    return T

def Successor(n, T):#Successor algorithm
    i = 0
    while i <= n - 1 and n - i in T:
        T.remove(n - i)
        i += 1
    if i <= n - 1:
        T.append(n - i)
    return T

def Cardinality(S):#Check the cardinality of a set S
    return len(S)

'''def Lexicographic(S):
    return sorted(S, key=lambda x: (len(x), x)) '''

def Collection(n):#Generate all subsets of n_set using successor algorithm
    subsets = []
    subset = nSet(n)
    for i in range(pow(2, n)):
        subset = Successor(n, subset) 
        subsets.append(subset.copy())
    return subsets

S = Collection(6)#Generate a lexicographic order collection of subsets of n_set
print ("the set is " + str(S))
for i in range(Cardinality(S)):
    r = SubsetRank(6, S[i])#front variable is n
    ur = SubsetUnrank(6, i)#front variable is n
    print("The rank of "+ str(S[i])+ " is " + str(r) + " the unrank of " + str(i) + " is " + str(ur) )

'''
To use this program, all you need to do is to change the variable 'n' on line 45, 48 and line 49
into the number you want. For instance, n = 3, 4, 5, etc.
'''
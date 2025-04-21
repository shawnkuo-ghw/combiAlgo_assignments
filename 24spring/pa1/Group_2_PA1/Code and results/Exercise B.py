import math

#The 2-color-n-set consists of following things. If we choose1 to represent a color, and choose 0 to represent the other one.
#Then the string that represents every element in a permutation is actually a binary string.
class color_permutation:
    def __init__(cp, numberofcolor, size):
        cp.numberofcolor = numberofcolor
        cp.size = size
        cp.permutation = []
        cp.color = []

#This function turns a binary string into an integer.
def decoder_color(cp):
    number = 0
    for i in range(cp.size - 1, -1, -1):
        if (cp.color[i] == 1):
            number += pow(cp.numberofcolor, cp.size - i - 1) #Since biggest position of the list is the smallest digit of binary string, we need to reverse it.
    return number

#This function turns an integer into a binary string.
#Take an integer, divide it by 2, you will get a quotient and a remainder. The remainder is the number of the biggest digit of binary string. Divide the quotient by 2, and get another remainder.
#Keep this process until len(cp.color) times.
def encoder_color(cp, n):
    remainder = n
    for i in range(cp.size - 1, -1, -1):
        cp.color[i] = remainder % cp.numberofcolor
        remainder = remainder // cp.numberofcolor
    return cp.color

 
def rank(cp):
    count1 = 0
    set1 = set() #Set of used elements.
    for i in range(cp.size):
        for j in range(1, cp.permutation[i]):
            if (j not in set1):
               count1 += math.factorial(cp.size - i - 1)
        set1.add(cp.permutation[i])  #Since ith element is fixed, we need to collect it into the set of used element.
    count2 = decoder_color(cp)
    return count1*pow(cp.numberofcolor, cp.size) + count2 + 1 #count1 * 2^n + count2 is the number of permutations precede cp, the rank need to be added 1 extraly

def unrank(n,m):
    cp = color_permutation(2, m)
    for i in range(m):
        cp.permutation.append(0)
        cp.color.append(0)
    list = [] #An increasing sequence, from 1 to n, represents elemernts haven't been used.
    for i in range(cp.size):
        list.append(i + 1)
    rank = math.ceil(n / pow(cp.numberofcolor, cp.size))
    cp.color = encoder_color(cp, n % pow(cp.numberofcolor, cp.size) - 1)
    for i in range(cp.size - 1):
        if (rank == 0):
            for j in range(i , cp.size - 1):
                cp.permutation[j] = list[len(list) + i - j - 1]
            break
        element = math.ceil(rank / math.factorial(cp.size - i - 1)) #Element is the quotient r of current rank \ (k - i)!, and element must be unused. 
        cp.permutation[i] = list[element - 1] #In other words, element is the rth smallest element in list.
        del list[element - 1] #When we have used element, we need to delete it from sequence and keep the order of sequence.
        rank = rank % math.factorial(cp.size - i - 1) 
    cp.permutation[cp.size - 1] = list[0] #Since after fixing (n - 1)th element, we know the last element, we just need to iterate from 0 to n - 2.
    return cp

def successor(cp):
    carry = 0 #Carry means if the current cp have the greatest color. If so, we need to find successor permutation after finding successor of color.
    if (cp.color[cp.size - 1] == 0):
        cp.color[cp.size - 1] = 1
    else:
        for i in range(cp.size - 1, -1, -1):
            if (cp.color[i] == 1):
                cp.color[i] = 0
                if (i == 0):
                    carry = 1
            else:
                cp.color[i] = 1
                break
    
    if (carry == 1):
        l = 0
        for i in range(cp.size - 1, -1, -1):
            if (cp.permutation[i - 1] < cp.permutation[i]):
                l = i
                x = len(cp.permutation) - 1
                while (cp.permutation[i - 1] > cp.permutation[x] and x >= 0):
                    x -= 1
                if (x == 0):
                    break
                cp.permutation[i - 1], cp.permutation[x] = cp.permutation[x], cp.permutation[i - 1]
                break
        for j in range(l, l + math.ceil((cp.size - l)/2)):
            cp.permutation[j], cp.permutation[cp.size - 1 - (j - l)] = cp.permutation[cp.size - 1 - (j - l)], cp.permutation[j]
    return cp 

def print_color_permutation(cp):
    print('[',end = "")
    for i in range(cp.size):
        if (cp.color[i] == 1):
            print('\033[0;31m' + str(cp.permutation[i]) + '\033[0m',end = "") #If the bit is 1, print red character.
        else:
            print('\033[0;34m' + str(cp.permutation[i]) + '\033[0m',end = "") #If the bit is 0, print blue character.
    print('] ',end = "")

def list_color_permutation(n):
    x = color_permutation(2, n)
    for p1 in range(n):
        x.permutation.append(p1 + 1)
    for p2 in range(n):
        x.color.append(0)
    for i in range(math.factorial(n)*pow(x.numberofcolor, x.size)):
        print_color_permutation(x)
        x = successor(x)
    


#Start from here:

x1 = color_permutation(2, 4)
x1.permutation = [2, 1, 3, 4]
x1.color = [1, 0, 1, 1]
print('The rank of ',end = "")
print_color_permutation(x1)
print(' is :' + str(rank(x1)) + ' \n')

y1 = color_permutation(2, 5)
y1.permutation = [2, 5, 3, 4, 1]
y1.color = [1, 0, 1, 0, 1]
print('The rank of ',end = "")
print_color_permutation(y1)
print(' is :' + str(rank(y1)) + ' \n')

z1 = color_permutation(2, 6)
z1.permutation = [6, 1, 2, 3, 5, 4]
z1.color = [1, 0, 0, 1, 0, 1]
print('The rank of ',end = "")

print_color_permutation(z1)
print(' is :' + str(rank(z1)) + ' \n')

print('The unrank is : ',end="" )
print_color_permutation(unrank(60, 4))
print('\n')

print('The unrank is : ',end="" )
print_color_permutation(unrank(60, 5))
print('\n')

print('The unrank is : ',end="" )
print_color_permutation(unrank(60, 6))
print('\n')

x2 = color_permutation(2, 4)
x2.permutation = [3, 1, 2, 4]
x2.color = [0, 1, 0, 1]
print('The sucessor of ',end = "")
print_color_permutation(x2)
print(' is ')
print_color_permutation(successor(x2))
print('\n')

y2 = color_permutation(2, 5)
y2.permutation = [3, 5, 1, 4, 2]
y2.color = [0, 0, 1, 1, 1]
print('The sucessor of ',end = "")
print_color_permutation(y2)
print(' is ')
print_color_permutation(successor(y2))
print('\n')

z2 = color_permutation(2, 6)
z2.permutation = [6, 5, 4, 3, 1, 2]
z2.color = [1, 1, 0, 0, 1, 1]
print('The sucessor of ',end = "")
print_color_permutation(z2)
print(' is ')
print_color_permutation(successor(z2))
print('\n')

print('The list of 2-color-4-set is :\n')
list_color_permutation(4)

# FILE: genBST.py

from BST import *

#global_L = [-3, -2, 0, 2]
global_L = [1, 2, 5, 7, 8, 9]
#global_L = [-100, -50, -25, -5, 5, 25, 50, 100]
global_length = len(global_L)
global_bst = BST()

global_count = [0]

def GENERATE_BST_(keyList, CurrKey, VistedList, l): 
    global_bst.insert(CurrKey)
    
    # 1. Check Feasibility of the current BST
    if l == global_length:
        print("Input List =", VistedList+[CurrKey])
        global_bst.print_BST()
        global_count[0] += 1
    
    # 2. Construct the choice list for the current key
    Choice_List = list(global_L)
    Choice_List.remove(CurrKey)
    for key in VistedList:
        Choice_List.remove(key)
    
    # 3. Call the algorithm recursively and assign every key in choice list to CurrKey
    for nextKey in Choice_List:
        GENERATE_BST_(global_L, nextKey, VistedList + [CurrKey], l+1)
    
    global_bst.remove_leaf(CurrKey)

def GENERATE_BST(global_L):
    for key in global_L:
        GENERATE_BST_(global_L, key, [], 1)


def main():
    GENERATE_BST(global_L)
    print("Total Number:", global_count[0])


if __name__ == "__main__":
    main()
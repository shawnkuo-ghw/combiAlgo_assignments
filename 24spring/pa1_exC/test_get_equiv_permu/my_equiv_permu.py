# FILE: my_equiv_permu.py

from BST import *

def print_nodes_list(nodes_list: list) -> None:
    N = len(nodes_list)
    print("[", end="")
    for i in range(N):
        if i == N - 1:
            print(nodes_list[i].key, sep="", end="")
        else:
            print(nodes_list[i].key, ", ", sep="", end="")
    print("]")

def get_children(node: Node) -> list:
    children = []
    if node.left is not None:
        children.append(node.left)
    if node.right is not None:
        children.append(node.right)
    return children

def get_equiv_permutations_(equiv_list, CurrNode, Visited_List, Prev_Choice_List):
    
    print("Prev_Choice List:", end=" ")
    print_nodes_list(Prev_Choice_List)
    print("    Visited List:", Visited_List)
    if CurrNode != None:
        print("         CurrKey:", CurrNode.key)

    # 1. Check feasibility
    if len(Prev_Choice_List) == 0:
        equiv_list.append(Visited_List)
        print("\n")
        return
    
    # 2. Construct choice list
    Choice_List = []
    if CurrNode != None:
        Choice_List.extend(get_children(CurrNode))    
        Choice_List.extend(Prev_Choice_List)
        Choice_List.remove(CurrNode)
        print("       Next List:", end=" ")
        print_nodes_list(Choice_List)
        print("\n")

    # 3. Call the function recursively
    if len(Choice_List) != 0:
        for nextNode in Choice_List:
            get_equiv_permutations_(equiv_list, nextNode, Visited_List + [CurrNode.key], Choice_List)
    else:
        get_equiv_permutations_(equiv_list, None, Visited_List + [CurrNode.key], [])

def get_equiv_permutations(bst: BST) -> list:
    equiv_list = []
    get_equiv_permutations_(equiv_list, bst.root, [], [bst.root])
    return equiv_list

def main():
    mybst = BST()
    L = [4, 2, 1, 3, 5]
    for i in L:
        mybst.insert(i)

    mybst.print_BST()

    equiv_list = get_equiv_permutations(mybst)

    print("\nEquivalent Input List:")
    for list in equiv_list:
        print(list)

if __name__ == "__main__":
    main()
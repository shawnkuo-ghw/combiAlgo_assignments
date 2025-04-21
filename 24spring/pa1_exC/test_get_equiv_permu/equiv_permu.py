# FILE: equiv_permu.py

from BST import *

def get_children(node: Node) -> list:
    children = []
    if node.left is not None:
        children.append(node.left)
    if node.right is not None:
        children.append(node.right)
    return children

def print_nodes_list(nodes_list: list) -> None:
    N = len(nodes_list)
    print("[", end="")
    for i in range(N):
        if i == N - 1:
            print(nodes_list[i].key, sep="", end="")
        else:
            print(nodes_list[i].key, ", ", sep="", end="")
    print("]\n")

def equiv_permutations(children_list: list, visited_list: list, equiv_list: list):

    print("visited  list:", visited_list)
    print("children list:", end=" ")
    print_nodes_list(children_list)

    # 1. Check feasibility of the current visited list
    if len(children_list) == 0:
        print("get one equivalent list!", end="\n\n")
        equiv_list.append(visited_list)
        return
    for i in range(len(children_list)):
        node = children_list[i]
        del children_list[i]          # delete the i-th children
        new_children_list = get_children(node) + children_list 
        equiv_permutations(new_children_list, visited_list+[node.key],  equiv_list)
        children_list.insert(i, node) # recover the children list

def get_equiv_permutations(bst: BST) -> list:
    equiv_list = []
    root_children = get_children(bst.root)
    
    equiv_permutations(root_children, [bst.root.key], equiv_list)
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
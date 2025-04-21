# FILE: _equiv_permu_.py

from BST import *

def get_children(node: Node) -> list:
    children = []
    if node.left is not None:
        children.append(node.left)
    if node.right is not None:
        children.append(node.right)
    return children

def get_equiv_permutations_(equiv_list, CurrNode, Visited_List, Prev_Choice_List):

    # 1. Check feasibility
    if len(Prev_Choice_List) == 0:
        equiv_list.append(Visited_List)
        return
    
    # 2. Construct choice list for the current node
    Choice_List = []
    if CurrNode != None:
        Choice_List.extend(get_children(CurrNode))    
        Choice_List.extend(Prev_Choice_List)
        Choice_List.remove(CurrNode)

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
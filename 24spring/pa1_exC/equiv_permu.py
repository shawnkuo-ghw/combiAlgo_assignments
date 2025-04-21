# FILE: equiv_permu.py

from BST import *

def get_children(node: Node) -> list:
    children = []
    if node.left is not None:
        children.append(node.left)
    if node.right is not None:
        children.append(node.right)
    return children

def get_equiv_permutaions(bst: BST) -> list:
    equiv_list = list()
    children = get_children(bst.root)
    equiv_permutations(children, [bst.root.key], equiv_list)
    return equiv_list

def equiv_permutations(children: list, key_list: list, equiv_list: list):
    # 1. Check feasibility
    if len(children) == 0:
        equiv_list.append(key_list)
        return
    for i in range(len(children)):
        node = children[i]
        del children[i]
        new_children = get_children(node) + children 
        equiv_permutations(new_children, key_list+[node.key],  equiv_list)
        children.insert(i, node)

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
    ret_list = list()
    equiv_permutations(get_children(bst.root), [bst.root.key], ret_list)
    return ret_list

def equiv_permutations(children: list, key_list: list, ret_list: list):
    if len(children) == 0:
        ret_list.append(key_list)
        return
    for i in range(len(children)):
        node = children[i]
        del children[i]
        new_children = get_children(node) + children 
        equiv_permutations(new_children, key_list+[node.key], ret_list)
        children.insert(i, node)

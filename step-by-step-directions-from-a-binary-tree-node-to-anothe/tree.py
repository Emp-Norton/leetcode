import sys

from graphviz import Digraph

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while queue and i < len(arr):
        node = queue.pop(0)
        if arr[i] != 'null':
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] != 'null':
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

def visualize_tree(root):
    if not root:
        return

    dot = Digraph()

    def add_edges(node):
        if node.left:
            dot.node(str(id(node.left)), str(node.left.val))
            dot.edge(str(id(node)), str(id(node.left)))
            add_edges(node.left)
        if node.right:
            dot.node(str(id(node.right)), str(node.right.val))
            dot.edge(str(id(node)), str(id(node.right)))
            add_edges(node.right)

    dot.node(str(id(root)), str(root.val))
    add_edges(root)
    dot.render('binary_tree', format='png', view=True)

def parse_input():
    ins = sys.argv[1]
    arr = ins.split(',')
    return [e if e != 'null' else None for e in arr]

def main():
    arr = parse_input()
    print(arr)
    root = build_tree(arr)
    visualize_tree(root)

if __name__ == "__main__":
    main()

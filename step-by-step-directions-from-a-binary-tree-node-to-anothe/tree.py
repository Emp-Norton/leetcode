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
    queue = [(root, 0)]

    while queue:
        node, i = queue.pop(0)

        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(arr):
            if arr[left_index] != 'null':
                node.left = TreeNode(arr[left_index])
                queue.append((node.left, left_index))
            else:
                node.left = None

        if right_index < len(arr):
            if arr[right_index] != 'null':
                node.right = TreeNode(arr[right_index])
                queue.append((node.right, right_index))
            else:
                node.right = None

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
        else:
            null_id = f"{id(node)}-left"
            dot.node(null_id, "null")
            dot.edge(str(id(node)), null_id)
        
        if node.right:
            dot.node(str(id(node.right)), str(node.right.val))
            dot.edge(str(id(node)), str(id(node.right)))
            add_edges(node.right)
        else:
            null_id = f"{id(node)}-right"
            dot.node(null_id, "null")
            dot.edge(str(id(node)), null_id)

    dot.node(str(id(root)), str(root.val))
    add_edges(root)
    dot.render('binary_tree', format='png', view=True)

def main():
    arr = [1, 'null', 10, 12, 13, 4, 6, 'null', 15, 'null', 'null', 5, 11, 'null', 2, 14, 7, 'null', 8, 'null', 'null', 'null', 9, 3]
    root = build_tree(arr)
    visualize_tree(root)

if __name__ == "__main__":
    main()

def get_path(node: TreeNode, s_val: int, path: str) -> str:
    if node.val == s_val:
            return path
    else:
        children = filter(None, [node.left, node.right])
        dirs = {0: 'L', 1: 'R'}
        for i, n in enumerate(list(children)):
            res =  get_path(n, s_val, path+dirs[i])
            if res:
              return res 
    return None

def get_directions(root, startValue: int, destValue: int) -> str:
    start_path = get_path(root, startValue, '')
    dest_path = get_path(root, destValue, '')
    start_path = ''.join(['U' for n in start_path])
    return start_path + dest_path

def make_tree():
    ll = TreeNode(3)
    l = TreeNode(1, left=ll)
    rl = TreeNode(6)
    rr = TreeNode(4)
    r = TreeNode(2, left=rl, right=rr)
    root = TreeNode(5, left=l, right=r)
    return root
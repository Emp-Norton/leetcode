# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #        self.right = right
# class Solution:
#     def get_path(self, node: TreeNode, s_val: int, path: str) -> str:
#         if node.val == s_val:
#                 return path
#         else:
#             children = [node.left, node.right]
#             dirs = {0: 'L', 1: 'R'}

#             for i, n in enumerate(list(children)):
#                 if n is not None:
#                     if len(list(children)) == 1:
#                         direction = "L" if node.left is not None else "R"
#                     else:
#                         direction = path + dirs[i]
#                     res =  self.get_path(n, s_val, direction)
#                     if res:
#                         return res 
#             return None

#     def getDirections(self, root, startValue: int, destValue: int) -> str:
#         print("get start")
#         start_path = self.get_path(root, startValue, '')
#         print('get dest')
#         dest_path = self.get_path(root, destValue, '')
#         # start_from_common = ''
#         # dest_from_common = ''
#         if len(start_path) > 0 and len(dest_path) > 0:
#             diverge = 0
#             for i in range(min(len(start_path), len(dest_path))):
#                 if start_path[i] == dest_path[i]:
#                     diverge += 1 
#                 else:
#                     break 
#                     # start_from_common += start_path[i]
#                     # dest_from_common = dest_path[i]
#             start_path = start_path[diverge:]
#             dest_path = dest_path[diverge:]
#         start_path = ''.join(['U' for n in start_path])
#         return start_path + dest_path

class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def find(n: TreeNode, val: int, path: List[str]) -> bool:
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path += "L"
            elif n.right and find(n.right, val, path):
                path += "R"
            return path

        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))

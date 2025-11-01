from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        res = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_len = len(queue)
            # print("level", level_len)
            for _ in range(level_len):
                node = queue.popleft()
                level_sum += node.val
                # print("node", node)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level_sum/level_len)


        return res
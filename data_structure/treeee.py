# encoding: utf-8
from data_structure.base import TreeNode


# 完全二叉树
class Tree():
    def __init__(self, node=None):
        if node:
            self.root = TreeNode(node)
        else:
            self.root = None

    def add(self, node):
        node = TreeNode(node)
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        # 层次遍历,广度优先
        while queue:
            cur = queue.pop(0)
            if cur.left == None:
                cur.left = node
                return
            elif cur.right == None:
                cur.right = node
                return
            else:
                queue.append(cur.left)
                queue.append(cur.right)

    def level_order(self):
        res = []
        if not self.root:
            return None
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        print(res)
        return res

    def post_order(self, node):
        if not node:
            return []
        res = self.post_order(node.left)
        res += self.post_order(node.right)
        res.append(node.val)
        return res

    def post_order_stack(self):
        if not self.root:
            return []
        stack1, stack2 = [self.root], []
        res = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        for i in stack2[::-1]:
            res.append(i.val)
        return res


tree = Tree()
for i in range(1, 11):
    tree.add(i)
print(tree.post_order(tree.root))
print(tree.post_order_stack())

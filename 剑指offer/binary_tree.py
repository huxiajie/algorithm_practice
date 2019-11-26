'''
number 1
实现二叉树
'''


class Node():
    def __init__(self, val, left_child=None, right_child=None):
        self.val = val
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree():
    def __init__(self, val=None):
        self.root = Node(val)

    def add(self, val):
        node = Node(val)
        # 根节点赋值
        if not self.root.left_child and not self.root.right_child:
            self.root = node
        # 子节点赋值



'''
number 2
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

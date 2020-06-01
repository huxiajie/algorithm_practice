# encoding: utf-8
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class TreeNode():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

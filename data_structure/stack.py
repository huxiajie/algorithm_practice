'''
number 1
实现栈: python-list动态顺序表支持栈;用链表实现栈；
'''
from data_structure.linkedlist import Node


class StackPythonList():
    def __init__(self, element_list=None, length=0):
        if element_list:
            self.stack = element_list
        elif length != 0:
            self.stack = [None] * length
        else:
            self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def read_top_element(self):
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        return self.stack == []


class StackLinkedList():
    def __init__(self, element_list=None, length=0):
        self.head = None
        if element_list:
            for ele in element_list:
                self.push(ele)
        elif length != 0:
            for i in range(length):
                self.push(None)

    def push(self, element):
        element = Node(val=element)
        if self.head:
            element.next = self.head
        self.head = element


    def pop(self):
        if self.head:
            element = self.head
            self.head = self.head.next
            return element.val
        return None


    def read_top_element(self):
        return self.head.val

    def is_empty(self):
        return self.head == None


if __name__ == "__main__":
    s1 = StackPythonList([1, 2, 3])
    s2 = StackLinkedList([1,2,3])
    s2.push(4)
    s2.push(5)
    while not s2.is_empty():
        print(s2.pop())

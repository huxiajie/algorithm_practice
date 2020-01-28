'''
number 1
实现链表
'''


# 定义节点类
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList():
    # 初始化，创建空链表
    def __init__(self):
        self.head = Node()

    # 删除链表
    def del_list(self):
        self.head.next = None

    # 按元素定位:满足条件的第一个节点
    def locate_by_element(self, val):
        p = self.head
        while p.next:
            p = p.next
            if p.val == val:
                return p
        return None

    def insert_head(self, node):
        node.next = self.head.next
        self.head.next = node
        # temp = self.head.next
        # temp.next = self.head.next
        # self.head.next = node

    def insert_end(self, node):
        end = self.head
        while end.next:
            end = end.next
        end.next = node

    def del_head(self):
        self.head.next = self.head.next.next1


'''
number 2
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
'''

linked_list_test = LinkedList()
for i in range(10):
    linked_list_test.insert_end(Node(i))


# 法1：获得正序list，倒序访问list
def show_from_end_to_head1(linked_list):
    temp = linked_list.head.next
    res = []
    res_reserve = []
    while temp:
        res.append(temp.val)
        temp = temp.next
    # print(res)
    # range(a,b) => [a,b)
    for i in range(len(res) - 1, -1, -1):
        res_reserve.append(res[i])
    # print(res_reserve)
    return res_reserve


# 法2：正序访问链表，倒序插入arraylist(倒序插入比较慢)
def show_from_end_to_head2(linked_list):
    temp = linked_list.head.next
    res_reserve = []
    while temp:
        res_reserve.insert(0, temp.val)
        temp = temp.next
    # print(res_reserve)
    return res_reserve


'''
number 3
链表原地反转
'''
# 迭代反转
def reverse_linkedlist1(linkedlist):
    # 最少有两个节点
    if not linkedlist.head.next.next:
        return linkedlist
    p, pre = linkedlist.head.next
    while p:
        pre = p
        p = p.next
        p.next = pre
    linkedlist.head.next.next = None
    linkedlist.head = pre
    return linkedlist
# 递归反转
def reverse_linkedlist2():
    pass

'''
number 4
链表排序
'''

'''
number 5
约瑟夫（Josephus）问题
'''

if __name__ == "__main__":
    show_from_end_to_head1(linked_list_test)

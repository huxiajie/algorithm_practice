'''
number 1
实现链表
'''


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():
    # 初始化，头结点为空
    def __init__(self):
        self.head = Node(None)
        self.end = self.head

    # 添加节点
    def add(self, data):
        self.end.next = Node(data)
        self.end = self.end.next


'''
number 2
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
'''

linked_list_test = LinkedList()


# linked_list_test.add(1)
# linked_list_test.add(2)
# linked_list_test.add(3)
# linked_list_test.add(4)
# linked_list_test.add(5)


def show_from_end_to_head1(linked_list):
    # 正序输出，反转arraylist
    temp = linked_list.head.next
    res = []
    res_reserve = []
    while temp:
        res.append(temp.val)
        temp = temp.next
    print(res)
    for i in range(len(res) - 1, -1, -1):
        res_reserve.append(res[i])
    print(res_reserve)
    return res_reserve


def show_from_end_to_head2(linked_list):
    # 正序访问链表，倒序插入arraylist
    temp = linked_list.head.next
    res_reserve = []
    while temp:
        res_reserve.insert(0, temp.val)
        temp = temp.next
    print(res_reserve)
    return res_reserve

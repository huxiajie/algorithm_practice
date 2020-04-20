'''
number 1
实现链表
'''


class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Linkedlist():
    # 初始化，创建空链表或非空链表
    # head指向第一个节点
    def __init__(self, val=None, next=None, head=None):
        # 指定头节点创建链表
        if head:
            self.head = head
        # 空链表
        elif not val:
            self.head = None
        # 创建有一个节点的链表
        else:
            self.head = Node(val, next)

    # 删除链表
    def del_list(self):
        self.head = None

    # 是否空链表
    def if_empty(self):
        if self.head:
            return False
        return True

    def get_last_node(self):
        if self.if_empty():
            return None
        p = self.head
        while p.next:
            p = p.next
        return p

    def insert_first(self, node):
        node.next = self.head
        self.head = node

    def insert_last(self, node):
        end = self.get_last_node()
        if end:
            end.next = node
        else:
            self.head = node

    def delete_first(self):
        if self.if_empty():
            return
        self.head = self.head.next

    def print_linkedlist(self):
        printlist = []
        p = self.head
        while p:
            printlist.append(p.val)
            p = p.next
        print("打印链表：", printlist)

    def get_len(self):
        length=0
        p=self.head
        while p:
            length+=1
        return length

    # 按元素定位:满足条件的第一个节点
    def locate_by_element(self, val):
        p = self.head
        while p:
            if p.val == val:
                return p
            p = p.next
        return None


'''
number 2
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
'''


# 法1：获得正序list，倒序访问list
def show_from_end_to_head1(linked_list):
    temp = linked_list.head.next
    res = []
    res_reserve = []
    while temp:
        res.append(temp.val)
        temp = temp.next
    # range(a,b) => [a,b)
    for i in range(len(res) - 1, -1, -1):
        res_reserve.append(res[i])
    return res_reserve


# 法2：正序访问链表，倒序插入arraylist(倒序插入比较慢)
def show_from_end_to_head2(linked_list):
    temp = linked_list.head.next
    res_reserve = []
    while temp:
        res_reserve.insert(0, temp.val)
        temp = temp.next
    return res_reserve


'''
number 3
链表原地反转
'''


# 法1【O(n)】：迭代反转，需要before p after 三个变量做支撑
def reverse_linkedlist1(linkedlist):
    # 要求至少有一个节点
    if not linkedlist or not linkedlist.head.next:
        return linkedlist
    # 错误写法：p, pre = linkedlist.head.next
    p = linkedlist.head.next
    # clever step
    before = None
    while p:
        # 把后移after node动作放到最前面的原因：
        #   如果p是最后一个节点，执行最后一轮循环
        #   如果后移after node在最后一句，则会报错
        after = p.next
        p.next = before
        before = p
        p = after
    linkedlist.head.next = before
    return linkedlist

# 法2【O(n)】：递归反转，利用递归的方式可以定位previous node
# https://blog.csdn.net/w605283073/article/details/86653745
def reverse_linkedlist2(node):
    # 空链表 or 找到last node
    if not node or not node.next:
        return node
    newhead = reverse_linkedlist2(node.next)
    # clever step
    node.next.next = node
    # 如若缺少这一步，在原链表的第一个节点的next值将无法被置为None
    node.next = None
    return newhead


if __name__ == "__main__":
    linked_list_test = Linkedlist()
    for i in range(100):
        linked_list_test.insert_last(Node(i))

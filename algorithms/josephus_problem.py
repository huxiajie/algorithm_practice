'''
number 1
约瑟夫（Josephus）问题
假设有n个人围坐一圈，现在要求从第k个人开始报数，报到第m个数的人退出。
然后从下一个人开始继续报数并按照同样的规则退出，直至所有人都退出。
按照顺序输出 退出的人 的编号
'''
from data_structure.collectionnn.sequenceee.linkedlist import Linkedlist, Node


# 基于list求解 O(n)
def josephus1(n, k, m):
    out_list = []
    if n <= 0 or k > n:
        return out_list
    people = list(range(1, n + 1))
    # clever step
    out_person = k - 1
    # 进行（0, n] n轮
    for length in range(n, 0, -1):
        # clever step
        out_person = (out_person + m - 1) % length
        out_list.append(people.pop(out_person))
    return out_list


# 基于循环单链表求解 O(m*n)
def josephus2(n, k, m):
    out_list = []
    if n <= 0 or k > n:
        return out_list

    people = Linkedlist(val=1)
    for i in range(2, n + 1):
        people.insert_last(Node(i))
    out_person_prev = people.get_last_node()
    people.get_last_node().next = people.head
    for i in range(k - 1):
        out_person_prev = out_person_prev.next

    while out_person_prev.next!=out_person_prev:
        for i in range(m - 1):
            out_person_prev = out_person_prev.next
        out_list.append(out_person_prev.next.val)
        out_person_prev.next = out_person_prev.next.next
    out_list.append(out_person_prev.val)
    return out_list

n = 9
k = 1
m = 5
print("1", josephus1(n, k, m))
print("2", josephus2(n, k, m))

'''
number 1
实现队列: python-list实现队列;用链表实现队列；
'''
from data_structure.collectionnn.sequenceee.linkedlist import Node


# 法1：enqueue使用append,O(1);出队使用pop(0),O(n)
# 法2：enqueue使用insert(0,ele),O(n);出队使用pop(),O(1)
# 法1类似法2，效果均不理想
# 法3：基于法1，队首元素出队后，队列元素不移动，重新记住队首位置
#      队尾位置不应无限+1，应该重新利用 0-队首 的空间
#      队列满时，需要扩容
#      当队列不满时，出入队列均为O(1)
#      当队列满了时，入队为O(n),出队为O(1)
class QueuePythonList():
    def __init__(self, element_list=None):
        self.head = 0
        self.rear = 0
        self.count = 0
        if element_list:
            self.queue = element_list
            self.rear = len(element_list) - 1
            self.count = len(element_list)
        else:
            # 注意 不能为[]
            self.queue = [None] * 2

    # 注意思路：分别要处理哪些变量
    def enqueue(self, element):
        # 处理rear
        if self.count == 0:
            self.queue[self.head] = element
        elif self.count == len(self.queue):
            new_queue_double = [None] * (self.count * 2)
            for i in range(self.count):
                new_queue_double[i] = self.queue[(self.head + i) % len(self.queue)]
            self.queue, self.head, self.rear = new_queue_double, 0, self.count
            self.queue[self.rear] = element
        else:
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = element
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return None
        element = self.queue[self.head]
        self.count -= 1
        if self.count != 0:
            self.head = (self.head + 1) % len(self.queue)
        return element

    def read_first_element(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def is_empty(self):
        return self.count == 0


class QueueLinkedList():
    def __init__(self, element_list=None, length=0):
        self.head = None
        self.rear = self.head
        if element_list:
            for ele in element_list:
                self.enqueue(ele)
        elif length != 0:
            for i in range(length):
                self.enqueue(None)

    def enqueue(self, element):
        element = Node(val=element)
        if self.head:
            self.rear.next = element
        else:
            self.head = element
        self.rear = element

    def dequeue(self):
        if self.head:
            element = self.head
            self.head = self.head.next
            return element.val
        return None

    def read_first_element(self):
        return self.head.val

    def is_empty(self):
        return self.head == None


if __name__ == "__main__":
    s1 = QueuePythonList()
    s2 = QueueLinkedList([1, 2, 3])
    s1.enqueue(1)
    print(s1.queue)
    print("head, rear, count:", s1.head, s1.rear, s1.count)
    s1.enqueue(2)
    print(s1.queue)
    print("head, rear, count:", s1.head, s1.rear, s1.count)
    while not s1.is_empty():
        print(s1.dequeue())
    print("====")
    print(s1.queue)
    print("head, rear, count:", s1.head, s1.rear, s1.count)
    print("====")
    s1.enqueue(3)
    print(s1.queue)
    print("head, rear, count:", s1.head, s1.rear, s1.count)
    s1.enqueue(4)
    print(s1.queue)
    print("head, rear, count:", s1.head, s1.rear, s1.count)
    s1.enqueue(5)
    print(s1.queue)
    print("head, rear, count:", s1.head, s1.rear, s1.count)
    s1.enqueue(6)
    print(s1.queue)
    print("head, rear, count:", s1.head, s1.rear, s1.count)
    print("====pop===")
    while not s1.is_empty():
        print(s1.dequeue())
        print("head, rear, count:", s1.head, s1.rear, s1.count)

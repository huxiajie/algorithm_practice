from data_structure.collectionnn.sequenceee.stack import StackPythonList
from data_structure.collectionnn.sequenceee.qqueue import QueuePythonList

maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# 右 下 左 上 clever step
# 如何去表示neighbors,以及如何确定neighbor之间是否passable
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

'''
number 1
找出一条路径即可
'''


# 法1：递归法（使用系统栈）深度优先
# 时间复杂度？？？？
# 直到走到出口, 返回True, 然后一路向上返回True
# 死节点 返回false
def solution1(start_pos, end_pos, maze):
    # 对于已经check的节点要加以标注,让下一个节点不走回头路,对被标记的节点本身不受影响
    maze[start_pos[0]][start_pos[1]] = 2
    if start_pos == end_pos:
        return True
    for dir in directions:
        i = start_pos[0] + dir[0]
        j = start_pos[1] + dir[1]
        if i >= 0 and i < len(maze) and j >= 0 and j < len(maze[0]) and maze[i][j] == 0:
            if solution1(start_pos=(i, j), end_pos=end_pos, maze=maze):
                print(start_pos)
                return True
    return False


# 法2：使用栈记录（下一个节点位置，下一节点位置，如果回溯在原先探索位置的基础上进行探索）深度优先
# 用自己的栈代替系统栈
def solution2(start_pos, end_pos, maze):
    path = StackPythonList()
    path.push((start_pos, 0))
    if start_pos == end_pos:
        return path.stack
    while not path.is_empty():
        current_pos = path.pop()
        maze[current_pos[0][0]][current_pos[0][1]] = 2
        for dir in range(current_pos[1], 4):
            i = current_pos[0][0] + directions[dir][0]
            j = current_pos[0][1] + directions[dir][1]
            if i >= 0 and i < len(maze) and j >= 0 and j < len(maze[0]) and maze[i][j] == 0:
                path.push((current_pos[0], dir + 1))
                path.push(((i, j), 0))
                if (i, j) == end_pos:
                    return path.stack
                break
    return False


# 法3：使用队列 宽度优先
# 无法记录具体路径 只有false or true
def solution3(start_pos, end_pos, maze):
    path = QueuePythonList()
    path.enqueue(start_pos)
    if start_pos == end_pos:
        return True
    while not path.is_empty():
        current_pos = path.dequeue()
        maze[current_pos[0]][current_pos[1]] = 2
        for dir in directions:
            i = current_pos[0] + dir[0]
            j = current_pos[1] + dir[1]
            if i >= 0 and i < len(maze) and j >= 0 and j < len(maze[0]) and maze[i][j] == 0:
                path.enqueue((i, j))
                if (i, j) == end_pos:
                    return True
    return False


print(solution3(start_pos=(1, 1), end_pos=(10, 12), maze=maze))

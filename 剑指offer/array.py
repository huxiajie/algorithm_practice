'''
number 1
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
def func(array, num):
    # 注意空值
    if not array:
        return False
    row = 0
    # len()是从1开始计算的
    col = len(array[0])-1
    while col >= 0 and row <= len(array)-1:
        if num == array[row][col]:
            return True
        elif num > array[row][col]:
            row += 1
        elif num < array[row][col]:
            col -= 1
    return False

# array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
# print(func(array, 7))

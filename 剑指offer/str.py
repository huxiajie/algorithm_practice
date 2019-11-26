'''
number 1
将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
def replace1(s):
    # s 不会被改变，replace()方法会生成一个新的字符串
    a = s.replace(' ', '%20')
    return s.replace(' ', '%20')

def replace2(s):
    a = s
    s = list(s)
    # a仍为源字符串 不会变成list
    # print(a)
    count = len(s)
    for i in range(0, count):
        if s[i] == ' ':
            s[i] = '%20'
    # s 不会被改变，join()方法会生成一个新的字符串
    return ''.join(s)